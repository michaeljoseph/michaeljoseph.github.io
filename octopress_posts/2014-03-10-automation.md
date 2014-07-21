---
layout: post
title: "Automation"
date: 2014-03-10 12:45:08 +0200
comments: true
categories: 
---
```bash
michael@resurrection:~/Source[master]$ git clone git@github.com:yola/yoconfig.git
Cloning into 'yoconfig'...
remote: Counting objects: 112, done.
remote: Compressing objects: 100% (53/53), done.
remote: Total 112 (delta 53), reused 108 (delta 53)
Receiving objects: 100% (112/112), 13.25 KiB | 0 bytes/s, done.
Resolving deltas: 100% (53/53), done.
Checking connectivity... done.
michael@resurrection:~/Source[master]$ cp changes/.env yoconfig/
michael@resurrection:~/Source[master]$ cd yoconfig
autoenv:
autoenv: WARNING:
autoenv: This is the first time you are about to source /Users/michael/Source/yoconfig/.env:
autoenv:
autoenv:     --- (begin contents) ---------------------------------------
autoenv:     use_env "${PWD##*/}"
autoenv:     --- (end contents) -----------------------------------------
autoenv:
autoenv: Are you sure you want to allow this? (y/N) y
Create virtualenv yoconfig now? (Yn) Y
New python executable in yoconfig/bin/python
Installing setuptools, pip...done.
(yoconfig)michael@resurrection:~/Source/yoconfig[master]$ yp
Downloading/unpacking mock
  Using download cache from /Users/michael/.pip_download_cache/https%3A%2F%2Fyolapi.yola.net%2Fmedia%2Fdists%2Fmock-1.0.1.zip
```

{% img http://cdn.hitthefloor.com/wp-content/uploads/2013/09/Marvell-Music-Boom-Bam-Bing-Cover.jpg %}
