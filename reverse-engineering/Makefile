default: all

NAME=reverse-challenges

all: build run

build:
	docker build . -t $(NAME)-build

run:
	docker run --name $(NAME)-run -it --rm $(NAME)-build

kill:
	docker kill $(NAME)-run
