import pytest

@pytest.fixture
def testdate():
    return [
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
         }
    ]