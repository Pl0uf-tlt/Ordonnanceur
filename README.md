# Ordonnanceur

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Credit](#credit)

## About <a name = "about"></a>

The goal of this project is to create a scheduler for fictional processes. The scheduler works with priorities.

The Processus.py module contains the process class wich defines what a fictional process is and some test sets. 

The Ordo.py file contains the main fonctions (triTpsArr, triPrio, triPrioExe, ordo, affichageOrdo, affichageOrdo2) and some tests on known test sets.

The Ordo.C file contains the process structure and (for now) only the FIFO function. 


## Getting Started <a name = "getting_started"></a>

Python 3 is needed

### Installing

You need to have both Ordo.py and Processus.py in the same directory for the python scheduler to work.
You can clone this directory with this command :
```bash
git clone https://github.com/Pl0uf-tlt/Ordonnanceur.git
```
It will also download the C scheduler at the same time. The C scheduler needs gcc to work, please make sure you have it on your machine.

The python version needs matplotlib wich is a library used to make plots. 
You can download it using pit with those two commandes :
```bash
$ python -m pip install -U pip
$ python -m pip install -U matplotlib
```

## Usage <a name = "usage"></a>

To use the python scheduler please execute Ordo.py

```bash
$ python3 Ordo.py
```

To use the C scheduler please compile it first :
```bash
$ gcc -Wall Ordo.c -o Ordo
```

Then use the executable with 

```bash
$ ./Ordo
```

## Credit <a name = "credit"></a>

Author : Cédric Toulotte <toulottece@cy-tech.fr>
