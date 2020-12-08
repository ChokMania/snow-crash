# Snow-Crash [(sujet)](https://cdn.intra.42.fr/pdf/pdf/13254/fr.subject.pdf)

![Alt Text](https://media.giphy.com/media/eCqFYAVjjDksg/giphy.gif)

## Introduction
En tant que développeur, vous risquez dans votre carrière de travailler sur des logiciels qui vont être utilisés par des centaines de personnes.

Si votre logiciel présente une vulnérabilité, les personnes l’utilisant sont également vulnérables et exposées avec un système exploitable.

Il est de votre responsabilité de comprendre les techniques utilisées pour exploiter les vulnérabilités afin de pouvoir les détecter, et les éviter.

Ce projet est donc une petite introduction à ce vaste monde qu’est la sécurité en
informatique, où le droit à l’erreur ne doit pas exister.

## Objectifs
Ce projet a pour but de vous faire découvrir, via plusieurs petits challenges, la sécurité en informatique dans plusieurs domaines.

Les méthodes que vous allez utiliser, plus ou moins complexes, vous feront voir différemment l’informatique en général.

Durant ce projet, vous allez surement rencontrer des difficultés : soyons clairs, ces difficultés, il faut que vous les dépassiez de vous-même. Il faut que votre approche des différentes épreuves vienne vraiment et uniquement de VOUS. L’intérêt ici est de vous faire développer une certaine logique qui va vous suivre par la suite. Avant de demander de l’aide, demandez-vous bien si vous avez vraiment réfléchi à toutes les possibilités.

## Failles

| Name | French | English | Sources
|:---------|:--------:|:--------:|:--------:|
|level00|[FR](https://github.com/ChokMania/snow-crash/blob/master/level00/Ressources/explications_fr.md)| [EN](https://github.com/ChokMania/snow-crash/blob/master/level00/Ressources/explanations_en.md) | |
|level01|[FR](https://github.com/ChokMania/snow-crash/blob/master/level01/Ressources/explications_fr.md)| [EN]() | |
|level02|[FR](https://github.com/ChokMania/snow-crash/blob/master/level02/Ressources/explications_fr.md)| [EN]() | [Read PCAP](https://serverfault.com/questions/38626/how-can-i-read-pcap-files-in-a-friendly-format) / [SCP](https://linuxize.com/post/how-to-use-scp-command-to-securely-transfer-files/)|
|level03|[FR](https://github.com/ChokMania/snow-crash/blob/master/level03/Ressources/explications_fr.md)| [EN]() | [Analyze Binary](https://opensource.com/article/20/4/linux-binary-analysis) / [Exploit system Command](https://stackoverflow.com/questions/8304396/what-is-vulnerable-about-this-c-code)|
|level04|[FR](https://github.com/ChokMania/snow-crash/blob/master/level04/Ressources/explications_fr.md)| [EN]() | [Perl](https://formation-perl.fr/guide-perl-05.html) / [Perl Parameters](https://www.cs.ait.ac.th/~on/O/oreilly/perl/learn32/ch18_04.htm)|
|level05|[FR](https://github.com/ChokMania/snow-crash/blob/master/level05/Ressources/explications_fr.md)| [EN]() | |
|level06|[FR](https://github.com/ChokMania/snow-crash/blob/master/level06/Ressources/explications_fr.md)| [EN]() | [Regex](https://regex101.com/) / [Preg_Replace](https://www.php.net/manual/fr/function.preg-replace.php) / [Pattern Modifiers](https://www.php.net/manual/en/reference.pcre.pattern.modifiers.php)|
|level07|[FR](https://github.com/ChokMania/snow-crash/blob/master/level07/Ressources/explications_fr.md)| [EN]() | |
|level08|[FR](https://github.com/ChokMania/snow-crash/blob/master/level08/Ressources/explications_fr.md)| [EN]() | |
|level09|[FR](https://github.com/ChokMania/snow-crash/blob/master/level09/Ressources/explications_fr.md)| [EN]() | [Char in Python](https://stackoverflow.com/questions/47310929/does-python-support-character-type) / [Encoding](https://stackoverflow.com/questions/27366479/python-3-os-walk-file-paths-unicodeencodeerror-utf-8-codec-cant-encode-s)|
|level10|[FR](https://github.com/ChokMania/snow-crash/blob/master/level10/Ressources/explications_fr.md)| [EN]() | [Exploit acces Command](https://security.stackexchange.com/questions/42659/how-is-using-acces-opening-a-security-hole) / [Race Condition Vulnerability Lab/ ](https://github.com/firmianay/Life-long-Learner/blob/master/SEED-labs/race-condition-vulnerability-lab.md) [File access race condition](https://vulncat.fortify.com/en/detail?id=desc.controlflow.cpp.file_access_race_condition)|
|level11|[FR](https://github.com/ChokMania/snow-crash/blob/master/level11/Ressources/explications_fr.md)| [EN]() | |
|level12|[FR](https://github.com/ChokMania/snow-crash/blob/master/level12/Ressources/explications_fr.md)| [EN]() | [Transliteration](https://unix.stackexchange.com/questions/86929/can-tr-work-with-regex) / [Perl Operators](http://perl.mines-albi.fr/DocFr/perlrequick.html) / [Regex](https://regex101.com/)|
|level13|[FR](https://github.com/ChokMania/snow-crash/blob/master/level13/Ressources/explications_fr.md)| [EN]() | [Modify Function Return](https://www.opensourceforu.com/2011/08/modify-function-return-value-hack-part-1/) / [GDB cheatsheet](https://darkdust.net/files/GDB%20Cheat%20Sheet.pdf) / [GDB Breakpoints](https://sourceware.org/gdb/onlinedocs/gdb/Set-Breaks.html) / [%esp, %ebp](https://reverseengineering.stackexchange.com/questions/2073/what-purpose-of-mov-esp-ebp) / [Asm Main Preamble](https://reverseengineering.stackexchange.com/questions/15173/what-is-the-purpose-of-these-instructions-before-the-main-preamble)|
|level14|[FR](https://github.com/ChokMania/snow-crash/blob/master/level14/Ressources/explications_fr.md)| [EN]() | [Man ptrace](https://www.man7.org/linux/man-pages/man2/ptrace.2.html) / [Bypassing ptrace LD_PRELOAD](https://dev.to/denisnutiu/bypassing-ptrace-calls-with-ldpreload-on-linux-12jl) / [Bypass ptrace Catchpoint](https://gist.github.com/poxyran/71a993d292eee10e95b4ff87066ea8f2)|

## Auteurs

- [Florian Blanchard](https://github.com/floblanc)
- [Mathieu Ginisty](https://github.com/maginist)
- [Martin de Lagarde](https://github.com/Martydl)
- [Julien Dumay](https://github.com/ChokMania)

