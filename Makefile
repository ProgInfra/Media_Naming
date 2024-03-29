# Production
publish: publish-docker
	docker compose -f ./docker/docker-compose.dev.yml run --rm -it media-naming-dev pdm publish

publish-docker: build
	docker login
	docker push progower/media-naming:1.4.0

build: build-dev generate-docs
	docker compose -f ./docker/docker-compose.yml build

start:
	docker compose -f ./docker/docker-compose.yml up

start-detach:
	docker compose -f ./docker/docker-compose.yml up -d

stop:
	docker compose -f ./docker/docker-compose.yml down

generate-docs:
	docker compose -f ./docker/docker-compose.dev.yml run --rm -it media-naming-dev bash -c "cd src && pdm run docs"


start-docs:
	docker compose -f ./docsify/docker-compose.yml up --build

stop-docs:
	docker compose -f ./docsify/docker-compose.yml down


# Development
bash:
	docker compose -f ./docker/docker-compose.dev.yml run --rm -it media-naming-dev bash 

lint:
	docker compose -f ./docker/docker-compose.dev.yml run --rm -it media-naming-dev pdm run flake8

build-dev:
	docker compose -f ./docker/docker-compose.dev.yml build
	docker compose -f ./docker/docker-compose.dev.yml run --rm -it media-naming-dev pdm install

start-dev:
	docker compose -f ./docker/docker-compose.dev.yml up

start-detach-dev:
	docker compose -f ./docker/docker-compose.dev.yml up -d

stop-dev:
	docker compose -f ./docker/docker-compose.dev.yml down


start-docs-dev:
	docker compose -f ./docsify/docker-compose.dev.yml up

stop-docs-dev:
	docker compose -f ./docsify/docker-compose.dev.yml down


# Workspace
w-init:
	mkdir -p ./workspace
	mkdir -p ./workspace/01-todo
	mkdir -p ./workspace/02-doing
	mkdir -p ./workspace/03-done
	echo "# Example : naming media serie "TODO" -t "anime" -db "TODO" -id "TODO" -ns 0" > ./workspace/working.sh
	docker compose -f ./docker/docker-compose.dev.yml run --rm -it media-naming-dev pdm run naming media init -o ./workspace/medias

w-start-test:
	docker compose -f ./docker/docker-compose.workspace.yml up

w-stop-test:
	docker compose -f ./docker/docker-compose.workspace.yml down
