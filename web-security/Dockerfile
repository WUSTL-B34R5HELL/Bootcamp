FROM python:3.10.13-alpine

RUN mkdir /src
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY wrapper_script.sh /src/wrapper_script.sh
COPY example-site /src/example-site
COPY challenge-site /src/challenge-site
COPY http-server /src/http-server
EXPOSE 8000 8001 8002

WORKDIR /src
ENTRYPOINT ["./wrapper_script.sh"]