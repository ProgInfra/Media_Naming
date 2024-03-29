# Media Naming : Video Naming

![Icon](../icon.png)

## Table Of Contents

- [Media Naming : Video Naming](#media-naming--video-naming)
  - [Table Of Contents](#table-of-contents)
  - [Videos Type](#videos-type)
  - [Movies Folders](#movies-folders)
    - [Movies Naming Rules](#movies-naming-rules)
    - [Movies Protocol](#movies-protocol)
  - [Series and Animes Folders](#series-and-animes-folders)
    - [Series and Animes Naming Rules](#series-and-animes-naming-rules)
    - [Series and Animes Protocol](#series-and-animes-protocol)
  - [Divers](#divers)

## Videos Type

There are differents videos **type** :

- **Movies**
- **Series**
- **Animes**
- **Divers** : Any other videos

## Movies Folders

We use this documentation to organize our movies : [Jellyfin documentation](https://jellyfin.org/docs/general/server/media/movies)

- **movies** :
  - movie_name (YYYY) - [1080p].mp4
  - movie_name (2022) [imdbid-tt0371746] - [1080p].mp4
  - **movie_name (2023) [imdbid-tt0371746]** :
    - movie_name (2023) [imdbid-tt0371746] - [1080p].mp4
    - movie_name (2023) [imdbid-tt0371746] - [720p].mp4
    - movie_name (2023) [imdbid-tt0371746] - [720p].mp4
    - cover.png
    - banner.png
    - **clips** :
      - movie_name_001-clip.mp4
    - **extrafanart** :
      - movie_name_fanart_001.png
    - **screenshots** :
      - movie_name_screenshot_YYYY-MM-DD_HH-MM-SS.png
      - movie_name_screenshot_2022-11-31_18-54-30.png

### Movies Naming Rules

- Always **lowercase** (**NOT** Iron Man **BUT** iron man)
- Replace of **space** by **underline** (**NOT** iron man **BUT** iron_man)
- **Video definition** : 2160p, 1080p, 720p, 480p, 360p.
- **Formatted Date** : **YYYY-MM-DD** (Year-Month-Day = 2022-11-31)
- **Formatted Time** : **HH-MM-SS** (Hour-Minute-Second = 18-54-30)
- **Formatted DateTime** : **YYYY-MM-DD_HH-MM-SS** (Year-Month-Day_Hour-Minute-Second = 2022-11-31_18-54-30)
- **Metadata ID** :
  - [IMDB (for movies and series)](https://www.imdb.com) : [imdbid-tt0371746]
  - [TMDB (for movies)](https://www.themoviedb.org/) : [tmdbid-413594]

### Movies Protocol

1) Get movie with best quality and rename it with [movies naming rules](#movies-naming-rules)
2) Add some clips if you have some, you can use the [tools](./tools.md) to extract a screenshot or a part of a video and rename it
3) Find extrafanart, rename it and convert these to PNG
4) Add some screenshot if you have some
5) Get cover and banner and convert it to PNG

## Series and Animes Folders

We use this documentation to organize our series : [Jellyfin documentation](https://jellyfin.org/docs/general/server/media/shows/)

- **series / animes** :
  - **serie_name [imdbid-tt2250192]** :
    - **season_01** :
      - serie_name_s01e01.mkv
      - serie_name_s01e02-e03.mp4
      - serie_name_s01e04.mp4
      - cover.png
      - banner.png
      - **clips** :
        - serie_name_001-clip.mp4
      - **extras** :
        - serie_name_e01-extra.mp4
      - **wallpapers** :
        - serie_name_wallpaper_001.png
      - **screenshots** :
        - serie_name_screenshot_YYYY-MM-DD_HH-MM-SS.png
        - serie_name_screenshot_2022-11-31_18-54-30.png
      - **backdrops** :
        - opening_01.mp4
      - **theme-music** : OST
        - 01 - song_name.mp3

### Series and Animes Naming Rules

- Always **lowercase** (**NOT** Sword Art Online **BUT** sword art online)
- Replace of **space** by **underline** (**NOT** sword art online **BUT** sword_art_online)
- Multiple **zero digit** before number (**NOT** sword_art_online_1 **BUT** sword_art_online_001)
- **Video definition** : 2160p, 1080p, 720p, 480p, 360p.
- **Formatted Date** : **YYYY-MM-DD** (Year-Month-Day = 2022-11-31)
- **Formatted Time** : **HH-MM-SS** (Hour-Minute-Second = 18-54-30)
- **Formatted DateTime** : **YYYY-MM-DD_HH-MM-SS** (Year-Month-Day_Hour-Minute-Second = 2022-11-31_18-54-30)
- **Metadata ID** :
  - [IMDB (for movies and series)](https://www.imdb.com) : [imdbid-tt0371746]
  - [TVDB (for series)](https://thetvdb.com/) : [tvdbid-259640]

### Series and Animes Protocol

1) Get serie or anime with best quality and rename it with [series and animes naming rules](#series-and-animes-naming-rules)
2) Divide it if you have multiple seasons
3) Add some clips if you have some, you can use the [tools](./tools.md) to extract a screenshot or a part of a video and rename it
4) Add some extras if you have some and rename it
5) Find wallpapers, rename these, and convert these to PNG
6) Add some screenshot if you have some
7) Extract intro for series or opening and ending for animes, you can use the [tools](./tools.md) to extract this part of a video and rename these
8) Find OST, rename these and convert these if needed
9) Get cover and banner and convert it to PNG

## Divers

For other specific **movies** or **series**, you have to use the good **naming format** is there are one unique video (movie) or a list of episode (series).
