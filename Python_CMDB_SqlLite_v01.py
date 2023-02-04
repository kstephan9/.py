'''
Python_CMDB_SqlLite_v01.py

'''
import os

import sqlite3
from EmployeeClass import Employee
from CMDBClasses import ci_class

from DefaultItems import DatabaseFolder

#    path_and_file = os.path.join(OutputFolder,filename)

dbname = 'cmdb.db'
#conn = sqlite3.connect(':memory:')

CIClassTablename = 'ci_class'

with sqlite3.connect(os.path.join(DatabaseFolder,dbname)) as conn:
    cursor = conn.cursor()

    DropCommand = 'DROP TABLE ' + CIClassTablename
    cursor.execute(DropCommand) # drop the table
    conn.commit()

    cursor.execute("""CREATE TABLE ci_class (
        ci_class_id INTEGER PRIMARY KEY,
        first text,
        last text,
        pay integer
        )""")

    conn.commit()


    cursor.execute('DROP TABLE employees') # drop the table
    conn.commit()

    cursor.execute("""CREATE TABLE employees (
        first text,
        last text,
        pay integer
        )""")

    conn.commit()

    def insert_ci_class(cicid):
        with conn:
            cursor.execute("INSERT INTO ci_class VALUES (:cicid, :first, :last, :pay)", {'ci_class_id': cicid.first, 'last': cicid.last, 'pay':cicid.pay})

    def insert_emp(emp):
        with conn:
            cursor.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay':emp.pay})

    def get_emps_by_name(lastname):
        cursor.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
        return cursor.fetchall()

    def update_pay(emp, pay):
        with conn:
            cursor.execute("""UPDATE employees SET pay = :pay
                WHERE first = :first AND last  = :last""",
                {'first': emp.first, 'last': emp.last, 'pay': pay})

    def remove_emp(emp):
        with conn:
            cursor.execute("DELETE from employees WHERE first = :first AND last = :last", {'first': emp.first, 'last': emp.last})

    emp_1 = Employee('John', 'Doe', 80000)
    emp_2 = Employee('Jane', 'Doe', 90000)
    emp_3 = Employee('Nora', 'Stephani', 100000)

    cursor.execute("INSERT INTO employees VALUES ('Corey', 'Schafer', 50000)")
    #    cursor.execute("INSERT INTO employees VALUES ('{}', '{}', {})".format(emp_1.first, emp_1.last, emp_1.pay)) #bad practice - SQL injection
    cursor.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
    conn.commit()

    cursor.execute("INSERT INTO ci_class VALUES (1,'Corey', 'Schafer', 50000)")
    #cursor.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
    conn.commit()





    cursor.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay':emp_2.pay})
    conn.commit()

    cursor.execute("INSERT INTO employees VALUES ('Mary', 'Schafer', 70000)")
    conn.commit()

    cursor.execute("SELECT * FROM employees WHERE last=?", ('Schafer',))
    print(cursor.fetchall())

    cursor.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Doe'})
    print(cursor.fetchall())

    cursor.execute("SELECT * FROM ci_class")
    print(cursor.fetchall())

    insert_emp(emp_1)
    insert_emp(emp_2)
    insert_emp(emp_3)


    cursor.execute("SELECT * FROM employees")
    print(cursor.fetchall())

    emps = get_emps_by_name('Stephani')
    print("emps: ",emps)

    update_pay(emp_3, 110000)

    emps = get_emps_by_name('Stephani')
    print("emps2: ",emps)



