import os
import json
from operator import itemgetter
from datetime import datetime


def opens_preparation_date(FILENAME):

    '''Функция открывает файл json, выбирает словари, содержащие ‘EXECUTED’,
    сортирует операции по дате, возвращает сортированный словарь'''

    path = os.path.join(os.path.dirname(__file__), FILENAME)

    with open(path, 'r') as file:
        operations_json = json.load(file)

        operations_json_cleared = []

        for item in operations_json:
            if item.get('state') == 'EXECUTED':
                operations_json_cleared.append(item)

        operations_json_sorted = sorted(operations_json_cleared, key=itemgetter('date'), reverse=True)
        return operations_json_sorted


def outputs_date(date):

    '''Функция выводит данные из подготовленного словаря по заданному шаблону'''

    final_list = []

    for operation in date[0:5]:

        date_str = operation.get("date")
        date_times = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")

        fromm = operation.get("from", "Открытие счета")
        if fromm == "Открытие счета":
            pass
        else:
            fromm = fromm[:-16] + fromm[-16:-12] + " " + fromm[-12:-10] + "** " + "**** " + fromm[-4:]

        to = operation.get("to")
        to = to[:5] + "**" + to[-4:]

        final_list.append(f'{date_times.strftime("%d.%m.%Y")} {operation.get("description")}\n'
                          f'{fromm} -> {to}\n'
                          f'{operation.get("operationAmount").get("amount")} {operation.get("operationAmount").get("currency").get("name")}\n')

        # print(f'{date_times.strftime("%d.%m.%Y")} {operation.get("description")}')
        # print(f'{fromm} -> {to}')
        # print(f'{operation.get("operationAmount").get("amount")} {operation.get("operationAmount").get("currency").get("name")}')
        # print('')

    return final_list

