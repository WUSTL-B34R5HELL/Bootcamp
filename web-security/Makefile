default: all

NAME=web-challenges

all: build run

build:
	docker build . -t $(NAME)-build

run:
	docker run --name $(NAME)-run -d --rm -p 8000-8002:8000-8002 $(NAME)-build

kill:
	docker kill $(NAME)-run
