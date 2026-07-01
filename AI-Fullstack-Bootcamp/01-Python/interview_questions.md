Day 1:
Question 1:
    x = 10
    print(type(x))

    Answer: <class 'int'>

Question 2:
    x = 10
    y = 20

    x, y = y, x

    print(x, y)

    Answer: 20 10

Question 3:
    x = True
    print(type(x))

    Answer: <class 'bool'>

Question 4: 
    Difference between [] and ()

    Answer: [] is a List.

Question 5: 
    Difference between {} and set()

    Answer: {}

Question 6:
    x = 10
    print(type(float(x)))

    Answer: <class 'float'>

Question 7:
    print(type("100"))

    Answer: <class 'str'>

Question 8: 
    print(type(10.5))
    
    Answer: <class 'float'>

Question 9: 
    print(type([10,20,30]))

    Answer: <class 'list'>

Question 10:
    print(type((10,20,30)))

    Answer: print(type((10,20,30)))

Question 11: 
    x = 10
    y = "10"

    print(x == y)

    Answer: False

Question 12: 
    x = 10
    y = 10.0

    print(x == y)

    Answer: True

Question 13:
    x = 10
    y = 10.0

    print(type(x))
    print(type(y))

    Answer: <class 'int'>
            <class 'float'>

Queston 14: 
    x = None

    print(type(x))

    Answer: <class 'NoneType'>

Question 15:
    x = True
    y = False

    print(x + y)

    Answer: 1

    Explanation: 
        True = 1
        False = 0

        True + False

        1 + 0

        1

#=======================================================================
Python Gems:

True == 1      # True

False == 0     # True

bool(1)        # True

bool(0)        # False

bool("")       # False

bool([])       # False

bool({})       # False

bool(None)     # False

#=======================================================================

Question 16:
    print(bool(""))

    Answer: False

Question 17:
    print(bool("Python"))

    Answer: True
    
Question 18:
    print(bool([]))

    Answer: False
    
Question 19:
    print(bool([10]))

    Answer: True
    
Question 20:
    print(bool(None))

    Answer: False
    
#=======================================================================
Python Truthy and Falsy Values

    Falsy Values:
        False
        None
        0
        0.0
        ''
        []
        ()
        {}
        set()

    Truthy Values
        1
        -10
        3.14
        'Python'
        [1, 2]
        (1, 2)
        {'name': 'Rabbani'}
        {1, 2}
#=======================================================================

Question 21:
    print(bool(0))
    
    Answer: 
    
Question 22:
    print(bool(-10))

    Answer: 

Question 23:
    print(bool(0.0))

    Answer: 
    
Question 24:
    print(bool(0.1))

    Answer: 
    
Question 25:
    print(bool({}))

    Answer: 
    
Question 26:
    print(bool({"name": "Rabbani"}))

    Answer: 

#================================================================
Tricky Question:
    x = [1, 2, 3]
    y = x

    y.append(4)

    print(x)
    print(y)

    Think carefully:

    What is the output of x?
    What is the output of y?
    Why?

    Correct Answer: 
        [1, 2, 3, 4]
        [1, 2, 3, 4]

    Step 1:
        x = [1, 2, 3]

    Step 2:
        y = x

        Many beginners think this creates a new list.

        It does NOT.

        Instead:
            x ──┐
                │
                ▼
            [1,2,3]
                ▲
                │
            y ──┘

        Now both variables point to the same list object.

    Step 3:
        Now both variables point to the same list object.

        Since x and y refer to the same list, the list itself changes.

        x ──┐
            │
            ▼
        [1,2,3,4]
            ▲
            │
        y ──┘

    Step 4: 
        print(x)
        [1, 2, 3, 4]
    step 5: 
        print(y)
        [1, 2, 3, 4]

If You Want a Copy
    x = [1,2,3]

    y = x.copy()

    y.append(4)

    print(x)
    print(y)

    Answer: 
        [1,2,3]
        [1,2,3,4]