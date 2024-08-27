import psycopg2
from psycopg2 import Error

try:
  # Соединение с Postgres сервером
    connection = psycopg2.connect(user="postgres",
                                  password="password",
                                  host="db",
                                  port="5432",
                                  database="corporation")
    cursor = connection.cursor()

  # Удаляем таблицу employees если есть
    query_drop = "DROP TABLE IF EXISTS employees" 
    cursor.execute(query_drop)

  # Создаём таблицу employees
    query_create = "CREATE TABLE IF NOT EXISTS employees (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, age INTEGER NOT NULL, department VARCHAR(255) NULL)"
    cursor.execute(query_create)

  # Заполняем таблицу employees данными 
    query_insert = "INSERT INTO employees (id,name,age,department) VALUES (100,'Boris',45,'hr'), (101,'Polina',22,'enginering'), (102,'Nikol',56,'sales')"  
    cursor.execute(query_insert)

  # Запрос к таблице employees на полную выборку данных
    query_select = "SELECT * FROM employees"
    cursor.execute(query_select)
    result = cursor.fetchall()

  # Выводим полученные данные
    for row in result:
      print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Department: {row[3]}")

  # Закрытие соединения с Postgres сервером
    cursor.close()
        
  # Фиксируем изменения
    connection.commit()

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)

finally:
    if connection is not None:
        connection.close()
