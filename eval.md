# Changer le type d'une chaîne retournée par input

La fonction input retourne sous forme d'une chaîne de caractères ce qui est saisi par un utilisateur.
```python
>>> input("Veuillez saisir un nombre: ")
Veuillez saisir un nombre: 2
'2'
```
Le problème est que ce qui est retourné par input n'est pas un nombre, mais bien une chaîne de caractères, ce qui va poser des problèmes dans la suite du code.

```python
>>> a = input("Veuillez saisir un nombre: ")
Veuillez saisir un nombre: 2
>>> 3 + a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
