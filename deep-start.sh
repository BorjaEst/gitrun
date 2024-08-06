#!/bin/bash

# Set default values
JENKINS_URL="${JENKINS_URL:?JENKINS_URL env is required}"
JENKINS_USERNAME=""
JENKINS_PASSWORD=""
EXECUTION_LABEL=""

# Parse command line arguments for username, password, and label
while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
    -l | --url)
        JENKINS_URL="$2"
        shift # past argument
        shift # past value
        ;;
    -u | --username)
        JENKINS_USERNAME="$2"
        shift # past argument
        shift # past value
        ;;
    -p | --password)
        JENKINS_PASSWORD="$2"
        shift # past argument
        shift # past value
        ;;
    *)
        EXECUTION_LABEL="$1"
        shift # past argument
        ;;
    esac
done

# Check EXECUTUON_LABEL argument is not empty

if [[ -z $EXECUTION_LABEL ]]; then
    echo "Error: Execution label argument is required."
    exit 1
fi

# Trigger the Jenkins job
java -jar /srv/swarm-client.jar \
    -url ${JENKINS_URL} \
    -mode "exclusive" \
    -labels ${EXECUTION_LABEL} \
    -username ${JENKINS_USERNAME} \
    -password ${JENKINS_PASSWORD}
