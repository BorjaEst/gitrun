## Coded edited from https://github.com/cwpearson/github-runner-docker
FROM ubuntu:22.04
ENV DEBIAN_FRONTEND noninteractive

# set the github runner version
ARG RUNNER_VERSION="2.312.0"

# update the base packages
RUN apt-get update -y
RUN apt-get install -y --no-install-suggests --no-install-recommends \
    curl \
    ca-certificates \
    python3 \
    jq

# Create the directory for the github runner
RUN adduser --system --group --no-create-home github
RUN mkdir -p /srv/actions-runner
RUN chown -R github:github /srv/actions-runner

# Download and unzip the github actions runner
WORKDIR /srv/actions-runner
RUN curl -O -L https://github.com/actions/runner/releases/download/v${RUNNER_VERSION}/actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz \
    && tar xzf ./actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz \
    && rm ./actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz 

# install some additional dependencies and change ownership
RUN ./bin/installdependencies.sh
RUN chown -R github:github /srv/actions-runner

# copy over the start.sh script
COPY deep-start.py /usr/local/bin/deep-start
RUN chmod +x /usr/local/bin/deep-start

# Create a user to run the github runner
USER github

# set the entrypoint to the deep-start.py script
EXPOSE 5000
CMD [ "deep-start" ]
