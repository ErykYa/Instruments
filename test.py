import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(
        user='instruments',
        password='mn12lk54pgf521',
        host='127.0.0.1',
        port='5432',
        database='instruments'
    )
    cursor = connection.cursor()
    print('Info o servere post')
    print(connection.get_dsn_parameters(), '\n')
    cursor.execute('SELECT version();')
    record = cursor.fetchone()
    print('Vi podklucheni k -', record, '\n')

except (Exception, Error) as error:
    print('Oshibka pri rabote', error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print('Soedinenie zakrito')
