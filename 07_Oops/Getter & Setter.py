
# To understand the concept of getter and setter for encapsulation

class Person:
    def __init__(self, name, age):
        self._name = name  # private attribute
        self._age = age    # private attribute

    # Getter for 'name'
    @property
    def name(self):
        return self._name

    # Setter for 'name'
    @name.setter
    def name(self, value):
        if len(value) > 0:
            self._name = value
        else:
            print("Name cannot be empty!")

    # Getter for 'age'
    @property
    def age(self):
        return self._age

    # Setter for 'age'
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            print("Age cannot be negative!")

# Example usage:
person = Person("Alice", 30)

# Using getters to access the values
print(person.name)  # Output: Alice
print(person.age)   # Output: 30

# Using setters to modify the values
person.name = "Bob"
person.age = 35

print(person.name)  # Output: Bob
print(person.age)   # Output: 35

# Invalid setter call
person.age = -5  # Output: Age cannot be negative!
