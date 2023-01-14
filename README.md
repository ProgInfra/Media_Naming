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
  - [Development](#development)
    - [Build and Deploy](#build-and-deploy)
    - [Requirements](#requirements)
    - [Docsify](#docsify)
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

## Development

If you want you can **develop** this repository :

1) You need to install the [Requirements](#requirements)
2) You can develop on [Naming Script](#build-and-deploy)
3) You can develop on [Docsify](#docsify)

### Build and Deploy

**Build** :

```bash
docker-compose build
docker-compose run --rm media-naming pdm install
```

**Launch** :

```bash
# Bash
docker-compose run --rm media-naming bash
pdm run python ./src/naming.py --help

# Launch Simple Command
docker-compose run --rm media-naming pdm run python ./src/naming.py --help
```

**Deploy** :

```bash
# Build
pdm build
# Install locally
pip install ./dist/naming-1.0.0-py3-none-any.whl
# Test locally
python -m naming --help
```

**Publish** :

```bash
TODO https://typer.tiangolo.com/tutorial/package/#publish-to-pypi-optional
pdm publish
```

### Requirements

We use **Docker** :

- Docker
- Docker Compose

### Docsify

```bash
cd docsify

# Development
docker-compose -f docker-compose.dev.yml up

# Production
docker-compose up --build
```

## Contributing

See [CONTRIBUTING](./CONTRIBUTING.md) for more information.

## Licence

This project is licensed under the terms of the MIT license.

See [LICENSE](./LICENCE.md) for more information.
