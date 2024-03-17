from src.user_interaction import UserInteraction

while True:
    working = UserInteraction("coursework_5")
    working.user_interaction()
    what_now = input('Хотите продолжить?\n'
                     'да/нет\n').lower()
    if what_now != 'да':
        break
