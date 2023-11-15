import json
import requests


def go_test_queries():
    url = 'http://127.0.0.1:8000/get_form'

    with open('test_data.json', 'r') as f:
        all_cases_dict = json.load(f)

    """Отправляем тестовые данные и получаем результат"""
    for case_name, case_values in all_cases_dict.items():
        print(f'\n{case_name}:')
        for single_case in case_values:
            response = requests.post(url=url, params=single_case)
            print(response.text)


if __name__ == '__main__':
    go_test_queries()

