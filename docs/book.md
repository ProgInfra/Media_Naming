# Media Naming : Book Naming

![Icon](../icon.png)

## Table Of Contents

- [Media Naming : Book Naming](#media-naming--book-naming)
  - [Table Of Contents](#table-of-contents)
  - [Folders](#folders)
  - [Naming Rules](#naming-rules)
  - [Protocol](#protocol)

## Folders

We use this documentation to organize our books : [Jellyfin documentation](https://jellyfin.org/docs/general/server/media/books)

- **books** :
  - **audiobooks** :
    - **author_name** :
      - book_01.flac
      - book_02.flac
    - **book_name** :
      - chapter_01.flac
      - chapter_02.flac
  - **books** :
    - **author_name** :
      - **book_name** :
        - book_01.epub
        - cover.png
        - banner.png
        - metadata.opf
  - **comics** :
    - **comic_name** :
      - comic_01.cbr
      - cover.png
      - banner.png
      - metadata.xml
  - **mangas** :
    - **manga_name** :
      - manga_01.cbr
      - cover.png
      - banner.png
  - **manhwas** :
    - **manhwa_name** :
      - manhwa_01.cbr
      - cover.png
      - banner.png
  - **manhuas** :
    - **manhua_name** :
      - manhua_01.cbr
      - cover.png
      - banner.png
  - **webtoons** :
    - **webtoon_name** :
      - webtoon_01.cbr
      - cover.png
      - banner.png

## Naming Rules

- Always **lowercase** (**NOT** Cherub **BUT** cherub)
- Replace of **space** by **underline** (**NOT** sword art online **BUT** sword_art_online)
- Multiple **zero digit** before number (**NOT** sword_art_online_1 **BUT** sword_art_online_001)

## Protocol

1) Get book and rename it with [naming rules](#naming-rules)
2) Get cover and banner and convert it to PNG
