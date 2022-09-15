# Rishat
### Для запуска проекта на локальной машине:
Установка виртуального окружения и запуск:
```shell
$ python -m venv venv
$ . venv/scripts/activate
```
Установка файла зависимостей:
```shell
$ pip install -r requirements.txt
```
Запуск проекта:
```shell
$ python manage.py runserver
```
Проект подготовлен к запуску на Heroku.com файл Procfile.
Для работы проекта необходим файл .env со следующим содержимым:
- key
- debug
- stripe
