class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'

class PersonRepository:
    @classmethod
    def save(cls, person:Person):
        print(f'Save the {person} to the database')

if __name__ == '__main__':
    p = Person('John Doe')
    PersonRepository.save(p)