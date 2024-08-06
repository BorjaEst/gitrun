## TODO: TRY IF POSSIBLE TO RUN WITH SMALLER IMAGE LIKE JAVA
ARG JENKINS_AGENT_VERSION=latest
FROM jenkins/inbound-agent:${JENKINS_AGENT_VERSION}

ARG JENKINS_URL
ENV JENKINS_URL=${JENKINS_URL}
USER root

# Install necessary packages
RUN apt-get update && apt-get install -y curl jq

# Download the swarm-client.jar
RUN curl -o /srv/swarm-client.jar ${JENKINS_URL}/swarm/swarm-client.jar

# Copy the entrypoint script
COPY deep-start.sh /srv/deep-start.sh

# Start the registration script
ENTRYPOINT [ "/srv/deep-start.sh" ]
