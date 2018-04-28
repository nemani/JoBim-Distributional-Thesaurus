# Distributional Thesaurus using JoBim Algorithm

### Arjun Nemani

### Alok Debnath

### Sahil Bakshi

Sahil converted the mouse corpus using [(stanford dependecy parser)](https://sourceforge.net/projects/jobimtextgpl.jobimtext.p/), and performed Holling Function on it.

Alok wrote the code for Pointwise Mutual Information as Similarity Function

Arjun wrote code to make a Graph-Based Aggregation Function.
Arjun also wrote the interface to interact with the DT.

Usage:

* To find N most common words:
* \*\* python3 main.py
* To generate thesaurus
* \*\* python3 thesuarus.py > DT.txt

Examples:

> python3 main.py

Loading

TotalCount: 288902, JoBimCount:171790, JoCount:23096, BimCount:66244

Welcome to the DT!

Pruning factor is set to 4.5

Enter number of words needed:5

Enter word:dog

dog#nn

    1 - pesticide-resistance#nn - 1 times

    2 - please#vb - 1 times

    3 - hamster#nn - 1 times

    4 - partner#nn - 1 times

    5 - investigates#nn - 1 times

Enter word:bite

bite#vb

    1 - drag#vb - 3 times

    2 - retrieve#vb - 2 times

    3 - ask#vb - 2 times

    4 - retaliate#vb - 2 times

    5 - marry#vb - 2 times

bite#nn

    1 - behaviour#nn - 3 times

    2 - attack#nn - 3 times

    3 - sighting#nn - 2 times

    4 - worship#nn - 2 times

    5 - tail#nn - 2 times

Enter word:bit

bit#vb

    1 - come#vb - 2 times

    2 - harass#vb - 1 times

    3 - revenge#vb - 1 times

    4 - answers#vb - 1 times

    5 - meet#vb - 1 times

bit#nn

    1 - part#nn - 2 times

    2 - recovery#nn - 1 times

    3 - youth#nn - 1 times

    4 - settlement#nn - 1 times

    5 - khan#nn - 1 times

bit#jj

    1 - next#jj - 1 times

    2 - several#jj - 1 times

    3 - spare#jj - 1 times

    4 - most#jjs - 1 times

    5 - multiple#jj - 1 times
