# Media Naming : Naming Workspace

![Icon](../icon.png)

## Table Of Contents

- [Media Naming : Naming Workspace](#media-naming--naming-workspace)
  - [Table Of Contents](#table-of-contents)
  - [Description](#description)
  - [Getting Started](#getting-started)

## Description

This is a special workspace to setup some media with naming cli and test it on Jellyfin to check it.

## Getting Started

First you need to init you naming workspace with `make w-init`

Next you have some folder in `workspace` folder :

- **medias** : Example of medias folders (ebook, musics, ...)
- **01-todo** : Medias to do (preparation of list of folder)
- **02-doing** : Medias in progress (add some assets, ...)
- **03-done** : Medias done and ready for test with Jellyfin

Once you have some media to test with Jellyfin, you have these command to test it :

- `make w-start-test` : Start Test Jellyfin
- `make w-stop-test` : Stop Test Jellyfin

You can access on it at this address : [Test Jellyfin](http://localhost:8097)
