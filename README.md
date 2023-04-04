# Ausy POEI : Maze in python

<a href="https://img.shields.io/badge/Python-3.11.2-4483B5" alt="Python">
        <img src="https://img.shields.io/badge/Python-3.11.2-4483B5" /></a>
<a href="https://img.shields.io/badge/pip-23.0.1-FFE05B" alt="NPM">
        <img src="https://img.shields.io/badge/pip-23.0.1-FFE05B" /></a>

---

This project aims to implement **mazes resolution algorithms**.

## Mandatories

* Create maze in **.txt** extention
* Unsolved mazes are in a root directory named **Unsolved**
* Solved mazes are in a root directory named **Solved**
* All sources are in a root directory named **Src**
* Use **Sqlite3**
* A **Game Menu**

#### Mazes

* Walls "#"
* Empty " "
* Path "X"
* One start / end

#### Game Menu

* Option 1 :
  * Display data form the solved mazes
  * Format :  `<file_name>; <date>; <time>`
* Option 2 :
  * Load randomly 1 maze form the **Unsolved** diretory and solved it
  * Display the maze solution
  * Save the **Date, Time** and **Name** of the maze solved
  * Move the maze into the **Solved** directory
* Option 3 :
  * Generate a maze with **X** and **Y** given as args and place it into the **Unsolved** directory
* Option 4 :
  * Exit game

## Build

You need to have an environment who can **compile Pyhton files**.

**Terminal :**

```
python3 __start__.py
```

**IDE :**

run into your IDE

## Authors

* **Yoann Le Saint**
* **Simon Tessier**
