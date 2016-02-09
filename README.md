[![Build Status](https://travis-ci.org/jherrlin/unipass.svg?branch=master)](https://travis-ci.org/jherrlin/unipass)

## UniPass

is a password manager for terminal environments.

Password entries are stored in a sqlite3 database.

AS FOR NOW THIS APPLICATION DOES NOT ENCRYPT STORED PASSWORDS!


## Requirements

* python2.7-3.5
* urwid
* click

## Usage

Show available commands

```shell
python -m unipass --help
```

Start urwid gui

```shell
python -m unipass --urwid
```

List services

```shell
python -m unipass --list
```


Add service

```shell
python -m unipass --add
```

Get service

```shell
python -m unipass --get <arg>
```

Import/export

```shell
python -m unipass --import-data <arg>
python -m unipass --export-data <arg>
```
