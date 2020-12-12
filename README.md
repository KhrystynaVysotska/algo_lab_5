## Повний перебір (наївний алгоритм пошуку)

### Завдання:
Реалізувати вказаний алгоритм пошуку підстрічки в стрічці.

### *Вхiднi данi*

Вхiдний файл strings.in складається з двох рядкiв.

* Перший рядок містить вхідну стрічку довжиною k.
* Другий рядок містить підстрічку довжиною l (l < k), координати якої (початковий і кінцевий індекси) потрібно знайти.
Кількість повторів -довільна, від  0  і може бути більшою k/l.
### *Вихiднi данi*

Вихiдний файл strings.out повинен мiстити всі знайдені координати даної підстрічки.

### Installation

Use [git](https://git-scm.com/downloads/) to install lab code
```
git clone https://github.com/KhrystynaVysotska/algo_lab_5.git
```

### Usage
In command line use [python](https://www.python.org/)
```
python substring_search.py
```

### Algorithm
Algorithm takes each element from input string and sequentially 
checks matching with given substring. 

In case mismatch was found, the loop is interrupted and the next element in input string is 
taken.
If substring matches some part of string, its coordinates
(start and end indexes) are written to the list.

Time complexity: O(N*M), where N - length of input string and M - length of substring
