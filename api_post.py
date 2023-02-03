import requests


URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'YTAxYmJhMjEtYWM2My00YWQxLTlhMzYtNDMxMzZhZTU5NzI4OjI2ZjY1MzllZjRmYjQyMGZiZGU0ODEzMmMzMjg4Njlm'
headers_auth = {'Authorization': 'Basic ' + KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)  # Получаем токен
print(auth.status_code)
print('token 👇 👇 👇', '\n', auth.text)

if auth.status_code == 200:  # Если ответ успешный - 200 то мы получем токен
    token = auth.text  # в токен

    while True:  # Запускаем цикл, который будет длиться до тех пор, пока пользователю не надоест и он закроет нашу программу
        word = input('Введите слово для перевода: ')  # Запрашиваем пользовательский ввод
        if word:
            headers_translate = {                                   #  Формируем заголовки
                'Authorization': 'Bearer ' + token
            }
            params = {                                              #  Формируем параметры
                'text': word,
                'srcLang': 1033,
                'dstLang': 1049
            }
            r = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)  # Отправляем в гет запрос
            res = r.json()  # получаем ответ
            try:
                print(res['Translation']['Translation'])  #  Просим у ответа распечатать перевод
            except:
                print('Не найдено варианта для перевода')  # Ловим ошибку

else:
    print('Error!')  # Если не авторизовались распечатаем строку Error!