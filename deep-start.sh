#!/bin/bash

# Get the first command line argument
jitconfig=$1

# Run the main program
bin/Runner.Listener run --jitconfig $jitconfig

# Exit with success status
exit 0