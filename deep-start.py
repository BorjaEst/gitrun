#!/usr/bin/env python3
"""Start the github runner and run the main program.
"""
import argparse
import logging
import subprocess
import sys


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
parser.add_argument(  # TODO: Remove this flag when the deepaas entrypoint is fixed
    *["--deepaas"],
    help="Hacky flag to bypass the deepaas entrypoint",
    action="store_true",
    required=False,
)
parser.add_argument(
    *["--url"],
    help="Repository to add the runner to",
    type=str,
    required=True,
)
parser.add_argument(
    *["--token"],
    help="Registration token",
    type=str,
    required=True,
)
parser.add_argument(
    *["--jitconfig"],
    help="Encoded JIT configuration for the runner",
    type=str,
    required=True,
)


# Script command actions --------------------------------------------
def _run_command(url, token, jitconfig, **options):
    # Common operations
    logging.basicConfig(level=options["verbosity"])

    # Run the runner configuration
    logger.info("Running the runner configuration")
    cmd = ["./config.sh", "--unattended", "--url", url, "--token", token]
    subprocess.run(cmd, check=True)

    # Run the main program
    logger.info("Running the main program")
    cmd = ["./run.sh", "--jitconfig", jitconfig]
    subprocess.run(cmd, check=True)

    # End of program
    logger.info("End of github runner script")


# Main call ---------------------------------------------------------
if __name__ == "__main__":
    args = parser.parse_args()
    _run_command(**vars(args))
    sys.exit(0)  # Shell return 0 == success
