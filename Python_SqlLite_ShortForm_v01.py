import sqlite3
from EmployeeClass import Employee

#conn = sqlite3.connect(':memory:')

with sqlite3.connect('databases\\employee.db') as conn:
    cursor = conn.cursor()
    cursor.execute('DROP TABLE employees') # drop the table
    conn.commit()

    cursor.execute("""CREATE TABLE employees (
        first text,
        last text,
        pay integer
        )""")

    conn.commit()

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



