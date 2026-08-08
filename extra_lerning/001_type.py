'''
#type()  : type() takes 1 or 3 arguments

name = "bhavna"
print(type(name))  #<class 'str'>

age = 25
print(type(age))   #<class 'int'>


List = [10, 30, 40]
print(type(List))  #<class 'list'>

l = ()
print(type(l))   #<class 'tuple'>

l = (2)
print(type(l))  #<class 'int'>
'''


'''
type() can actually be used to create a class dynamically. This is an important Python concept called dynamic class creation.


2. Creating the same class using type()

type() can take 3 arguments:

type(class_name, parent_classes, attributes)

for the third argument (attributes) of type(), you normally provide a dictionary (mapping).

'''


Student = type("Student", (), {"name":"Bhavna", "age":24})
s1 = Student()
print(s1.name)
print(s1.age)

'''
<class 'type'>
bhavna
25
'''



#is roughly equivalent to:

class Student:
    pass
print(type(Student))  #<class 'type'>


'''
So:

Student
   ↓
is an object
   ↓
created by
   ↓
type

That's why type is sometimes called the metaclass of classes.

type()
  ↓
normally tells you the type of an object

type(obj)

BUT

type(name, bases, attributes)
  ↓
creates a new class
'''





