# hello-package-python

## Empty __init_.py

```
> pip install .
> python
Python 3.6.5 (default, Apr  4 2018, 10:31:24)
[GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import hello
>>> hello.age.age()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'hello' has no attribute 'age'
>>> import hello.age
>>> hello.age.age()
10
>>> import hello.name
>>> hello.name.name()
'john'
```

## Non empty __init__.py

```
> cat ./src/hello/__init__.py
# Comment out the following if we want to expose everything to the package level.
from hello.age import *
from hello.name import *
```

```
> python
Python 3.6.5 (default, Apr  4 2018, 10:31:24)
[GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import hello
>>> hello.age()
10
>>> hello.name()
'john'
```