<!--
vim: tw=70
SPDX-License-Identifier: (CC-BY-SA-4.0 OR GFDL-1.3-or-later)
Copyright 2018 Nick Howell
-->

# Introduction to Unix Terminal

<div style="column-width: 30em">

Introduction
==========

These rough notes are designed to help you get a working set of unix
tools and become familiar with them. If you already run GNU/Linux, or
have a compatible set of command-line tools, you can skip to the next
section.

1. Unix-like

   a) GNU

      Modern GNU (most Linux distributions) make it easy to install a
      friendly command-line environment. Make sure you have:
      > bash, python, git, gcc, icu


   b) BSD

      Modern BSDs might not come with good unicode-supporting
      utilities.  Make sure you have 1. a) tools for GNU systems,
      plus the following GNU tools:
      > coreutils, sed, awk

   c) Plan9

      Plan 9 distributions are few and far between; if you're running
      plan9, you probably know what you need.

2. Apple

   Apple ships tools, but out of legal fear the tools they choose are
   outdated.

   a) [homebrew][homebrew] is an unofficial Unix-style package
      manager for OS X.

      Install it, and use it to install the tools from 1. a) and 1.
      b).  Keep in mind that homebrew, in order to avoid interfering
      with Apple's tools, might install packages where they are
      inaccessible. Read carefully the messages produced by `brew
      install`.

      *Note that we cannot provide support for homebrew in this
      class.*

   b) [virtualbox][virtualbox] is a virtual machine which will
      allow you to install a copy of GNU/Linux that runs inside of
      your computer.

      Download an ISO for [Debian][debian] and use virtualbox to
      install it.

      *Note that support **will** be provided for virtualbox in this
      class.*

3. Windows

   a) Windows 10 includes a Linux virtual machine; this should
      work.

      *Note that we cannot provide support for Windows 10 Linux in
      this class.*

   b) [Cygwin][cygwin] is a Unix-compatibility layer for Windows.

      *Note that we cannot provide support for Cygwin in this
      class.*

   c) [virtualbox][virtualbox] is a virtual machine wihich will
      allow you to install a copy of GNU/Linux that runs inside of
      your computer.  Download an ISO for [Debian][debian] and use
      virtualbox to install it.

      *Note that support **will** be provided for virtualbox in this
      class.*


Get Started
===========

See the appendix for some terminology, and a brief explanation of why
a command-line environment is useful.

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

0. Glossary

   a) Terminal: a piece of software that emulates the physical
      telephone-typewriter. It runs a shell. Common terminals are "xfce
      Terminal", "urxvt", "xterm", "konsole", "GNOME Terminal", "(Apple)
      Terminal".

   b) Shell: a call-response program that runs in the terminal. The shell
      is a program that loops, prompting you to enter commands, and
      displaying their output. Common shells are "bash", "zsh".

      sample prompt:
      ```
      nlhowell@mercury ~ $ _
      ```

      Prompts typically include username, hostname (the name of the computer
      the shell is running on), the current working directory, and the
      end-of-prompt delimiter $.

      sample prompt-command-output:
      ```
      nlhowell@mercury $ echo hi
      hi
      ```

   c) Command: a program, or pipeline of programs, together with their
      arguments.

      command with program "echo" and argument "hi"
      ```
      $ echo hi
      ```

      pipeline of two subcommands: program "echo" with argument "hi", and
      program "tr" with arguments "a-z" and "A-Z"; output of "echo" command
      is fed as input to "tr" command
      ```
      $ echo hi | tr a-z A-Z
      HI
      ```

   d) Pipeline: a chain of programs (with arguments) which are hooked
      together, so that the output of a program is fed to the next program
      in the chain.

   e) Arguments: a small collection of configuration data provided to a
      program on the commandline.


1. Getting Help
   If you want to learn more about a command, you have a few options:

   ```
   $ man $command

   $ $command --help
   ```

2. Matching Text

   Regex - basic, extended, perl, other

   $ man 3 regex
   $ man 7 regex
   $ man grep
   $ man pcrepattern


[homebrew]:    https://brew.sh
[debian]:      https://debian.org
[virtualbox]:  https://virtualbox.org
[cygwin]:      https://cygwin.org

</div>
