import sqlite3
import pandas as pd
def  create_table():
    conn=sqlite3.connect('Test.db')
    cursor=conn.cursor()

    cursor.execute('''
       create table if not exists Patient (
                   id integer primary key,
                   test_name text,
                   first_name text,
                   last_name text,
                   age text,
                   gender text,
                   race text,
                   job_info text,
                   therapy_session text,
                   mental_health_issue text,
                   physical_health_issue text,
                   date text,
                   phone_number text,
                   email text,
                   result text)''')
    conn.commit()
    conn.close()



def insert_patient(id, test_name, first_name, last_name, age, gender, race, job_info, therapy_session, mental_health_issue, physical_health_issue, date, phone_number, email, result):
    conn = sqlite3.connect('Test.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Patient (id, test_name, first_name, last_name, age, gender, race, job_info, therapy_session, mental_health_issue, physical_health_issue, date, phone_number, email, result) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (id, test_name, first_name, last_name, age, gender, race, job_info, therapy_session, mental_health_issue, physical_health_issue, date, phone_number, email, result))
    conn.commit()
    conn.close()

def search_patient(test_name,gender,race):
    conn = sqlite3.connect('Test.db')
    cursor = conn.cursor()
    cursor.execute("select id,first_name,last_name from Patient Where test_name= ? and gender= ? and race= ?",(test_name,gender,race))
    patientinfo=cursor.fetchall()
    conn.close()
    return patientinfo

# ans=search_patient('ADHD','female','Asian')
# chart=pd.DataFrame(ans)
# # chart=chart.rename_axis(columns="hi")
# # chart = chart.rename(columns={"0": "ID"})


# # chart=chart.rename_axis(None, axis =1)
# print(chart)
def fetch_SPpatient(id,fname,lname):
    conn = sqlite3.connect('Test.db')
    cursor = conn.cursor()
    cursor.execute("select * from Patient Where id= ? and first_name= ? and last_name= ?",(id,fname,lname))
    patientinfo=cursor.fetchall()
    conn.close()
    return patientinfo

def delete_patient(id,fname,lname):
    conn = sqlite3.connect('Test.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Patient where id= ? and first_name= ? and last_name= ?",(id,fname,lname))
    conn.commit()
    conn.close()


def fetch_patient():
    conn=sqlite3.connect('Test.db')
    cursor=conn.cursor()
    cursor.execute('select * from Patient')
    patient=cursor.fetchall()
    conn.close()
    return patient

# x= fetch_patient()
# print(x)

def get_id():
    conn = sqlite3.connect('Test.db')
    cursor = conn.cursor()

    # Check if there is any data in the database
    cursor.execute('SELECT MAX(id) FROM Patient')
    result = cursor.fetchone()[0]

    if result is None:
        # If there is no data in the database, return 1
        res=1
    else:
        # If there is data in the database, return the maximum ID
        res=result+1
    conn.close()
    return res
