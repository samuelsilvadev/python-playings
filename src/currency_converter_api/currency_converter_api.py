import requests
import inquirer

ENDPOINT = 'https://economia.awesomeapi.com.br/json/last'

available_currencies = ['USD', 'EUR', 'BTC']

questions = [
    inquirer.Checkbox(
        'base_currency',
        message='Select the base currency',
        choices=available_currencies
    ),
    inquirer.Checkbox(
        'target_currency',
        message='Select the target currency',
        choices=available_currencies
    ),
    inquirer.Text(
        'quantity',
        message='Type the amount you want to convert'
    )
]


answers = inquirer.prompt(questions)

is_base_currency_answer_empty = len(
    answers['base_currency']) == 0

is_target_currency_answer_empty = len(
    answers['target_currency']) == 0

if (is_base_currency_answer_empty):
    print('\nBase currency cannot be empty.')
    exit()

if (is_target_currency_answer_empty):
    print('\nTarget currency cannot be empty.')
    exit()

base_currency = answers['base_currency'][0]
target_currency = answers['target_currency'][0]
quantity = float(answers['quantity'])

currencies = f'{base_currency}-{target_currency}'
glued_currencies = currencies.replace('-', '')

response = requests.get(f'{ENDPOINT}/{currencies}')
parsed_response = response.json()

if ('status' in parsed_response and parsed_response['status'] == 404):
    print('\nThe API does not support this combination of currencies. Try again.')
    exit()

bid = parsed_response[glued_currencies]['bid']

result = quantity * float(bid)

print(f'You will get: {result:.2f}')
