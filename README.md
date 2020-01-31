# Voice Assistant

A python voice assistant to help your life

* [Voice Assistant](#voice-assistant)
* [What it can do](#what-it-can-do)
  * [Calendar Integration](#calendar-integration)
  * [Google search](#google-search-integration)
* [Setup](#setup)

# What it can do

This voice assistant was design to help on a developer day to day life. Is important to notice this is an early version, and new features will be add in the future

## Calendar integration

The voice assistant can check for events on your main Google calendar account for a specific date

### commands

You can trigger this feature by saying something like

- **do i have plans on saturday?**

- **what do i have for today?**

- **am i busy on october 27th?**

## Google search integration

It is also possible to ask for a Google search about some topic, this feature will open your default browser and do the search

### commands

You can trigger this feature by saying something like

- **search for python**

- **can you search for snake**

# Setup

**IMPORTANT: this was only tested on linux so far**

- linux packages needed:

```bash
$ sudo apt install libdbus-1-dev libdbus-glib-1-dev build-essential swig git libpulse-dev libasound2-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg espeak mbrola  mbrola-br1  mbrola-en1 pkg-config libcairo2-dev gcc python3-dev libgirepository1.0-dev python-gst-1.0 gstreamer1.0-plugins-good gstreamer1.0-plugins-ugly gstreamer1.0-tools
```

- install python dependencies using [pipenv](https://github.com/pypa/pipenv)

```bash
$ pipenv install
```

- get a [Google calendar credentials](https://developers.google.com/calendar) and put the `credentials.json` on the `root` folder
- run the `main.py` file

