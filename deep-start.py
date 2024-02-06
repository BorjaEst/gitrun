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
parser.add_argument(
    *["--jitconfig"],
    help="Encoded JIT configuration for the runner",
    type=int,
    default=10,
)


# Script command actions --------------------------------------------
def _run_command(jitconfig, **options):
    # Common operations
    logging.basicConfig(level=options["verbosity"])

    # Run the main program
    logger.info("Running the main program")
    cmd = ["./run.sh", f"--jitconfig={jitconfig}"]
    subprocess.run(cmd, check=True)

    # End of program
    logger.info("End of github runner script")


# Main call ---------------------------------------------------------
if __name__ == "__main__":
    args = parser.parse_args()
    _run_command(**vars(args))
    sys.exit(0)  # Shell return 0 == success
