# ADD
num=10
res = num.__add__(5)
print(res)


# init gia constructor kai __str__ an thelw na exei ena str representation ena object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

person = Person("Alice", 30)
print(person)


# repr
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

person = Person("Alice", 30)
print(repr(person))  # Output: "Person('Alice', 30)"



# getitem na kaneis to object sa lisa na exei index dld
class MyList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

my_list = MyList([1, 2, 3, 4, 5])
print(my_list[2])  # Output: 3


# getItem
class MyList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

my_list = MyList([1, 2, 3, 4, 5])
print(my_list[2])  # Output: 3