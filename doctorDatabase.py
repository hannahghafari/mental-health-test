import sqlite3

def  create_table():
    conn=sqlite3.connect('Test.db')
    cursor=conn.cursor()

    cursor.execute('''
       create table if not exists Doctor (
                   id integer primary key,
                   username text,
                   password text)''')
    conn.commit()
    conn.close()




# اینجا باید تابع هایی که تعریف میکنیم اینجوری باشه که بیاد اطلاعات نشون بده و بشه فیلتر کرد


def fetch_doctors():
    conn=sqlite3.connect('Test.db')
    cursor=conn.cursor()
    
    cursor.execute('select * from Doctor')
    doctor=cursor.fetchall()
    conn.close()
    return doctor



def insert_doctor(p):
    conn = sqlite3.connect('Test.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Doctor (id, username,password) VALUES (?, ?, ?)",(p))
    conn.commit()
    conn.close()



# a=(1001,"aminfarsadaf","sadaf111")
# b=(1002,"gholamisaeed","123456")
# c=(1003,"arezorahaii","3948a")
# d=(1004,"abdileila","9323a")
# e=(1005,"godarzinafis","nafis2930")
# f=(1006,"poenrazi","pone2000")
# g=(1007,"maryamsadeghi","maryam1992")
# h=(1008,"hoseinhaghi","ho3ein1032")
# i=(1009,"amirbagheri","amirrima21")
# a=(1010,"gholamali","1234")

# insert_doctor(a)
# insert_doctor(b)
# insert_doctor(c)
# insert_doctor(d)
# insert_doctor(e)
# insert_doctor(f)
# insert_doctor(g)
# insert_doctor(h)
# insert_doctor(i)



def get_id():
    conn = sqlite3.connect('Test.db')
    cursor = conn.cursor()

    # Check if there is any data in the database
    cursor.execute('SELECT MAX(id) FROM Doctor')
    result = cursor.fetchone()[0]

    if result is None:
        # If there is no data in the database, return 1
        res=1
    else:
        # If there is data in the database, return the maximum ID
        res=result+1
    conn.close()
    return res
