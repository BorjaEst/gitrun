#!/usr/bin/env python3
"""Start the github runner and run the main program.
"""
import argparse
import logging
import subprocess
import sys
import urllib.parse

import requests

logger = logging.getLogger(__name__)


# Script arguments definition ---------------------------------------
parser = argparse.ArgumentParser(
    prog="PROG",
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog="See '<command> --help' to read about a specific sub-command.",
)
parser.add_argument(
    *["-v", "--verbosity"],
    help="Sets the logging level (default: %(default)s)",
    type=str,
    choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
    default="INFO",
)
parser.add_argument(
    *["-t", "--token"],
    help="Token to register runner in the GitHub repository.",
    type=str,
    required=True,
)
parser.add_argument(
    *["-u", "--url"],
    help="Github repository where to store the runner.",
    type=urllib.parse.urlparse,
    required=True,
)
parser.add_argument(
    *["--timeout"],
    help="Timeout for the HTTP requests (default: %(default)s)",
    type=int,
    default=10,
)


# Script command actions --------------------------------------------
def _run_command(token, url, **options):
    # Common operations
    logging.basicConfig(level=options["verbosity"])

    # Exchange token the GitHub token with a real access token
    logger.info("Exchange token for access token")
    response = requests.post(
        url=f"{url.geturl()}/actions/runners/registration-token",
        headers={
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json",
        },
        timeout=options["timeout"],
    )

    # Check if the request was successful
    logger.debug("Response: %s", response.status_code)
    match response.status_code:
        case 200:
            token = response.json()["token"]
        case _:
            response.raise_for_status()

    # Configure the runner
    logger.info("Configuring the runner")
    cmd = ["./config.sh", "--url", url.geturl(), "--token", token]
    subprocess.run(cmd, check=True)

    # Run the main program
    logger.info("Running the main program")
    cmd = ["./run.sh"]
    subprocess.run(cmd, check=True)

    # End of program
    logger.info("End of github runner script")


# Main call ---------------------------------------------------------
if __name__ == "__main__":
    args = parser.parse_args()
    _run_command(**vars(args))
    sys.exit(0)  # Shell return 0 == success
