import os
import json
import hashlib

def get_hash(filename):
    return hashlib.md5(filename).hexdigest()

def init_blockchain():
    print('init blockchain...', end='\n\n')
    data = {'investor': input('investor name: '),
            'borrower': input('borrower name: '),
            'cash': input('cash: '),
            'hash': ''
    }
    with open(os.path.join(os.curdir, 'blockchain_data', '1.json'), 'w', encoding='utf8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def add_blockchain():
    files = os.listdir(os.path.join(os.curdir, 'blockchain_data'))
    file = sorted(files, key=lambda i: int(i[:-5]))[-1]
    hash_file = open(os.path.join(os.curdir, 'blockchain_data', file), 'rb').read()
    h = get_hash(hash_file)
    data = {'investor': input('investor name: '),
            'borrower': input('borrower name: '),
            'cash': input('cash: '),
            'hash': h
    }
    files = os.listdir(os.path.join(os.curdir, 'blockchain_data'))
    files = sorted(files, key=lambda i: int(i[:-5]))
    new_block = str(int(files[-1][:-5]) + 1)
    with open(os.path.join(os.curdir, 'blockchain_data', f'{new_block}.json'), 'w', encoding='utf8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def check_valid():
    files = os.listdir(os.path.join(os.getcwd(), 'blockchain_data'))
    files = sorted(files, key=lambda i: int(i[:-5]))
    for j in range(1, len(files)):
        cur_hash = json.load(open(os.path.abspath(os.path.join('blockchain_data', files[j])), 'r'))['hash']
        prev_hash_file = open(os.path.join(os.curdir, 'blockchain_data', files[j - 1]), 'rb').read()
        prev_hash = get_hash(prev_hash_file)
        print(f'block <{files[j - 1]}> is valid') if cur_hash == prev_hash else print(f'block <{files[j - 1]}> is corrupt')

def main():
    if not os.path.exists(os.path.join(os.curdir, 'blockchain_data')):
        os.mkdir(os.path.join(os.curdir, 'blockchain_data'))
        init_blockchain()

    while True:
        print("""MENU:
                 1. add contract
                 2. data verification
                 3. exit
              """)
        print()
        choiсe = int(input('your choiсe: '))
        if choiсe == 1:
            add_blockchain()
        elif choiсe == 2:
            check_valid()
        else:
            exit()


if __name__ == '__main__':
    main()