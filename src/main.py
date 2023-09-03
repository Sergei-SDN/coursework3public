FILENAME = '../../coursework3/operations.json'

from utils import outputs_date, opens_preparation_date

operations = opens_preparation_date(FILENAME)

for operation in outputs_date(operations):
    print(operation)