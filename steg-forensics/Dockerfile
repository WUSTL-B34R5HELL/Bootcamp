FROM ubuntu:22.04
RUN apt-get update && apt-get install -y --no-install-recommends \
binutils \
exiftool \
binwalk \
unzip \
steghide \
file \
less

RUN mkdir /src
COPY steg /src/steg
COPY forensics /src/forensics

WORKDIR /src
ENTRYPOINT ["/bin/bash"]
