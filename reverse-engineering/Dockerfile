FROM ubuntu:22.04
RUN apt-get update && apt-get install -y --no-install-recommends \
binutils \
gdb \
python3 \
less \
vim

RUN mkdir /challenges
COPY challenges /challenges

WORKDIR /challenges
ENTRYPOINT ["/bin/bash"]
