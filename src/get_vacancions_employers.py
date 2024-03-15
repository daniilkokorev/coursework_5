from pprint import pprint
import requests
from src.get_empoyers_hh_api import GetemployersHHAPI


class GetVacancionEmployers(GetemployersHHAPI):
    """
    Класс получает список вакансий по каждому работодателю
    """
    def __init__(self, name_employer, page_employer):
        super().__init__(name_employer, page_employer)

    def get_vacancies_from_company(self, id_employer):
        """
        получает список вакансий по id работодателя
        """
        params = {
            'text': self.name_employer,
            'area': 113,
            'per_page': self.page_employer,
            'employer_id': id_employer
        }
        response_vacancies = requests.get('https://api.hh.ru/vacancies/', params).json()['items']
        return response_vacancies

    def get_all_vacancies_from_company(self):
        """
        получает все вакансии одного работодателя
        :return:
        """
        vacancies_list = []
        for vacancie in self.get_employers_list():
            vacancies_list.extend(self.get_vacancies_from_company(vacancie['id_employer']))
        return vacancies_list


if __name__ == '__main__':
    v = GetVacancionEmployers('алабуга', 1)
    pprint(v.get_all_vacancies_from_company())
