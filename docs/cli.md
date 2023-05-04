# `naming`

**Usage**:

```console
$ naming [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `init`: Create basics folders for your main...
* `media`

## `naming init`

Create basics folders for your main operating system

**Usage**:

```console
$ naming init [OPTIONS]
```

**Options**:

* `-o, --output-folder TEXT`: [default: .]
* `--admin / --no-admin`: [default: admin]
* `--project / --no-project`: [default: project]
* `--server / --no-server`: [default: server]
* `--sys / --no-sys`: [default: sys]
* `--linux / --no-linux`: [default: linux]
* `--windows / --no-windows`: [default: windows]
* `--help`: Show this message and exit.

## `naming media`

**Usage**:

```console
$ naming media [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `book`: Add folders to store a book
* `game`: Add folders to store a game
* `image`: Add folders to store some images
* `init`: Create folders for your media storage
* `movie`: Add folders to store a movie
* `music`: Add folders to store some musics
* `serie`: Add folders to store a serie

### `naming media book`

Add folders to store a book

**Usage**:

```console
$ naming media book [OPTIONS] NAME
```

**Arguments**:

* `NAME`: [required]

**Options**:

* `-m, --media-folder TEXT`: [default: .]
* `-t, --type [audiobook|book|comic|manga|manhwa|manhua|webtoon]`: [default: book]
* `-an, --author-name TEXT`
* `--help`: Show this message and exit.

### `naming media game`

Add folders to store a game

**Usage**:

```console
$ naming media game [OPTIONS] NAME
```

**Arguments**:

* `NAME`: [required]

**Options**:

* `-m, --media-folder TEXT`: [default: .]
* `--image / --no-image`: [default: image]
* `--package / --no-package`: [default: package]
* `--patch / --no-patch`: [default: patch]
* `--mod / --no-mod`: [default: mod]
* `--wallpaper / --no-wallpaper`: [default: wallpaper]
* `--screenshot / --no-screenshot`: [default: screenshot]
* `--save / --no-save`: [default: save]
* `--todo / --no-todo`: [default: todo]
* `--help`: Show this message and exit.

### `naming media image`

Add folders to store some images

**Usage**:

```console
$ naming media image [OPTIONS] NAME
```

**Arguments**:

* `NAME`: [required]

**Options**:

* `-m, --media-folder TEXT`: [default: .]
* `-t, --type [screenshot|wallpaper|photo]`: [default: photo]
* `--help`: Show this message and exit.

### `naming media init`

Create folders for your media storage

**Usage**:

```console
$ naming media init [OPTIONS]
```

**Options**:

* `-o, --output-folder TEXT`: [default: ./medias]
* `--game / --no-game`: [default: game]
* `--image / --no-image`: [default: image]
* `--book / --no-book`: [default: book]
* `--music / --no-music`: [default: music]
* `--video / --no-video`: [default: video]
* `--help`: Show this message and exit.

### `naming media movie`

Add folders to store a movie

**Usage**:

```console
$ naming media movie [OPTIONS] NAME
```

**Arguments**:

* `NAME`: [required]

**Options**:

* `-m, --media-folder TEXT`: [default: .]
* `-y, --year INTEGER`: [default: 2023]
* `-db, --db-type [imdb|tvdb|tmdb]`: [default: imdb]
* `-id, --db-id TEXT`
* `--extrafanart / --no-extrafanart`: [default: extrafanart]
* `--screenshot / --no-screenshot`: [default: screenshot]
* `--clip / --no-clip`: [default: clip]
* `--todo / --no-todo`: [default: todo]
* `--help`: Show this message and exit.

### `naming media music`

Add folders to store some musics

**Usage**:

```console
$ naming media music [OPTIONS] NAME
```

**Arguments**:

* `NAME`: [required]

**Options**:

* `-m, --media-folder TEXT`: [default: .]
* `-an, --artist-name TEXT`
* `--help`: Show this message and exit.

### `naming media serie`

Add folders to store a serie

**Usage**:

```console
$ naming media serie [OPTIONS] NAME
```

**Arguments**:

* `NAME`: [required]

**Options**:

* `-m, --media-folder TEXT`: [default: .]
* `-t, --type [serie|anime]`: [default: serie]
* `-db, --db-type [imdb|tvdb|tmdb]`: [default: imdb]
* `-id, --db-id TEXT`
* `-ns, --nb-season INTEGER`: [default: 0]
* `--wallpaper / --no-wallpaper`: [default: wallpaper]
* `--screenshot / --no-screenshot`: [default: screenshot]
* `--backdrop / --no-backdrop`: [default: backdrop]
* `--ost / --no-ost`: [default: ost]
* `--clip / --no-clip`: [default: clip]
* `--extra / --no-extra`: [default: extra]
* `--todo / --no-todo`: [default: todo]
* `--help`: Show this message and exit.
