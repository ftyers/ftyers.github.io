vim: tw=70
SPDX-License-Identifier: (CC-BY-SA-4.0 OR GFDL-1.3-or-later)
Copyright 2018 Nick Howell

Introduction
==========

These rough notes are designed to help you get a working set of unix
tools and become familiar with them. If you already run GNU/Linux, you
can skip to the next section.


1. GNU / BSD

Modern GNU (most Linux distributions) tools all have good unicode
support. BSD?

You can install the vm too, if you like linux-inside-linux; install
virtualbox.

2. Macintosh

Apple ships tools, but they are not reasonable. Install homebrew by
navigating to https://brew.sh and following their instructions. We
will use the "brew" command to install modern tools.

$ brew install gnu-sed icu4c # what others?
$ echo 'export PATH=$PATH:/usr/local/opt/icu4c/bin' >> ~/.bash_profile
(discuss path?)

Or install the vm. Visit https://www.virtualbox.org

3. Windows

Who knows, install the vm. Visit https://www.virtualbox.org

Get Started
===========

Follow the unicode adaptation of Unix for Poets:

https://ftyers.github.io/079-osnov-programm/classes/01.html


Appendix
===========

Old computers consisted of rooms filled with equipment. You interacted
with them by typing on (what is essentially) a typewriter connected to
a phoneline. The computers response would be printed after your
command. The connection was very slow, so you would not be able to
transfer much data. It was important that commands and responses were
brief.

This is still the most efficient way to perform many tasks on the
computer; unfortunately many modern computers do not give you access
to such interfaces, and use of these interfaces is limited to a small
community, even amongst computer specialists.

We will learn how to gain access to and use these interfaces in the
context of natural language processing. If we do our job correctly,
you will begin to hate mice, media, and javascript. (Probably we won't
do our job correctly.)

0. What is a terminal

A terminal (more properly, "teletype emulator") is a piece of software
which emulates the telephone-typewriter. It runs a program, called a
"shell"; you type commands into the shell, and the shell executes them
and displays their results.

1. Getting Help
If you want to learn more about a command, you have a few options:

$ man $command

$ $command --help

2. Matching Text

Regex - basic, extended, perl, other

$ man 3 regex
$ man 7 regex
$ man grep
$ man pcrepattern



