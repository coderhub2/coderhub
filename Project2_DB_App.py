#*Notes*
'''1. we use psycopg2 library which helps python to interact with postgress sql
2.inorder to connect python and the postgress sql we need to use 3rd party library which psycopg2, to download that
go to google>search for psycopg2
3. create a table- create table students (id serial primary key, name text, address text, age int, number text);
inset into table- insert into students (name, address, age, number) values('vinayaka', 'Bengaluru', 25, '8618558976');
update the existing data - update students set name='vinayak' where id=1;

********************************************************************************************************

1. conn = psycopg2.connect = used to establish a connection to postgress sql db "studentdb" and to the python
2. cur = conn.cursor() = so cursor() acts as intermeditiary between DB and the python, it takes command and send it to database to perform sql query, 
                        since cursor() doesnot have connection send the files to DB we provide the connection as conn.cursor so this would create an object we store that in the cur variable 
3. cur.execute = execute has some command, here it says take the command under the execute and send it to the cur object where it sends the command to database to execute sql commands
                  So, the command goes through the cursor (cur) to the database server via the established connection (conn).
4. conn.commit() = used to update the changes made permanently to the database  
5.cconn.close() = closes the connection to the PostgreSQL database and to the python

6. values(%s,%s,%s,%s) = helps to convert the variable values to the sql injection format so that it would execute the command without any error
                         if you need to insert any variable value into sql query, you need to use the %s for safe injection



'''


#importing psycopg2 library used to work on database such as postgresssql
import psycopg2
 
def create_table():
    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="Vinayak27@",host="localhost",port="5432")
    cur = conn.cursor()
    cur.execute("create table students (id serial primary key, name text, address text, age int, number text);")
    print("Table created")
    conn.commit()
    conn.close()

def insert_data():
    name = input("Enter the name:")
    address = input("Enter the Address:")
    age = input("Enter the Age:")
    number = input("Enter the number:")
    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="Vinayak27@",host="localhost",port="5432")
    cur = conn.cursor()
    cur.execute("insert into students (name, address, age, number) values(%s,%s,%s,%s)", (name, address, age, number))
    print("data added into student table")
    conn.commit()
    conn.close()

def updating_existing_data():
    id =  input("Enter the id of student need to be updated:")
    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="Vinayak27@",host="localhost",port="5432")
    cur = conn.cursor()
    fields = {
        "1":("name", "Enter the new name"),
        "2":("age", "Enter the new age"),
        "3":("address", "Enter the new address"),
        "4":("number", "Enter the new number"),
    }
    print("Which field would you like to update?")

    for key in fields:
        print(f"{key}: {fields[key][0]}")
    field_selection = input("Enter the field you want to update")

    if field_selection in fields:
       field_value, message = fields[field_selection]
       new_value = input(message)
       sql = f"UPDATE students SET {field_value} = %s WHERE id = %s"
       cur.execute(sql, (new_value, id))
       print("success")

    else:
        print("invalid choice")

    conn.commit()
    conn.close()

#create_table()
#insert_data()
updating_existing_data()