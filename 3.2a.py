import requests
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(text, to_lang= None):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """
    # C:\Users\USER\PycharmProjects\openfiles\3.2.http.requests\translator\DE.txt
    # .\translator\DE.txt

    params = {
        'key': API_KEY,
        'text': text,
        'lang': 'ru',
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])

def open_file(path_file):
    with open(path_file, 'r', encoding= 'UTF-8') as fi:
        w = translate_it(fi.read())
    with open('result.txt','w',encoding='utf-8') as fl:
        fl.write(w)


# print(translate_it('В настоящее время доступна единственная опция — признак включения в ответ автоматически определенного языка переводимого текста. Этому соответствует значение 1 этого параметра.', 'no'))

if __name__ == '__main__':
    while True:
        a = int(input('Введите язык с которого нужно перевести: 1-испанский, 2- франзуский, 3-немецкий : ' ))
        if a == 1:
            open_file('translator/ES.txt')
        elif a == 2:
            open_file('translator/FR.txt')
        elif a == 3:
            open_file('translator/DE.txt')









