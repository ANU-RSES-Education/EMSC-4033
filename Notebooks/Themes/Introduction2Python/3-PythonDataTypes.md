---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.12
    jupytext_version: 1.6.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Python data types

Python can be a little strange in providing lots of data types, dynamic type allocation, and some interconversion. 


## Numbers

Integers, Floating point numbers, and complex numbers are available automatically.

```{code-cell} ipython3
f = 1.0
i = 1

print (f, i)
print 
print ("Value of f is {}, value of i is {}".format(f,i))
print 
print ("Value of f is {:f}, value of i is {:f}".format(f,i))
```

```{code-cell} ipython3
:tags: [raises-exception]

## BUT !! 

print ("Value of f is {:d}, value of i is {:f}".format(f,i))
```

```{code-cell} ipython3

c = 0.0 + 1.0j

print (c)

print ("Value of c is {:f}".format(c))

print ("Value of c**2 is {:f}".format(c**2))
```

---

Notes: The `math` module needs to be imported before you can use it. 

```{code-cell} ipython3
import math
math.sqrt(f)
```

```{code-cell} ipython3
:tags: [raises-exception]

math.sqrt(c)
```

```{code-cell} ipython3
:tags: [raises-exception]

math.sqrt(-1)
```

```{code-cell} ipython3
import cmath

print (cmath.sqrt(f))
print (cmath.sqrt(c))
print (cmath.sqrt(-1))
```

### numbers as objects 

Virtually everything in python is an object. This means that it is a __thing__ that can have multiple copies made (all of which behave independently) and which knows how to __do__ certain operations on itself. 

For example, a floating point number knows certain things that it can do as well as simply "being" a number:

```{code-cell} ipython3
f
```

```{code-cell} ipython3
help(f)
```

```{code-cell} ipython3
print (f.is_integer() ) # Strange eh ?
print (f.conjugate())
print (c.conjugate())
print (f.__truediv__(2.0) ) # This looks odd, but it is the way that f / 2.0 is implemented underneath
```

```{code-cell} ipython3
1.0.__truediv__(2.0)
```

## Strings




```{code-cell} ipython3
s = 'hello'
print (s[1]  )
print (s[-1])
print (len(s)      )  
print (s + ' world')
```

```{code-cell} ipython3
ss = "\t\t HellO \n \t\t world\n  \t\t !!!\n\n "
print (ss)
print (ss.partition(' '))
```

```{code-cell} ipython3
"Hello World".lower()
```

```{code-cell} ipython3
print (s[-1]," ", s[0:-1])
```

---

But one of the problems with strings as data structures is that they are immutable. To change anything, we need to make copies of the data

```{code-cell} ipython3
:tags: [raises-exception]

s[1] = 'a'
```

---

## tuples and lists and sets

Tuples are bundles of data in a structured form but they are not vectors ... and they are immutable

```{code-cell} ipython3
a = (1.0, 2.0, 0.0)
b = (3.0, 2.0, 4.0)

print (a[1])
print (a + b)
```

```{code-cell} ipython3
:tags: [raises-exception]

print (a-b)
```

```{code-cell} ipython3
:tags: [raises-exception]

print (a*b)
```

```{code-cell} ipython3
print( 2*a)
```

```{code-cell} ipython3
:tags: [raises-exception]

a[1] = 2
```

```{code-cell} ipython3
e = ('a', 'b', 1.0)
2 * e
```

---

Lists are more flexible than tuples, they can be assigned to, have items removed etc

```{code-cell} ipython3
l  = [1.0, 2.0, 3.0]
ll = ['a', 'b', 'c']
lll = [1.0, 'a', (1,2,3), ['f','g', 'h']]

print (l)
print (ll)
print (l[2], ll[2])
print (2*l)
print (l+l)
print (lll)
print (lll[3], " -- sub item 3 --> ", lll[3][1])
```

```{code-cell} ipython3
:tags: [raises-exception]

2.0*l
```

```{code-cell} ipython3
l[2] = 2.99
l
```

```{code-cell} ipython3
l.append(3.0)
print (l)
```

```{code-cell} ipython3
ll += 'b'
print (ll)
ll.remove('b')  # removes the first one !
print (ll) 
```

```{code-cell} ipython3
:hide_input: false
:tags: [raises-exception]

l += [5.0]
print ("1 - ", l)
l.remove(5.0)
print ("2 - ", l)
l.remove(3.0)
print( "3 - ", l)
l.remove(4.0)
print ("4 - ", l)
```

---

Sets are special list-like collections of unique items. NOTE that the elements are not ordered (no such thing as `s[1]` 

```{code-cell} ipython3
s = set([6,5,4,3,2,1,1,1,1])
print (s)
s.add(7)
print (s)
s.add(1)

s2 = set([5,6,7,8,9,10,11])

s.intersection(s2)
s.union(s2)
```

## Dictionaries

These are very useful data collections where the information can be looked up by name instead of a numerical index. This will come in handy as a lightweight database and is commonly something we need to use when using modules to read in data. 

```{code-cell} ipython3
d = { "item1": ['a','b','c'], "item2": ['c','d','e']}

print (d["item1"])
print (d["item1"][1])

d1 = {"Small Number":1.0, "Tiny Number":0.00000001, "Big Number": 100000000.0}

print (d1["Small Number"] + d1["Tiny Number"])
print (d1["Small Number"] + d1["Big Number"])

print (d1.keys())

for k in d1.keys():
    print ("{:>15s}".format(k)," --> ", d1[k])
```

More useful is the fact that the dictionary can have as a key, anything that can be converted using the `hash` function into a unique number. Strings, obviously, work well but anything immutable can be hashed:

```{code-cell} ipython3
def hashfn(item):
    try:
        h = hash(item)
        print ("{}".format(str(item)), " --> ", h)
    except:
        print ("{}".format(item), " -->  unhashable type {}".format((type(item))))
    return


hashfn("abc")
hashfn("abd")
hashfn("alphabeta")
hashfn("abcdefghi")

hashfn(1.0)
hashfn(1.00000000000001)
hashfn(2.1)

hashfn(('a','b'))
hashfn((1.0,2.0))

hashfn([1,2,3])

import math
hashfn(math.sin)  # weird ones !! 
```

+++ {"solution": "hidden"}

---

__Exercise__: _Build a reverse lookup table_

Suppose you have this dictionary of phone numbers:

```python
phone_book = { "Achibald":   ("04", "1234 4321"), 
               "Barrington": ("08", "1111 4444"),
               "Chaotica" :  ("07", "5555 1234") }

```

Can you construct a reverse phone book to look up who is calling from their phone number ?
    
    

+++ {"solution": "shown", "solution_first": true}

__Solution:__ Here is a possible solution for the simple version of the problem but this could still use some error checking (if you type in a wrong number) 

```{code-cell} ipython3
# Name: ( area code, number )
phone_book = { "Achibald":   ("04", "1234 4321"), 
               "Barrington": ("08", "1111 4444"),
               "Chaotica" :  ("07", "5555 1234") }
```

```{code-cell} ipython3
newdict = {}
for key in phone_book:
    newdict[phone_book[key]] = key
newdict
```

```{code-cell} ipython3
letters_and_numbers = [['a', 1], ['b', 2], ['c', 3]]
```

```{code-cell} ipython3
[i**2 for i in range(10)]
```

```{code-cell} ipython3
phone_book.items()
```

```{code-cell} ipython3
%%timeit

{val:key for key, val in phone_book.items()}
```

```{code-cell} ipython3
for letter, number in letters_and_numbers:
    print(number * letter)
```

```{code-cell} ipython3
:solution: shown

# Name: ( area code, number )
phone_book = { "Achibald":   ("04", "1234 4321"), 
               "Barrington": ("08", "1111 4444"),
               "Chaotica" :  ("07", "5555 1234") }

reverse_phone_book = {}
```

```{code-cell} ipython3
:solution: shown

%%timeit

for key in phone_book.keys():
    reverse_phone_book[phone_book[key]] = key

    
```

```{code-cell} ipython3
print (reverse_phone_book[('07','5555 1234')])
```

```{code-cell} ipython3

```
