from pprint import pprint

from src.get_vacanciens_employers import GetVacancionEmployers


class VacanciensSorty(GetVacancionEmployers):
    """
    Класс сортирует список вакансий
    """
    def vacancien_sorted(self):
        """
        получаем отсортированный список вакансий
        """
        vacancien_sorty_list = []
        date_formated = None
        for vacancien in self.get_all_vacancies_from_company():
            # проверяет зарплату
            if not vacancien["salary"]:
                salary_from = 0
                salary_to = 0
            else:
                salary_from = vacancien["salary"]["from"] if vacancien["salary"]["from"] else 0
                salary_to = vacancien["salary"]["to"] if vacancien["salary"]["to"] else 0
            vacancien_sorty_list.append({
                "id_vacancien": vacancien["id"],
                "name_vacancion": vacancien["name"],
                "salary_from":  salary_from,
                "salary_to": salary_to,
                "city": vacancien["area"]["name"],
                "company": vacancien["employer"]["id"],
                "url": vacancien["alternate_url"]
            })
        return vacancien_sorty_list


if __name__ == '__main__':
    v = VacanciensSorty()
    pprint(v.vacancien_sorted())
