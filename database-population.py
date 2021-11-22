import sqlite3

dbase = sqlite3.connect('tp10.db', isolation_level=None)
print('Database opened')
dbase.execute(''' 
                INSERT INTO Students
                (first_name , last_name, matricule, secret)
                VALUES ('Chris', 'Castan', 'CHRCAS01', '123456')
            ''')
dbase.execute(''' 
                INSERT INTO Teachers
                (id, first_name , last_name, secret)
                VALUES ('0001', 'Chris', 'Castan', '123456')
            ''')
dbase.execute(''' 
                INSERT INTO Courses
                (id, name , teacher_id)
                VALUES ('0001', 'Info', '0001')
            ''')
dbase.execute(''' 
                INSERT INTO Sessions
                (id, course_id , session_date)
                VALUES ('0001', '0001', '2021-12-19T01:00:00+01:00')
            ''')
dbase.close()
print('Database Closed')