from pprint import pprint

import requests


class GetemployersHHAPI:
    """
    Класс получает список работодателей по API с HH.ru
    """
    def __init__(self):
        self.url_hh = 'https://api.hh.ru/'
        self.employers_list = []

    @property
    def get_employers_hh_api(self):
        """
        получает список работодателей с HH по API
        """
        key_response = {
                        'area': 113,
                        'per_page': 10,
                        'only_with_vacancies': 'True',
                        'sort_by': "by_vacancies_open"}
        response_employers = requests.get(f'{self.url_hh}employers', key_response).json()['items']
        return response_employers

    def get_employers_list(self):
        """
        составляет список работодателей по id
        :return: id работодателя и название компании
        """
        for employer in self.get_employers_hh_api:
            self.employers_list.append({'id_employer': employer['id'],
                                        'name_employer': employer['name']})
        return self.employers_list


if __name__ == '__main__':
    g = GetemployersHHAPI()
    pprint(g.get_employers_list())
