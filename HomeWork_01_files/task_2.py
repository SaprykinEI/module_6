def writes_text_to_file(text):
    '''Функция записывает текст в файл'''
    with open('poem.txt', 'wt', encoding='utf-8') as file:
        file.write(text)
    return


writes_text_to_file('Если б мишки были пчелами,\nТо они бы нипочем,\nНикогда и не подумали,\nТак высоко строить дом.')


def reads_the_text():
    '''Функция считывает текст'''
    with open('poem.txt', 'r', encoding='utf-8') as file:
        text_list = file.readlines()
    return text_list


print(''.join(reads_the_text()))