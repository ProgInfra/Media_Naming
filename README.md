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

TODO Getting Started Script (get from Pypi)

## Development

If you want you can **develop** this repository :

1) You need to install the [Requirements](#requirements)
2) You can develop on [Docsify](#docsify)

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
