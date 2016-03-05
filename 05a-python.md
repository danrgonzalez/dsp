# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists are like arrays in Java. The lists can be modified at any time. Items can be deleted and inserted. Lists are mutable. Tuples, are immutable. They are enclosed by parenthesis and the items in the tuples exist as a whole. Although they can be sliced and concatenated. Order matters in tuples. Tuples can work as primary keys in dictionaries because of their immutable nature. Lists are not guaranteed to be unique. 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are similar in that they contain items. However, sets contain unordered, unique and immutable items. Tuples can be added to sets but not lists. Examples:

>> cities = set(("Paris", "Lyon", "London","Berlin","Paris","Birmingham"))
>> cities
>> set(['Paris', 'Birmingham', 'Lyon', 'London', 'Berlin'])

Since sets contain unique object, they can be faster in finding an element. Whereas list can contain duplicate objects and therefore can take longer to find a particular object. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> A lambda function in python acts like a function without being explicitly defined. The syntax is different. It offers the ability to locally create a computation without having to create a function. 

sorted(tuples, key = lambda tuples: tuples.ID)

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> map(func, seq) applies the func to all elements in seq and returns a new list with the elements modified by func. 
>> filter(function, list) eliminates elements from a list that do not return true via the function. 
>> A set comprehension example: s = {v for v in 'ABCDABCD' if v not in 'CB'} --> {'A','D'}
>> A dictionary compresion example: d = {d: n**2 for n in range(5)}

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> response added to file

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> response added to file

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> response added to file

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

>> response added to file

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





