import json
import os
import hashlib


def getHash(filename):
    block_dir = os.curdir + '/blockchains/'
    file = open(block_dir + filename, 'rb').read()
    return hashlib.md5(file).hexdigest()

def helpHash():
    """Данная функция возвращает последнее имя файла"""
    # Получили список из файлов в директории
    block_dir = os.curdir + '/blockchains/'
    files = os.listdir(block_dir)
    # Приобразовали элементы списка в числа и отсортировали
    files = sorted([int(i) for i in files])
    # Извлекаем последнее имя файла
    try:
        lastName = files[-1]

    except:
        lastName = 0
        return lastName
    return str(lastName)




def checkIntegrity():
    """Проверка хэша
        1) Считываем хэш предыдущего блока
        2) Заного вычисляем Хэш предыдущего блока
        3) Сравниваем"""
    result = []
    block_dir = os.curdir + '/blockchains/'
    files = os.listdir(block_dir)
    # Приобразовали элементы списка в числа и отсортировали
    files = sorted([int(i) for i in files])

    for file in files[1:]:
        h = json.load(open(block_dir + str(file)))['hash']
        prevFile = str(file - 1)
        actualHash = getHash(prevFile)

        if h == actualHash:
            res = 'Ok'
        else:
            res = 'Currupted'

        result.append({'block': prevFile, 'result': res})

    return result

def nameFile():
    """Получение имени файлов в дериктории
        На основании посленего файла происходит генерация имени для нового файла
    """

    # Получили список из файлов в директории
    block_dir = os.curdir + '/blockchains/'
    files = os.listdir(block_dir)
    # Приобразовали элементы списка в числа и отсортировали
    files = sorted([int(i) for i in files])
    # Извлекаем последнее имя файла
    try:
        lastName = files[-1]
    except:
        finalName = 1
        return finalName
    # Присваиваем имя файла следующему файлу
    finalName = lastName + 1
    return str(finalName)





def write_block(name, amount, to_whom, hash=''):

    block_dir = os.curdir + '/blockchains/'
    prevHash = getHash(helpHash())

    data = {'name': name,
            'amount': amount,
            'to_whom': to_whom,
            'hash': prevHash}

    with open(block_dir+str(nameFile()), 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)



def main():
    test = str(input('Создать блок(create) или проверить целостность(check)? -> '))
    try:
        if test == 'create':
            name = str(input('Введите свое имя: '))
            amount = int(input('Введите сумму передачи: '))
            to_whom = str(input('Кому: '))
            write_block(name, amount, to_whom)
        elif test == 'check':
            checkIntegrity()
        else:
            exit(0)
    except:
        print('Ошибка')
        exit(0)


if __name__ == '__main__':
    main()