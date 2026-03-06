class TeacherSingleton(type):
    instance = None
    
    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__call__(*args, **kwargs)
        return cls.instance

class Teacher(metaclass=TeacherSingleton):
    
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}'
    
if __name__ == '__main__':
    a = Teacher('a')
    a_copy = Teacher('a')
    b = Teacher('b')
    print(a, a_copy)  # Teacher: a Teacher: a
    assert a == a_copy # True
    assert isinstance(a, Teacher) # True
    assert isinstance(a_copy, Teacher) # True
    assert a == b # True