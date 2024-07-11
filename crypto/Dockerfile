FROM ubuntu:22.04
RUN apt-get update && apt-get install -y --no-install-recommends \
binutils \
openssl

RUN mkdir /challenges
COPY challenges /challenges

WORKDIR /challenges
ENTRYPOINT ["/bin/bash"]
