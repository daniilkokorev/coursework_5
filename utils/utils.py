import psycopg2

from config import config
from src.get_empoyers_hh_api import GetemployersHHAPI
from src.vacanciens_sorty import VacanciensSorty


def create_database(name_db):
    """
    создаёт базу данных PSQL
    :param name_db: имя базы данных
    """
    connect_database = psycopg2.connect(**config(), database="test")
    connect_database.autocommit = True
    cur = connect_database.cursor()
    cur.execute(f"DROP DATABASE IF EXISTS {name_db}")
    cur.execute(f"CREATE DATABASE {name_db}")

    cur.close()
    connect_database.close()


def create_table(name_db):
    """
    создаёт таблицы в базе данных name_db PSQL
    """
    connect_database = psycopg2.connect(**config(), database=name_db)
    try:
        with connect_database:
            with connect_database.cursor() as cur:
                cur.execute('CREATE TABLE employers'
                            '('
                            'employer_id int PRIMARY KEY,'
                            'company_name varchar(255) UNIQUE NOT NULL'
                            ')')
                cur.execute('CREATE TABLE vacanciens'
                            '('
                            'vacancien_id int PRIMARY KEY,'
                            'employer_id int REFERENCES employers(employer_id) NOT NULL,'
                            'name_vacancien varchar(255) NOT NULL,'
                            'salary_from int,'
                            'salary_to int,'
                            'city varchar(255),'
                            'url varchar(255)'
                            ')')
    finally:
        connect_database.close()


def filling_tables_with_data(name_db):
    """
    заполняет таблицы базы данных данными по вакансиям работодателя
    """
    ge = GetemployersHHAPI()
    vs = VacanciensSorty()
    employers_data = ge.get_employers_list()
    vacancies_data = vs.vacancien_sorted()
    connect_database = psycopg2.connect(**config(), database=name_db)
    try:
        with connect_database:
            with connect_database.cursor() as cur:
                for employer_data in employers_data:
                    cur.execute("INSERT INTO employers VALUES (%s, %s)",
                                (employer_data['id_employer'], employer_data['name_employer']))
                for vacancie_data in vacancies_data:
                    cur.execute("INSERT INTO vacanciens VALUES (%s, %s, %s, %s, %s, %s, %s)",
                                (vacancie_data['id_vacancien'], vacancie_data['company'],
                                 vacancie_data['name_vacancion'], vacancie_data['salary_from'],
                                 vacancie_data['salary_to'], vacancie_data['city'], vacancie_data['url']))
    finally:
        connect_database.close()


if __name__ == '__main__':
    filling_tables_with_data("coursework_5")
