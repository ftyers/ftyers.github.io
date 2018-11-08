<!--
vim: tw=70
SPDX-License-Identifier: (CC-BY-SA-4.0 OR GFDL-1.3-or-later)
Copyright 2018 Nick Howell
-->

# Intro to `git` from an NLP perspective

### <a name="Abstract">Abstract</a>
[#Abstract]: #Abstract

We will introduce the version control system (VCS) `git` with an
emphasis on connections to techniques in natural language programming.
A brief overview of the motivation and history of revision control,
followed by a description of the data model of `git`, and finally a
casual overview of the workflow of git. As appendix, we include a
number of interesting technologies developed on top of `git`.

<div style="column-width:30em">

## <a name="Introduction">Introduction</a>
[#Introduction]: #Introduction

Most human endeavors involve the drafting and revision of materials.
With the use of networked computers, collaboration and revision become
easier and more fruitful: authors can revert undesired changes, keep
parallel tracks of the same document developing in different ways,
review and incorporate changes from others, and publish their works to
a broad audience.

Storing and processing this data is essentially a solved problem, from
the perspective of the computer. The ongoing struggle is in presenting
human-usable interfaces to manage the histor(y|ies) of the documents.
Software intending to assist users in this management are called
"version control systems."

The first version control systems involved a central server which
stored hierarchical histories for each file in a project. Modern
revision control systems are completely distributed, allowing users to
compare and merge changes from disparate sources, and have tooling
built over them for review, feedback, quality control, and much more.

**Exercise:** Who is interested in such systems? Describe some
professions that might have interests in revision control systems
beyond programmers. What are some challenges you can imagine in
supporting such workers? (For example, suppose you have several
artists collaborating; how can version control be performed? What does
it mean to merge two different sets of changes?)

## <a name="Data models">Data models for document histories</a>
[#Data models]: #Data%20models

If we wish to track the history of a document (or collection of
documents), we should have some idea of what the data model for such a
thing looks like.

### <a name="Unified diff">Unified diff</a>
[#Unified diff]: #Unified%20diff

First we describe a data format for describing changes to a single
document. The UNIX program `diff` compares two files and outputs a
series of line-wise operations to change the first file into the
second. The output, also called a `diff` or a `patch`, consists of
a series of hunks, or portions of the document which was changed.
Each hunk contains a header describing the initial and final numbers
of line ranges, after which follow three types of lines:
* context lines, preceded with a ' ' character,
* insertion lines, preceded with a '+' character, and
* deletion lines, preceded with a '-' character.

#### Example:

```bash
$ diff -u <(echo a; echo c) <(echo b; echo c)
--- /dev/fd/63	2018-11-05 18:24:31.820054553 +0300
+++ /dev/fd/62	2018-11-05 18:24:31.820054553 +0300
@@ -1,2 +1,2 @@
-a
+b
 c

```

The first line is the command executed: to compute a patch from the
file "a\\nc" to the file "b\\nc".
```bash
$ diff -u <(echo a; echo c) <(echo b; echo c)
```

Lines 2 and 3 are the patch header, describing the names and
last-modified time of the two files. 
```patch
--- /dev/fd/63	2018-11-05 18:24:31.820054553 +0300
+++ /dev/fd/62	2018-11-05 18:24:31.820054553 +0300
```

Line 4 starts the first (and only) hunk, explaining that the hunk
covers a range of lines 1..(1+2) in the first file and 1..(1+2) in the
second file.
```patch
@@ -1,2 +1,2 @@
```

Lines 5-7 are the contents of the hunk: the line `a` is deleted, the
line `b` inserted, and the line `c` is preserved.

**Exercise:** using the Levenshtein distance algorithm, implement a
unified diff program in Python.

### <a name="Linear history">Linear history: sequence of modification</a>
[#Linear history]: #Linear%20history

Suppose that we are writing a document, and are making revisions. The
typical editorial process involves writing a draft and making some
changes; the process repeats several times. We can visualize this as
a directed graph:

```
(A) → (B) → (C) → ⋯ → (final)
```

Each vertex in the graph is a version of the document. Each arrow is
represented as a diff between the current version and the previous.
Using just the original version (which could be empty!) and an ordered
collection of diffs, we can reconstruct the final document. The UNIX
program `patch` can read and apply the changes described in a unified
diff.

A simple version control system then would store at each stage a diff
from the previous stage.

**Exercise:** Implement the described version control system in
Python. Your implementation should support entire projects, not just
single files.

**Exercise:** How would you handle non-text documents? Suppose you are
writing music, drawing a painting, mixing and resampling music. How
can you track changes to this?

### <a name="Branching histories">Branching histories: trees of modification</a>
[#Branching histories]: #Branching%20histories

When working on a document, you might come up with several different
ideas for developing it. If you don't know which one will turn out
best, you might try both independently. This is called "forking" or
"branching," and is common in software development.

```
    (B) → (C) → (D)
   ↗
(A)
   ↘
    (В) → (Г)

```

Now we cannot simply assign consecutive integer numbers; the two
branches are different lengths, and aren't comparable to each-other.
RCS (the original version control system) solves this by assigning
each branch a major number and the version is the minor number:

```
    (1.2) → (1.3) → (1.4)
   ↗
(1)
   ↘
    (2.2) → (2.3)

```

However, if you share your document with several people, and they all
make different branches, a different persons `2.3` might not be the
same as *your* `2.3`.

### <a name="Hashes">Hashes</a>
[#Hashes]: #Hashes

A solution is *hash functions*. A hash function is a way to associate
a number (the "hash") to data, in a way that it is extremely unlikely
that you will be able to find two blocks of data with the same hash
(called a "collision"). The process of applying the hash function is
called "hashing."

Some popular hash algorithms are:
* md5
* sha1
* sha2 / sha3
* blake2

Some hash algorithms are used for cryptography, and need to have
certain mathematics justifying important properties (e.g.,
unlikelihood of finding collisions, lack of correlation between data
and its hash, and others). For our purposes, we want our hash to not
have collisions, but cryptographic strength is not important.

You can experiment with hashes on Linux or other UNIX-like systems.
Typically hashes are displayed not as decimal numbers, but rather as
hexadecimal, using digits 0-9a-f.
```bash
$ echo hi > testfile; echo hi2 > testfile2

$ md5sum testfile testfile2
764efa883dda1e11db47671c4a3bbd9e  testfile
4da1c6449a2a34a338e56d6718838016  testfile2

$ sha1sum testfile testfile2
55ca6286e3e4f4fba5d0448333fa99fc5a404a73  testfile
906faceaf874dd64e81de0048f36f4bab0f1f171  testfile2

$ sha512sum testfile testfile2 # sha2, hash size is 512bit
d78abb0542736865f94704521609c230dac03a2f369d043ac212d6933b91410e06399e37f9c5cc88436a31737330c1c8eccb2c2f9f374d62f716432a32d50fac
testfile
d1fde846964c462fe3686eb0c2bed0ab1c66feb77bd06a8f6aefdca90c04036b8c8bdd8ee65567ea2f4d30714f4343d0151a13b9937473d526f3cda5d5413023
testfile2

$ b2sum testfile testfile2 # blake2
7ea59e7a000ec003846b6607dfd5f9217b681dc1a81b0789b464c3995105d93083f7f0a86fca01a1bed27e9f9303ae58d01746e3b20443480bea56198e65bfc5
testfile
768d17d444de521eb82f9c45cf0d6384c87f18ea67e164c7a832e24ab47483be0c006fc8ab806694e670f4df306468c5f30f6a987f7f8ba02c011ba641db3a7b
testfile2

```
Notice that hashes are completely changed even though the file
contents are nearly the same.

### <a name="Commit ids">Commit ids: Hashes as commit identifiers</a>
[#Commit ids]: #Commit%20ids

Instead of version numbers, `git` uses hashes. The hash itself is
typically referred to as the "commit id," "commit hash," or sometimes
just the "hash".

In order to generate a new commit id, `git` performs a hash of a bit
of data, including the previous commit id, some additional metadata
(author, time, a message describing the changes, and others), and the
changes themselves in unified diff format.

A simplified picture of a linear `git` history might look like:
```
da39a3ee5e6b4b0d3255bfef95601890afd80709
                   ↓
e6c26cce733885d31af746add898954191598ba2
                   ↓
fbb6bab8ddee30e0114cb362111ebab964ace13d
```

The first hash, `da39a3ee5e6b4b0d3255bfef95601890afd80709`, is the
hash of an empty data block (created with `sha1sum </dev/null`).

The second hash is formed by hashing the first commit id and a diff
creating `testfile`:
```
da39a3ee5e6b4b0d3255bfef95601890afd80709
--- /dev/null	2018-11-04 10:45:53.800000232 +0300
+++ testfile	2018-11-05 21:01:33.870059045 +0300
@@ -0,0 +1 @@
+hi
```

The third hash is formed by hashing the second commit id and a diff
creating `testfile2`:
```
e6c26cce733885d31af746add898954191598ba2
--- /dev/null	2018-11-04 10:45:53.800000232 +0300
+++ testfile2	2018-11-05 21:03:38.140059105 +0300
@@ -0,0 +1 @@
+hi2
```

**Exercise:** Change your version control system to store
previous-commit-id with the diff as described above.

**Exercise:** Write a tool to migrate projects from your old format to
your new format. 

**Exercise:** Write export and import commands which print and read a
sequence of commits (where commit = prev commit id + patch). The
sequence is called a "changeset."

**Exercise:** Find someone else who has completed the previous
exercises, and exchange changesets with them, creating and updating
branches. What are some good transport methods? E-mail attachment?
Posting on social media? E-mail inline?

### <a name="Merging histories">Merging histories: directed acyclic graphs of modifications</a>
[#Merging histories]: #Merging%20histories

After working on several different branches (possibly with several
people), you may eventually wish to merge several of these branches.

```
    (B) → (C) → (D)
   ↗             
(A)               ↘
   ↘               
    (В) → (Г)   → *(Е)

```

Since the two branches have different histories, some logic is
necessary to merge the changesets. There are two classes of problems
which can be encountered: a hunk from (D) might not apply to (Г) because
* the lines it was supposed to change have moved
* the lines it was supposed to change have changed

The first problem can be resolved automatically through the use of
*context* lines. If the original text from a hunk is not found in (Г),
the `patch` program (or whatever diff application implementation you
are using) can scan backwards and forwards until it finds the context
lines.

The second problem is *not* so easily solved. The idea is that if two
people together made different changes, only one of these people can
decide how to incorporate the changes made by the other. If they make
different choices, you may end up with two different merges:

```
    (B) → (C) → (D) → *(E)
   ↗                 
(A)                 ⤨
   ↘                 
    (В)    →    (Г) → *(Д)

```

There are several popular algorithms designed to help users
efficiently resolve merges automatically or manually; see the [Merge
(version control) article on Wikipedia] for more.

[Merge (version control) article on Wikipedia]: https://en.wikipedia.org/wiki/Merge_(version_control)

### <a name="Directed acyclic graphs">Directed acyclic graphs</a>
[#Directed acyclic graphs]: #Directed%20acyclic%20graphs

We now have the ingredients we need to describe the datamodel of
`git`.

Recall that a graph is a diagram of vertices and edges; a graph is
called "directed" if each edge is given a direction, and "directed
acyclic" if no path which follows the arrows can create a loop (also
known as a "cycle").

Without merging, our commit sequences formed a directed tree: the
starting point is the initial commit, and branches are created
whenever two different changesets are made from the same commit, as
before in the section [#Branching histories].

Now that we have merges, it is possible for non-direction-respecting
cycles to form in our modification graphs; however, since it is
impossible for a future change to be the base for an earlier change,
these cycles can never be direction-respecting. This is why the term
"directed acyclic" must be used, instead of purely "acyclic."

**Exercise:** Write or read a short fiction story about time-travel,
and diagram the interactions of the characters using a directed graph:
vertices are events, edges are actions or causes. Can you form a
cycle? A directed cycle?

**Hard Exercise:** Repeat for [Primer].

[Primer]: https://en.wikipedia.org/wiki/Primer_(film)

## The `git` version control system

We are now ready to actually tackle the use of `git`. This software
has many features we will not describe here, but we'll give the basic
workflow and describe the data model you should have in your head
when running `git` commands.

### Working tree, staging area, HEAD

There are three layers of file data when working with `git`: the
working tree, the staging area, and HEAD (the tip of the current
branch of history).

The working tree is the highest level; this is where your files
actually appear. It is the only layer which you interact with as files
and folders.You can edit them in whatever way you are used to.

The staging area is the next level; it is a tentative commit. Changes
you have made in the working tree can be added to the staging area,
either file-wise, or line-wise if you want to only commit some of the
changes you have made.

The history is the lowest level of git; once something is in the
history, only the seldom-used history rewriting tools can alter it.
The tip of the current branch of history you are working on is always
referred to as HEAD; HEAD is advanced when you commit from the staging
area.

```
                editeditedit
             |---------------|
             |   work tree   |
git add/rm ↓ |---------------| ↑ git reset / checkout
             |    staging    |
git commit ↓ |---------------| ↑ git reset / checkout
             |     HEAD      |
             |---------------|

```

Let's walk through creating the history from [#Commit ids]. 

```
# create the directory, enter it
$ mkdir test; cd test

# initialize the repository
$ git init
Initialized empty Git repository in /home/nlhowell/test/.git/

# create our first file
$ echo hi > testfile

# see repository status
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	testfile

nothing added to commit but untracked files present (use "git add" to
track)


# add the testfile to staging
$ git add testfile

# see repository status
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   testfile



# make commit
$ git commit -m "message describing first commit"
[master (root-commit) e8d7309] message describing first commit
 1 file changed, 1 insertion(+)
 create mode 100644 testfile

```

Now we've created our first commit, whose commit id starts with
`e8d7309`. The diagram of our history is

```
(e8d7309)
HEAD, master
```

The label "HEAD" means that this is the tip of our repository; new
commits will extend from e8d7309. The label "master" is used to
describe a named branch. Your can change the name of the branch using
`git branch` or `git checkout -b`.

Let's make our next commit:
```
# create the next file
$ echo hi2 > testfile2
$ git add testfile2
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   testfile2

$ git commit -m "we added another file"
[master 34a7695] we added another file
 1 file changed, 1 insertion(+)
 create mode 100644 testfile2

```

Here's our new repository state:
```
(e8d7309) → (34a7695)
            HEAD
	    master
```

You can view a of list of commits using `git log`, or show the diff
for a commit using `git show`.

To go back to a previous commit, you can use `git reset` (to change HEAD and
staging; the work tree is unchanged) or `git checkout` (to change HEAD,
staging, and the work tree).

Let's go back to our first commit:
```
$ git checkout e8d7309
Note: checking out 'e8d7309'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

  git checkout -b <new-branch-name>

HEAD is now at e8d7309 message describing first commit

```

Now the repository state is
```
(e8d7309) → (34a7695)
HEAD        master
```

We can make a new commit, say by deleting our remaining file:
```
# remove in work tree and staging
$ git rm testfile
$ git status
HEAD detached at e8d7309
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	deleted:    testfile

$ git commit -m "removed that nasty testfile"
[detached HEAD e72d2e1] removed that nasty testfile
 1 file changed, 1 deletion(-)
 delete mode 100644 testfile
```

Now our repository state is:
```
(e8d7309) → (34a7695)
            master
          ↘
	    (e72d2e1)
	    HEAD
```



### (Named) branches and tags

In `git`, named branches are just called "branches." A named branch is
a label applied to a commit which tracks the tip as more commits are
made. A named branch is created by calling `git checkout -b
<branchname>`.

Some named branches are created automatically by `git`:
* `master` is created when you make your first commit
* `origin/*` branches are created when you clone someone else's
  repository; when you run `git fetch` to download changes, these
  branches will update to reflect the branches of the remote
  repository

A tag is simply a label which does not follow future commits. You can
create a tag using `git tag <tagname>`.

Tags and named branches can be used instead of commit ids in most
`git` commands. In particular, `git` reserves the right to delete any
commits which don't lead to either a tag or a named branch; this is
used to prune history which isn't used any more.

#### Example:
```
$ mkdir test; cd test; git init test
$ echo hi > testfile; git add testfile; git commit -m "first file"
[master (root-commit) c901142] first file
 1 file changed, 1 insertion(+)
 create mode 100644 testfile

# display current branch
$ git branch
* master

# create tag
$ git tag this-is-my-first-tag

# show tags and branches
$ git log --decorate --oneline
c901142 (HEAD -> master, tag: this-is-my-first-tag) first file

$ echo hi2 > testfile2; git add testfile2; git commit -m "second file"
[master e564b17] second file
 1 file changed, 1 insertion(+)
 create mode 100644 testfile2

# branch name followed the commit, but the tag stayed
$ git log --decorate --oneline
e564b17 (HEAD -> master) second file
c901142 (tag: this-is-my-first-tag) first file

```

Notice that master tracked the second commit, while the tag stayed
with the first commit. Here's the final repository state:

```
(c901142)                   → (e564b17)
tag:this-is-my-first-tag      HEAD, master
```

Branches are typically used for feature or topic development, while
tags are used for version releases.

## Appendix

There are many features of `git` we haven't discussed. Here's a brief
overview of many of them.

### Merging

To merge a commit, branch, or tag `X` into `HEAD`, simply run `git
merge X`. If `X` was a named branch, after merging you can delete it
with `git branch -d <name>`.

If there are conflicts which require human intervention, you will be
notified with a message. You can abort the attempted merge with `git
merge --abort`, or after resolving the conflicts you may continue with
`git merge --continue`.

### Reworking

If you don't like the way your history looks, you can use the tool
`git rebase` to alter it. See the manual page (`man git-rebase`) for
more information.

For more aggressive or thorough rewriting of history, you can use `git
filter-branch`.

### Sending and receiving changesets

As with the exercise in [#Commit ids], you can transfer changesets in
many ways with `git`.

* `git format-patch` and `git am` export and import changesets,
  respectively
* `git send-email` can be used to send changesets by e-mail
* `git fetch` can be used to fetch changes from a remote repository
  ([#Remote repositories] for more info)
* `git pull` and `git push` can be used to merge changes from and to
  remote repositories
* `git request-pull` can generate requests to pull from remote
  repositories

### <a name="Remote repositories">Remote repositories</a>
[#Remote repositories]: #Remote%20repositories

There are a variety of ways to handle remote repositories; most are
connected to over `ssh` or `https`, but `git` has a plugin
architecture for remote transports. Some other interesting remote
transports:
* `git-remote-gcrypt` encrypts its contents
* `git-remote-ssb` uses the SecureScuttleButt decentralized
  communication platform
* `git-remote-ipfs` uses the InterPlantary FileSystem decentralized
  communication platform

### Dealing with non-text files

There are many times when text source isn't available for the files
you are working with. Since `git` is not designed for handling binary
data, many operations will be inefficient. There are some tools which
work with `git` to assist managing binary files without keeping them
in the commit history graph:
* [`git-annex`](https://git-annex.branchable.com) (personal favorite)
* `git` Large File Support

### Review/workflow tools

There are many code review tools which can be used provide feedback to
hopeful contributors. If they suggest you merge a branch that you
don't think is ready, you can provide feedback to them. These tools
assist in understanding the feedback and changes that have been made
to the suggested merge.
* [`git-series`](https://github.com/git-series/git-series) (personal favorite)
* Patchwork
* Gerrit
* GitHub

</div>

