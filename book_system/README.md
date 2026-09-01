# Book System

## Main Objectives

- Tuples
- List
- Dictionaries
- CRUD, creating, reading , updating, deleting.

### Steps

- We need somewhere we will store all books : list

```python

[
    {
    'title': 'Atomic Habits', # string
    'author': "James Clear", # string
    'category': "Behavior", # string
    'year_published': 2018 # int, datetime=>later
    },
    {
    'title': 'Atomic Habits', # string
    'author': "James Clear", # string
    'category': "Behavior", # string
    'year_published': 2018 # int, datetime=>later
    },
    {
    'title': 'Atomic Habits', # string
    'author': "James Clear", # string
    'category': "Behavior", # string
    'year_published': 2018 # int, datetime=>later
    }
]



```

- We need a structure of a book that will be created: dictionary

```python
{
    'title': 'Atomic Habits', # string
    'author': "James Clear", # string
    'category': "Behavior", # string
    'year_published': 2018 # int, datetime=>later
}

```

- Instead of guessing the categories, we need to have constant categories defined: tuple , 
- A tuple because the categories are being defined as constant, which means they wont be chnaging.

```python

CATEGORIES = ("Fiction", "Science", "History")

```


- Functions to organize the code,