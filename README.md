# Media Naming

![Icon](./icon.png)

[Storage icons created by Freepik - Flaticon](https://www.flaticon.com/free-icons/storage)

## Table Of Contents

- [Media Naming](#media-naming)
  - [Table Of Contents](#table-of-contents)
  - [Description](#description)
  - [Access](#access)
  - [Documentations](#documentations)
  - [Getting Started](#getting-started)
    - [With Pip](#with-pip)
    - [With Docker](#with-docker)
  - [Development](#development)
    - [Build and Deploy](#build-and-deploy)
  - [Contributing](#contributing)
  - [Licence](#licence)

## Description

How to structure your system (media, computer, ...).

## Access

- **Development (Local)** :
  - [Media Naming Docs Development](http://localhost:6007)
- **Production (Local)** :
  - [Media Naming Docs Production](http://localhost:6007)
- **Production** :
  - [Media Naming Docs Production](https://proginfra.gitlab.io/media_naming)

## Documentations

- [Account Naming](./docs/account.md)
- [System Naming](./docs/system.md)
- [Game Naming](./docs/game.md)
- [Image Naming](./docs/image.md)
- [Book Naming](./docs/book.md)
- [Music Naming](./docs/music.md)
- [Video Naming](./docs/video.md)
- [Tools](./docs/sources.md)
- [Ideas](./docs/ideas.md)

## Getting Started

### With Pip

To **install** it :

```bash
# Install with Pip
pip install --user naming
```

To **use** it :

```bash
naming --help
naming init -o tmp
naming media init -o tmp/medias
naming media image -m tmp/medias -t photo "Summer 2022"
```

### With Docker

To **install** it :

```bash
docker pull progower/media-naming:1.0.0
```

To **use** it :

```bash
alias naming='docker run --rm -it -v ${PWD}:/app --workdir /app progower/media-naming:1.0.0 naming'
naming --help
naming init -o tmp
naming media init -o tmp/medias
naming media image -m tmp/medias -t photo "Summer 2022"
```

## Development

If you want you can **develop** this repository :

1) You need to install **[Docker](https://docs.docker.com/get-docker/)** and **[Make](https://progdevlab.gitlab.io/dyntools/#/docs/global/makefile)**
2) [Build and Deploy](#build-and-deploy) the application

### Build and Deploy

- **Production** :
  - `make publish` : [TODO](https://typer.tiangolo.com/tutorial/package/#publish-to-pypi-optional) with pdm publish
  - `make publish-docker` : Publish in Docker repository
  - `make build` : Build
  - `make start` : Start
  - `make start-detach` : Start in detach mode
  - `make stop` : Stop
  - `make start-docs` : Start Documentation Website
  - `make stop-docs` : Stop Documentation Website
- **Development** :
  - `make bash-dev` : Start a bash into the container to develop (example : `pdm run naming --help`)
  - `make build-dev` : Build
  - `make start-dev` : Start
  - `make start-detach-dev` : Start in detach mode
  - `make stop-dev` : Stop
  - `make start-docs-dev` : Start Documentation Website
  - `make stop-docs-dev` : Stop Documentation Website

## Contributing

See [CONTRIBUTING](./CONTRIBUTING.md) for more information.

## Licence

This project is licensed under the terms of the MIT license.

See [LICENSE](./LICENCE.md) for more information.
