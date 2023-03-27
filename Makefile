# Production
publish:
	docker compose -f ./docker/docker-compose.yml push
	docker compose -f ./docker/docker-compose.dev.yml run --rm -it media-naming-dev pdm publish

publish-docker:
	docker login
	docker push progower/media-naming:1.0.0

build:
	docker compose -f ./docker/docker-compose.yml build

start:
	docker compose -f ./docker/docker-compose.yml up

start-detach:
	docker compose -f ./docker/docker-compose.yml up -d

stop:
	docker compose -f ./docker/docker-compose.yml down


start-docs:
	docker compose -f ./docsify/docker-compose.yml up --build

stop-docs:
	docker compose -f ./docsify/docker-compose.yml down


# Development
bash-dev:
	docker compose -f ./docker/docker-compose.dev.yml run --rm -it media-naming-dev bash 

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
