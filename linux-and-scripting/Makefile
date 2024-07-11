default: all

NAME=linux-challenges

all: build run

build:
	docker build --platform linux/amd64 . -t $(NAME)-build

run:
	docker run --name $(NAME)-run -it --rm $(NAME)-build

kill:
	docker kill $(NAME)-run
