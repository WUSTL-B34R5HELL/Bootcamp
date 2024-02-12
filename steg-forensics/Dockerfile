FROM ubuntu:22.04
RUN apt-get update && apt-get install -y --no-install-recommends \
binutils \
exiftool \
binwalk \
unzip \
steghide \
file \
less \
man-db 

RUN mkdir /src
COPY steg /src/steg
COPY forensics /src/forensics
RUN yes | unminimize

WORKDIR /src
ENTRYPOINT ["/bin/bash"]
