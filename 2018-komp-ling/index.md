<!--
vim: tw=70
SPDX-License-Identifier: (CC-BY-SA-4.0 OR GFDL-1.3-or-later)
Copyright 2018 Francis Tyers, Nick Howell
-->

# Компьютерная лингвистика

<div style="column-width:30em">

## Description

This course is an introduction to the pipeline approach to natural
language processing. In a pipeline approach, raw text goes through a
sequence of steps (or tasks) to process it into a form more useful for
end-user applications. The steps we will cover are sentence
segmentation, word tokenisation, morphological analysis and
disambiguation and dependency parsing. This should give you all of the
details you need in order to approach more complex tasks such as
co-reference resolution, relation extraction, etc.

## Organization

The course is organized into two tracks, known as *algorithms* (for
those comfortable with introductory NLP engineering techniques) and
*engineering* (for those unfamiliar with these techniques).
*Algorithms*-track students have the option of completing a course
project.

The *algorithms* track will study the algorithms and ideas used in
scientific research in natural language processing. Students will be
asked to use software produced as the result of scientific research,
write their own implementations of important algorithms, and compare
methodologies through a series of small projects called "practicals."

The *engineering* track will focus on the tools and techniques used in
software design, analysis, and distribution in the context of natural
language processing. The main topics of study will be Python and UNIX
environment in the context of natural language processing. The course is
completed through a serious of small projects called "practicals."

*Algorithms*-track students may propose an *optional* project in groups
or on their own. Instructors can provide suggestions for project ideas.
See the [request for project proposals][project-rfp] for more details.

## Objectives

By the end of this course, *algorithms*-track students will:
* Understand issues in segmentation and tokenisation of texts and implement
  solutions 
* Use two-level morphology to model morphological phenomena 
* Describe and use three approaches to morphological disambiguation 
* Understand the principles behind transition-based and graph-based dependency
  parsing 
* Know the steps to be able to go from raw text to dependency trees for any
  language 
  
while *engineering*-track students will:
* Be familiar with the syntax of the Python programming language
* Be able to navigate the filesystem using the UNIX shell
* Be capable of efficiently using online resources to guide their own learning
* Be able to use Python to process corpora from the web
* Be able to use Python to implement a simple NLP pipeline from scratch

## Prior experience

*Algorithms*-track students are expected to have basic proficiency with Python
and UNIX-like operating systems, and to be capable of answering simple
questions through the use of search engines, documentation, chat systems, etc.

## Practicals
  0. ### [UNIX] and [git] (both tracks)
  1. ### [Segmentation & Tokenization] (both tracks)
  2. ### [Finite-state Morphology] / [Transliteration]
  3. ### [Morphological disambiguation] / [Unigram model]
  4. ### [Dependency parsing] / [Unigram part-of-speech tagger]

See [submission guidelines].

[submission guidelines]:         submission.html


[UNIX]:                          practicals/unix.html
[git]:                           appendix/git.html
[Segmentation & Tokenization]:   practicals/segmentation.html
[Finite-state Morphology]:       ../2017-КЛ_МКЛ/hfst.html
[Transliteration]:               ../079-osnov-programm/classes/04_1.html
[Morphological disambiguation]:  ../2017-КЛ_МКЛ/practicals/disambiguation.html
[Unigram model]:                 ../079-osnov-programm/classes/04_2.html
[Dependency parsing]:            practicals/dependency.html
[Unigram part-of-speech tagger]: ../079-osnov-programm/classes/05.html

## Schedule

We are scheduled to meet every Tuesday 18.10-21.00 MSK. Generally
we will alternate between classes with new material and
co-working.

Co-working classes are optional, and are an opportunity to work
together on NLP projects (even those not part of the class) and
ask questions of peers and instructors.

[project-rfp]:         projects/rfp.html
[segmentation-slides]: slides/segmentation.pdf
[segmentation-video]:  https://peertube.xyz/videos/watch/55348c29-1f15-4e8b-a02a-5c7fb21b6acd
[tokenization-slides]: slides/tokenisation.pdf
[tokenization-video]:  https://peertube.xyz/videos/watch/772d548b-e04c-49ae-9c60-7134fc1ba098
[segtok-quiz]:         quizzes/quiz-01.html
[morphology-slides]:   slides/morphology.pdf
[morphology-video]:    https://peertube.xyz/videos/watch/5811dfa7-9984-4c02-97e2-90934810fe9e
[morphology-quiz]:     quizzes/quiz-02.html

### Oct 9

In this class we will give an introduction to the syllabus and help with
installing the requisite software.

### Oct 16

Sentence segmentation ([slides][segmentation-slides],
[video][segmentation-video]) and tokenization & word segmentation
([slides][tokenization-slides], [video][tokenization-video]).

Read §3.9 *Word and Sentence Tokenisation* in [Jurafsky-Martin 2ed] and
§4.2.4 *Sentences* in [Manning-Schütze]. [Reading quiz][segtok-quiz] due
Tue Oct 30.

Start [practical 1][Segmentation & Tokenization].

### Oct 23

Exam week, no class.

### Oct 30

Co-work on [Segmentation & Tokenization].

Due: [quiz 1][segtok-quiz].

### Nov 2 (**Friday**)

Finite-state morphology ([slides][morphology-slides],
[video][morphology-video]).

Read §3.2-3.7 of [Jurafsky-Martin 2ed], and all (but especially §4) of
[Karttunen]. [Reading quiz][morphology-quiz] due <!-- FIXME: --> no
earlier than Nov 13. 

Due: [practical 1 Segmentation & Tokenization][Segmentation &
Tokenization], [project proposals][project-rfp].

Start practical 2, [Finite-state Morphology] (algorithms) or
[Transliteration] (engineering).

### Nov 6

Co-work on practical 2, [Finite-state Morphology] (algorithms) or
[Transliteration] (engineering).

### Nov 13

Morphological disambiguation ([slides][morph-disam-slides],
[video][morph-disam-video]).

Read §5.1-5.8 in [Jurafsky-Martin 2ed]. [Reading quiz][morph-disam-quiz] due <!-- FIXME --> no earlier than Nov 27.

Due: practical 2, [Finite-state Morphology] (algorithms) or
[Transliteration] (engineering), [quiz-02][morphology-quiz].

Start practical 3, [Morphological disambiguation] (algorithms) or
[Unigram model] (engineering).

### Nov 20

Co-work on practical 3, [Morphological disambiguation] (algorithms) or
[Unigram model] (engineering).

### Nov 27

Dependency parsing ([slides][dep-parse-slides],
[video][dep-parse-video]).

Read Chapter 13 *Dependency parsing* in [Jurafsky-Martin 3ed]. [Reading
quiz][dep-parse-quiz] due <!-- FIXME --> no earlier than Dec 11.

Due: practical 3, [Morphological disambiguation] (algorithms) or
[Unigram model] (engineering), [quiz-03][morph-disam-quiz].

Start practical 4, [Dependency parsing] (algorithms) or [Unigram
part-of-speech tagger] (engineering).

### Dec 4

Co-work on practical 4, [Dependency parsing] (algorithms) or [Unigram
part-of-speech tagger] (engineering).

### Further

To be decided.

## Details

### Submission

All submissions are carried out through pull-requests on
[Github][github.com]. See [submission guidelines] for details.

Deadlines are all 23:59:59 [anywhere on
earth](https://en.wikipedia.org/wiki/Anywhere_on_Earth).

### Marking

* 70% Practicals
* 20% Reading Quizzes
* 10% Active participation

### Quizzes

Each lecture will have a short reading quiz attached.

### Active participation

Beyond simply showing up, I encourage you to contribute to
discussions by asking questions, answering questions, making
relevant comments, helping classmates and asking for help with
in-class activities, etc. There are no stupid questions &mdash; I
want to make sure everyone grasps the concepts, and many are not
as straightforward as they may first seem (or as I think they
are). You are also expected to have read any assigned readings
before class.

### In the classroom

Note on pronouns: If you'd like to be referred to by a pronoun
that you think we might not guess correctly or if you notice us
referring to you by some other pronoun than what you'd prefer,
please let me know so that we can get it right.


Note on language: If we are talking too fast, or if we use an
expression that you do not understand and you think it is having
an effect on your learning, please ask us to slow down. You are
welcome to come and talk to us at any time about issues relating
to language. We will be happy to discuss them.


<!-- References -->

[Jurafsky-Martin 2ed]:  http://www.cs.colorado.edu/~martin/slp.html
[Manning-Schütze]:   https://nlp.stanford.edu/fsnlp/
[Karttunen]:         https://web.stanford.edu/~laurik/publications/fsc-91/fsc91.html
[Jurafsky-Martin 3ed]:  https://web.stanford.edu/~jurafsky/slp3/

</div>

