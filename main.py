import os
import json

data = {'investor': 'name',
        'borrower': 'name',
        'cash': 'cash',
        'hash': ''
}
def create_data():
    with open('1.json', 'w', encoding='utf8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    create_data()


if __name__ == '__main__':
    main()