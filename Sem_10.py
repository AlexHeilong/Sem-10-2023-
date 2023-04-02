class Human():
    def __int__(self, name: str, age: int, is_work: bool):
        self.name = name
        self.age = age
        self.is_work = is_work

    def greetings(self):
        print(f'{self.name} говорит "Привет!!!"')

    def good_bye(self, name: str):
        print(f'{self.name} прощается с вами!')

    def __str__(self):
        return f'Это человек с именем {self.name}, возраста {self.age}'



stone = Human('Max', 38, True)
rudolf = Human('Рудольф', 18, True)

print(stone)
print(rudolf)

stone.greetings()
rudolf.greetings()
stone.good_bye('Рудольфом')
rudolf.good_bye('Кириллом')
# print(stone.name)
