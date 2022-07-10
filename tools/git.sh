#!/bin/bash


# Git Setup Multiple Repository
git remote add gitlab git@gitlab.com:proginfra/media_naming.git
git remote set-url --add --push origin git@gitlab.com:proginfra/media_naming.git

git remote add github git@github.com:ProgInfra/Media_Naming.git
git remote set-url --add --push origin git@github.com:ProgInfra/Media_Naming.git


# Display Config
git remote show origin

git config --list
