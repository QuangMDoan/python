from collections import namedtuple
Person = namedtuple('Person', ['name', 'age', 'gender'])

People = [
    Person("An", 20, "F"),
    Person("Quang", 15, "M"),
    Person("Dad", 49, "M"),
    Person("Mom", 50, "F"),
]

teen_names = [person.name for person in People if 13 <= person.age <= 17 ]
print(f"teen_names: {teen_names}")