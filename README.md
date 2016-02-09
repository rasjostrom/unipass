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

{% highlight bash %}

   python -m unipass --help
   
{% endhighlight %}

Start urwid gui

{% highlight bash %}

   python -m unipass --urwid
   
{% endhighlight %}

Add service

{% highlight bash %}

   python -m unipass --add
   
{% endhighlight %}

Get service

{% highlight bash %}

   python -m unipass --get <arg>
   
{% endhighlight %}

Import/export

{% highlight bash %}

   python -m unipass --import-data <arg>
   python -m unipass --export-data <arg>
   
{% endhighlight %}


