

from src.utils import opens_preparation_date, outputs_date


def test_opens_preparation_date():
    assert opens_preparation_date('testdate.json') == [
        {'id': 207126257,
         'state': 'EXECUTED',
         'date': '2019-07-15T11:47:40.496961',
         'operationAmount': {'amount': '92688.46',
                             'currency': {'name': 'USD',
                                          'code': 'USD'}
                             },
         'description': 'Открытие вклада',
         'to': 'Счет 35737585785074382265'
         },

        {'id': 667307132, 'state': 'EXECUTED',
         'date': '2019-07-13T18:51:29.313309',
         'operationAmount': {'amount': '97853.86',
                             'currency': {'name': 'руб.',
                                          'code': 'RUB'}
                             },
         'description': 'Перевод с карты на счет',
         'from': 'Maestro 1308795367077170',
         'to': 'Счет 96527012349577388612'
         },

        {'id': 893507143,
         'state': 'EXECUTED',
         'date': '2018-02-03T07:16:28.366141',
         'operationAmount': {'amount': '90297.21',
                             'currency': {'name': 'руб.',
                                          'code': 'RUB'}
                             },
         'description': 'Открытие вклада',
         'to': 'Счет 37653295304860108767'
         }
    ]



def test_outputs_date(testdate):
    assert outputs_date(testdate) == ['15.07.2019 Открытие вклада\nОткрытие счета -> Счет **2265\n92688.46 USD\n',
 '13.07.2019 Перевод с карты на счет\n'
 'Maestro 1308 79** **** 7170 -> Счет **8612\n'
 '97853.86 руб.\n']