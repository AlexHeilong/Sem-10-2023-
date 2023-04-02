class Human:
    def __int__(self, name: str, age: int, is_work: bool):
        self.name = name
        self.age = age
        self.is_work = is_work


stone = Human("Max", 38, True)

print(stone.is_work)

'''
class Contact:

    def __init__(self, name: str, phone: str, comment: str ):
        self.name = name
        self.phone = phone
        self.comment = comment

    def __str__(self):
        return f'{self.name}'
'''
