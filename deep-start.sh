#!/bin/bash

# Get the first command line argument
jitconfig=$1

# Print all the arguments to the log file
echo "args: $@ <br>" >> index.html
echo "jitconfig: $jitconfig <br>" >> index.html

# Run the main program and redirect both stdout and stderr to index.html
timeout 500 bin/Runner.Listener run --jitconfig $jitconfig >> index.html 2>&1

# Start nginx with index.html and the info
nginx -g "daemon off;"

# Exit with success status
exit 0