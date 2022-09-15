# Указывает Docker использовать официальный образ python 3 с dockerhub в качестве базового образа
FROM python:3
# Устанавливает переменную окружения, которая гарантирует, что вывод из python будет отправлен прямо в терминал без предварительной буферизации
ENV PYTHONUNBUFFERED=1
ENV debug=True
ENV key=django-insecure-e5d*xtgi*z%_7-!\@7$9hkzu$h1xz1\@vez6##re&^qri2npj6
ENV stripe=sk_test_51LhXWLAH1MlYWwwsLCU5zqtPe5jjGlXcS65BccGaxRPv0xPoF22QHYbqVRddBVBF9YAbk4JzAuDECIVY8KdlmjQk00DQIU90nN
# Устанавливает рабочий каталог контейнера — "app"
WORKDIR /app
# Копирует все файлы из нашего локального проекта в контейнер
ADD . /app
# Запускает команду pip install для всех библиотек, перечисленных в requirements.txt
RUN pip install -r requirements.txt

