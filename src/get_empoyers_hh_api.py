from pprint import pprint

import requests


class GetemployersHHAPI:
    """
    Класс получает список работодателей по API с HH.ru
    """
    def __init__(self, name_employer, page_employer):
        self.name_employer = name_employer
        self.page_employer = page_employer
        self.url_hh = 'https://api.hh.ru/'

    @property
    def get_employers_hh_api(self):
        """
        получает список работодателей с HH по API
        """
        key_response = {'text': self.name_employer,
                        'area': 113,
                        'per_page': self.page_employer,
                        'only_with_vacancies': 'True',
                        'sort_by': "by_vacancies_open"}
        response_employers = requests.get(f'{self.url_hh}employers', key_response).json()['items']
        return response_employers

    def get_employers_list(self):
        """
        составляет список работодателей по id
        :return: id работодателя и название компании
        """
        employers_list = []
        for employer in self.get_employers_hh_api:
            employers_list.append({'id_employer': employer['id'],
                                   'name_employer': employer['name']})
        return employers_list


if __name__ == '__main__':
    g = GetemployersHHAPI('develop', 100)
    pprint(g.get_employers_list())
