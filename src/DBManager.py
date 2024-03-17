from pprint import pprint

import psycopg2

from config import config


class DBManager:
    """
    Класс который подключаться к БД PostgreSQL и иметь следующие методы:
    """
    def __init__(self, name_db):
        self.name_db = name_db

    def execute_query(self, query) -> list:
        """
        подключается к базе данных
        :param query:
        :return:
        """
        conn = psycopg2.connect(dbname=self.name_db, **config())
        with conn:
            with conn.cursor() as cur:
                cur.execute(query)
                conclusion = cur.fetchall()
        conn.close()
        return conclusion

    def get_companies_and_vacancies_count(self):
        """
        получает список всех компаний и количество вакансий у каждой компании.
        :return:
        """
        conclusion = self.execute_query('SELECT company_name, '
                                        'COUNT(vacancien_id) AS vacancies_count '
                                        'FROM employers '
                                        'INNER JOIN vacanciens ON employers.employer_id = vacanciens.employer_id '
                                        'GROUP BY company_name')
        return conclusion

    def get_all_vacancies(self):
        """
        получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
        :return:
        """
        conclusion = self.execute_query('SELECT company_name, name_vacancien, ' 
                                        'salary_from, salary_to, url '
                                        'FROM vacanciens '
                                        'LEFT JOIN employers ON '
                                        'vacanciens.employer_id = employers.employer_id')
        return conclusion

    def get_avg_salary(self):
        """
        получает среднюю зарплату по вакансиям.
        :return:
        """
        conclusion = self.execute_query('SELECT name_vacancien, '
                                        'ROUND(AVG(salary_from), 0) AS avg_salary_from, '
                                        'ROUND(AVG(salary_to), 0) AS avg_salary_to '
                                        'FROM vacanciens '
                                        'GROUP BY name_vacancien '
                                        'ORDER BY avg_salary_from DESC')
        return conclusion

    def get_vacancies_with_higher_salary(self):
        """
        получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        :return:
        """
        conclusion = self.execute_query('SELECT name_vacancien, salary_from '
                                        'FROM vacanciens '
                                        'WHERE salary_from > '
                                        '(SELECT AVG(salary_from) FROM vacanciens) '
                                        'ORDER BY salary_from DESC')
        return conclusion

    def get_vacancies_with_keyword(self, keyword):
        """
        получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python.
        :return:
        """
        query = (f"SELECT name_vacancien "
                 f"FROM vacanciens "
                 f"WHERE name_vacancien "
                 f"LIKE '%{keyword}%' "
                 f"GROUP BY name_vacancien")
        result = self.execute_query(query)
        return result


if __name__ == '__main__':
    db = DBManager("coursework_5")
    pprint(db.get_vacancies_with_keyword('manager'))