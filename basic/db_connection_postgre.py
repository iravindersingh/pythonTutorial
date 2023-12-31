import psycopg2
import psycopg2.extras # can fetch data in various data types like dictionary

conn = None
cur = None
try:
    conn = psycopg2.connect(host='localhost', dbname='my_db_1', port=5433, user="postgres", password='init@123')

    cur = conn.cursor()

    cur.execute("drop table if exists employee ")

    create_script = '''
        CREATE TABLE IF NOT EXISTS employee (
            id int primary key,
            name varchar(40) NOT NULL,
            salary int,
            dept_id varchar(30))
    '''

    cur.execute(create_script)

    insert_script = 'insert into employee (id, name, salary, dept_id) values (%s, %s, %s, %s)'
    insert_value = [(1, 'rav', 800000, '01'),(2, 'gp', 800000, '01')]
    for i in insert_value:
        cur.execute(insert_script, i)

    cur.execute('SELECT * FROM employee')
    print(cur.fetchall())

    conn.commit()
except Exception as error:
    print(error)
    print(11111)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()