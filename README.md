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

- install dependencies using [pipenv](https://github.com/pypa/pipenv)

```bash
$ pipenv install
```

- get a [Google calendar credentials](https://developers.google.com/calendar/quickstart/python?authuser=3) and put the `credentials.json` on the `root` folder
- run the `main.py` file

