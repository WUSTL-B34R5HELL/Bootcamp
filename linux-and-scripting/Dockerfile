FROM ubuntu:22.04
RUN apt-get update && apt-get install -y --no-install-recommends \
binutils \
less \
netcat \
tmux \
vim \
man-db \
adduser \
gzip

RUN yes | unminimize #include man pages
COPY src/.init /
RUN chmod 500 /.init

RUN adduser test_user
RUN cd /home/test_user && /.init

RUN mkdir /home/test_user/challenge3 && chown test_user /home/test_user/challenge3
RUN mkdir /home/test_user/challenge5 && chown test_user /home/test_user/challenge5
RUN mkdir /home/test_user/challenge6 && chown test_user /home/test_user/challenge6

COPY challenges/flag-challenge3 /home/test_user/challenge3
RUN chown test_user /home/test_user/challenge3/flag-challenge3
RUN chmod 000 /home/test_user/challenge3/flag-challenge3

COPY challenges/redirect-to-win /home/test_user/challenge5
RUN chmod 755 /home/test_user/challenge5/redirect-to-win

COPY challenges/test_program /home/test_user/challenge6
RUN chmod 755 /home/test_user/challenge6/test_program

COPY src/entrypoint.sh /home/test_user
RUN chmod +x /home/test_user/entrypoint.sh

USER test_user

WORKDIR /home/test_user/
ENTRYPOINT ["./entrypoint.sh"]
