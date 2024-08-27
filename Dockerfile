FROM python:3.9

LABEL maintainer="Alexander Ivanayskiy" python_version="3.9"

# Рабочая папка
WORKDIR /usr/src/app

# Установка библиотек
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Запуск приложения
CMD ["python", "./app.py"]