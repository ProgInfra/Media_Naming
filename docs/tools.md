# Media Naming : Tools

![Icon](../icon.png)

## Table Of Contents

- [Media Naming : Tools](#media-naming--tools)
  - [Table Of Contents](#table-of-contents)
  - [Naming Sources](#naming-sources)
  - [Renamer Tools](#renamer-tools)
  - [Metadata Website](#metadata-website)
  - [Wallpaper](#wallpaper)
  - [Video Extractor : Image](#video-extractor--image)
  - [Video Extractor : Clip](#video-extractor--clip)
  - [Automatic Extractor](#automatic-extractor)

## Naming Sources

- [Jellyfin Media Movies](https://jellyfin.org/docs/general/server/media/movies.html)
- [Plex Naming](https://support.plex.tv/articles/naming-and-organizing-your-tv-show-files/)

## Renamer Tools

- **Linux** : [Thunar](https://docs.xfce.org/xfce/thunar/start)
- **Windows** : [Ant Renamer](https://antp.be/software/renamer)
- [TV Rename](https://www.tvrename.com/)

## Metadata Website

- [IMDB](https://www.imdb.com/)
- [TMDB](https://www.themoviedb.org/)
- [TVDB](https://thetvdb.com/)

## Wallpaper

- [WallpaperFlare](https://www.wallpaperflare.com/)
- [Alphacoders](https://alphacoders.com/)

Mass Download : (with FireFox)

1) Go to [Alphacoders](https://alphacoders.com/) and search
2) Scroll the page all you want
3) Download the HTML page with all data
4) Sort full images and get it

## Video Extractor : Image

Cut at `time` :

```bash
ffmpeg -ss [time] -i video.mp4 -frames:v 1 screenshot.png
```

You can use : Time for start and end : `ffmpeg -ss "00:02:43.500" -i video.mp4 -frames:v 1 screenshot.png`

## Video Extractor : Clip

Cut from `start` for `duration` :

```bash
ffmpeg -ss [start] -i video.mp4 -t [duration] -map 0 -c copy clip.mp4
```

Cut from `start` to `stop` :

```bash
ffmpeg -copyts -ss [start] -i video.mp4 -to [stop] -map 0 -c copy clip.mp4
```

You can use :

- Duration in seconds for start, duration and stop : `ffmpeg -ss 5 -i video.mp4 -t 30 -map 0 -c copy clip.mp4`
- Time for start and stop : `ffmpeg -copyts -ss "00:00:10.000" -i video.mp4 -to "00:01:45.000" -map 0 -c copy clip.mp4`

## Automatic Extractor

We have create in naming a command to automatically extract screenshot and clip from a file that regroup all of these :

- **screenshots** : List of screenshot to take
  - **file** : Filename of the video (**ex** : "video_s01_e01.mp4")
  - **time** : Time to take the screenshot (**ex** : "00:02:43.500")
  - **name (OPTIONAL)** : Custom Name (**ex** : "fly")
- **clips** : List of clips to extract
  - **file** : Filename of the video (**ex** : "video_s01_e01.mp4")
  - **start** : Start time of the clip (**ex** : "00:00:10.000" or 30 for 30 seconds)
  - **stop** : Stop time of the clip (**ex** : "00:01:45.000")
  - **duration (OPTIONAL)** : Duration from the start time (**ex** : 30 for 30 seconds) (need of stop or duration)
  - **name (OPTIONAL)** : Custom Name (**ex** : "fight")
- **backdrops** : List of opening or ending to extract and converted to mp3
  - **name** : Backdrops Name (**ex** : "op" for opening or "ed" ending)
  - **file** : Filename of the video (**ex** : "video_s01_e01.mp4")
  - **start** : Start time of the clip (**ex** : "00:00:10.000" or 30 for 30 seconds)
  - **stop** : Stop time of the clip (**ex** : "00:01:45.000")
  - **duration (OPTIONAL)** : Duration from the start time (**ex** : 30 for 30 seconds) (need of stop or duration)

Example :

```json
{
  "screenshots": [
    { "file": "video_s01_e01.mp4", "time": "00:02:43.500" },
    { "file": "video_s01_e01.mp4", "time": "00:18:00.000" }
  ],
  "clips": [
    { "file": "video_s01_e01.mp4", "start": "00:00:10.000", "stop": "00:01:45.000" },
    { "file": "video_s01_e01.mp4", "start": 5, "duration": 30 }
  ],
  "backdrops": [
    { "name": "op", "file": "video_s01_e01.mp4", "start": 1, "duration": 90 },
    { "name": "ed", "file": "video_s01_e01.mp4", "start": "00:00:10.000", "stop": "00:01:45.000" }
  ]
}
```

```yaml
screenshots:
- file: "video_s01_e01.mp4"
  time: "00:02:43.500"
- file: "video_s01_e01.mp4"
  time: "00:18:00.000"

clips:
- file: "video_s01_e01.mp4"
  start: "00:00:10.000"
  stop: "00:01:45.000"
- file: "video_s01_e01.mp4"
  start: 5
  duration: 30

backdrops:
- name: "op"
  file: "video_s01_e01.mp4"
  start: "00:00:10.000"
  stop: "00:01:45.000"
- name: "ed"
  file: "video_s01_e01.mp4"
  start: 5
  duration: 30
```

Save it to file : `extract.json` or `extract.yml` or `extract.yaml`

Next you can run this command in the media folder where the extract file is : `naming media extract`
