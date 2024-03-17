from pprint import pprint

from src.DBManager import DBManager


class UserInteraction(DBManager):
    """
    Класс принимает от пользователя запрос и выводит запрашиваемую информацию
    """
    def __init__(self, name_db):
        super().__init__(name_db)

    def user_interaction(self):
        info_db = DBManager(self.name_db)
        while True:
            user_input = input('Выберите вариант предоставления данных:\n'
                               '1 - Показать список всех компаний и количество вакансий у каждой компании.\n'
                               '2 - Показать список всех вакансий с указанием названия компании, названия '
                               'вакансии, зарплаты и ссылки на вакансию.\n'
                               '3 - Показать среднюю зарплату по вакансиям.\n'
                               '4 - Показать список всех вакансий, у которых зарплата выше средней по всем вакансиям.\n'
                               '5 - Показать список всех вакансий по ключевому слову.\n')
            if user_input in ['1', '2', '3', '4', '5']:
                break
            else:
                print("Не верно!\nПопробуйте ещё раз.\n")
        if user_input == '1':
            pprint(info_db.get_companies_and_vacancies_count())
        elif user_input == '2':
            pprint(info_db.get_avg_salary())
        elif user_input == '3':
            pprint(info_db.get_avg_salary())
        elif user_input == '4':
            pprint(info_db.get_vacancies_with_higher_salary())
        elif user_input == '5':
            user_keyword = input('ВВедите ключевое слово: ')
            pprint(info_db.get_vacancies_with_keyword(user_keyword))


if __name__ == '__main__':
    v = UserInteraction("coursework_5")
    v.user_interaction()

