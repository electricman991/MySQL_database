import mysql.connector
from mysql.connector import errorcode
from csv import reader

try:
  # Open connection.
    cnx = mysql.connector.connect( user=''
                               , password=''
                               , host='127.0.0.1'
                               , database=''
                               , auth_plugin='mysql_native_password')
  # Create cursor.
    cursor = cnx.cursor()
 
  # Create statements to query database

    choice = None
    while choice != "9":
        print("1) Display Employees")
        print("2) Add Employee")
        print("3) Display Employee Address")
        print("4) Choose Employee Id")
        print("5) Update Employee Pay")
        print("6) Choose CSV file name: ")
        print("7) Show Total Salary and Hours")
        print("8) Delete Employee from Database")
        print("9) Quit")
        choice = input("> ")
        print()
    
        if choice == '1':
            cursor.execute('SELECT * FROM workers')
            result = cursor.fetchall()
            for row in result:
                print(row, '\n')

        elif choice == '2':
            worker_id = int(input('Id: '))
            name = input('Name: ')
            address = input('Address: ')
            salary = int(input('Salary: '))
            values = (worker_id, name, address, salary)
            cursor.execute('INSERT INTO workers (workers_id, name, address, salary)'
                           'VALUES '
                           '(%s,%s,%s,%s)', values)
            

        elif choice == '3':
            cursor.execute('SELECT address FROM workers')
            result = cursor.fetchall()
            for row in result:
                print(row, '\n')

        elif choice == '4':
            worker = input('Choose worker id to see information: ')

            cursor.execute(f'SELECT * FROM workers WHERE workers_id = {worker} \n')
            results = cursor.fetchall()
            print(f'\n{results[0]}\n')

        elif choice == '5':
          employee = input('Choose employee id: ')
          salary = input('Set new salary: ')
          cursor.execute('UPDATE workers '
                          f'SET salary = {salary} '
                          f'WHERE workers_id = {employee}')
          print(f'\nSalary Information has been updated for {employee}\n')

        elif choice == '6':
          file = input('Input CSV file name: ')
          with open(f'{file}', 'r') as read_obj:
            csv_reader = reader(read_obj)
            next(csv_reader)
            stmt = ("INSERT INTO workers "
            "(workers_id, name, address, salary) "
            "VALUES "
            "(%s, %s, %s, %s)")

            stmt2 = ("INSERT INTO hours_worked "
                     "(hours_worked_id, weekly_hours, workers_id) "
                     "VALUES "
                     "(%s, %s,%s)")
          
            for row in csv_reader:
              
              second_values = [row[0], row[1], row[2], row[3]]
              cursor.execute(stmt, second_values)
                
              first_values = [row[5], row[6], row[4]]
              cursor.execute(stmt2, first_values)
                
        
        elif choice == '7':
          cursor.execute('SELECT SUM(workers.salary) AS total_salary, SUM(hours_worked.weekly_hours) AS total_hours '
                         'FROM workers '
                         'INNER JOIN hours_worked ON workers.workers_id=hours_worked.hours_worked_id')
          print('{:>10} {:>10} \n'.format('Total_Salary  ', 'Total_Hours'))
          result=cursor.fetchall()
          print('{:>10} {:>10}'.format(result[0][0], result[0][1]))

        elif choice == '8':
          choice = input('Choose worker id to delete: ')
          cursor.execute(f'DELETE from workers where workers_id = {choice} ')
          print(f'\nEmployee with worker id {choice} has been deleted\n')
         
    # Commit the writes.
    cnx.commit()
 
    #close the connection to the database.
    cursor.close()
 
# Handle exception and close connection.
except mysql.connector.Error as e:
  if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif e.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print("Error code:", e.errno)        # error number
    print("SQLSTATE value:", e.sqlstate) # SQLSTATE value
    print("Error message:", e.msg)       # error message
 
# Close the connection when the try block completes.
else:
  cnx.close()