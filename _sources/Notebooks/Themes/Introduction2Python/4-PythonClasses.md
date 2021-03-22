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

# Classes and objects

Python is an object oriented language. We briefly mentioned that objects are self-contained entities that bundle together data and functionality. We also discussed how we can have multiple copies of objects.

Pretty much everything in python is an object. It may not be obvious at this point why it is useful to have a language that works this way and, in fact, this is not something we will dwell upon.

However, it is important to be able to recognise that certain things are objects and that objects are defined by a language construct called a `class` if only to be able to read the documentation and know what to expect.

Let's just look at a couple of examples - ways to bundle up some data easily


```{code-cell} ipython3
class colour(object):
    
    rgb = (0.0,0.0,0.0)
    description = "Black"
    
    
```

```{code-cell} ipython3
c = colour()
d = colour()
```

```{code-cell} ipython3
print (c.description)
print (c.rgb)
print (d.description)
print (d.rgb)
```

```{code-cell} ipython3
d.description = 'Blue'
d.rgb = (0.0,0.0,1.0)
```

```{code-cell} ipython3
print (c.description)
print (c.rgb)
print (d.description)
print (d.rgb)
```

`colour` is a data container that standardises how we refer to colours. By default it is "Black" but we can always change the values. The only thing is, we can also do this:

```{code-cell} ipython3
d.complement = (1.0,1.0,0.0)
print (d.complement)
```

```{code-cell} ipython3
:tags: [raises-exception]

print (c.complement)  # This is expected to fail (why ?)
```

So much for standardisation ! 

The `colour` class defines how objects will look once defined, but each 'instance' of the class (here `c` and `d`) lives a life of its own once built.

```{code-cell} ipython3
class colour(object):
    
    rgb = (0.0,0.0,0.0)
    description = "Black"
    complement  = (1.0,1.0,1.0)
    
e = colour()
print (e.complement)
```

```{code-cell} ipython3
:tags: [raises-exception]

print (c.complement)  # This is also expected to fail (why ?)
```

```{code-cell} ipython3
print (type(e) == type(d))
```

And changing the definition of the class does not affect the instances that have already been defined. The class definition is copied into the object. 

---

A better way to deal with this is to define some methods that also live in the class and use those to set values of data at initialisation time, and to define how the class behaves.

Let's look at a better way to initialise the class:

```{code-cell} ipython3
class colour2(object):   
    """
    An rgb colour object with a description of the colour 
    """
    
    def __init__(self, rgb = (0.0,0.0,0.0), description="Black"):
        
        self.rgb = rgb
        self.description = description
        self.complement = ( 1.0 - rgb[0], 1.0 - rgb[1], 1.0-rgb[2] )
        
        return

new_c = colour2(rgb=(1.0,0.0,0.0), description="Red")
new_d = colour2(rgb=(0.0,1.0,0.0), description="Green")

print (new_c.rgb)
print (new_c.complement)

```

```{code-cell} ipython3
help(colour2)
```

```{code-cell} ipython3
class colour2(object):   
    """
    An rgb colour object with a description of the colour 
    """
    
    def __init__(self, rgb = (0.0,0.0,0.0), description="Black"):
        
        self.rgb = rgb
        self.description = description
        self.complement = ( 1.0 - rgb[0], 1.0 - rgb[1], 1.0-rgb[2] )
        
        return

    def mix(self, other):
        if type(self) != type(other):
            print ("Cannot mix apples and oranges")
            return
        else:
            return ( 0.5*(self.rgb[0]+other.rgb[0]),
                     0.5*(self.rgb[1]+other.rgb[1]),
                     0.5*(self.rgb[2]+other.rgb[2]) )
        
    def mixmax(self, other):
        if type(self) != type(other):
            print ("Cannot mix apples and oranges")
            return
        else:
            return ( min(self.rgb[0]+other.rgb[0],1.0),
                     min(self.rgb[1]+other.rgb[1],1.0),
                     min(self.rgb[2]+other.rgb[2],1.0) )

```

```{code-cell} ipython3
new_c = colour2(rgb=(1.0,0.0,0.0), description="Red")
new_d = colour2(rgb=(0.0,1.0,0.0), description="Green")
```

```{code-cell} ipython3
print (new_c.mix(new_d))
print (new_c.mixmax(new_d))
```

## More interesting stuff

One of the extensibility secrets of python is that all the language operators are defined by special 'invisible' functions on the classes. 

Look at the following example. 

```{code-cell} ipython3
class colour3(object):   
    """
    An rgb colour object with a description of the colour 
    """
    
    def __init__(self, rgb = (0.0,0.0,0.0), description="Black"):
        
        self.rgb = rgb
        self.description = description
        self.complement = ( 1.0 - rgb[0], 1.0 - rgb[1], 1.0-rgb[2] )
        
        return

    def mix(self, other):
        if type(self) != type(other):
            print ("Cannot mix apples and oranges")
            return
        else:
            return ( 0.5*(self.rgb[0]+other.rgb[0]),
                     0.5*(self.rgb[1]+other.rgb[1]),
                     0.5*(self.rgb[2]+other.rgb[2]) )
        
    def mixmax(self, other):
        if type(self) != type(other):
            print ("Cannot mix apples and oranges")
            return
        else:
            return ( min(self.rgb[0]+other.rgb[0],1.0),
                     min(self.rgb[1]+other.rgb[1],1.0),
                     min(self.rgb[2]+other.rgb[2],1.0) )

        
    def __add__(self, other):
        
        return self.mix(other)


    def __mul__(self, other):
        
        return self.mixmax(other)



    
new_c = colour3(rgb=(1.0,0.0,0.0), description="Red")
new_d = colour3(rgb=(0.0,1.0,0.0), description="Green")
```

```{code-cell} ipython3
print (new_c.mix(new_d))
print (new_c + new_d)

print (new_c.mixmax(new_d))
print (new_c * new_d)
```

That's all we really need to know about classes, but if you want to know more about that last example, you'll need to know about this page at the very least: [Object Model: numeric types](https://docs.python.org/2/reference/datamodel.html#emulating-numeric-types) from the python documentation. This is mostly advanced stuff, but if you find yourself being given a class description when you ask for help on something, this information will help you.

```{code-cell} ipython3
## 1. Another example would be to make sure to set complement any time rgb gets changed
## 2. Another example would be to show how to subclass colour and match types so anything with an rgb works for mixing
```
