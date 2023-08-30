import mysql.connector
from mysql.connector import Error

class functions():

  # Get username and password for a selected database
  def __init__(self, user, pwd, db):
  
    self.user = user
    self.pwd = pwd
    self.db = db
    
  # Add access timestamp to history
  def add_to_history(self, ID, time):
    
    check = False # Use for authorization
    
    try:
      # Establish connection to MySQL server
      connection = mysql.connector.connect(host = 'localhost',
                                           database = self.db,
                                           user = self.user,
                                           password = self.pwd)
      
      # If connected
      if connection.is_connected():
        # Create cursor to run SQL code
        cursor = connection.cursor()
          
        # Check ID
        cursor.execute("""select Type, Status from Users where ID = (%s)""", (ID,))
        result = cursor.fetchone()
                
        # If ID exists
        if result != None:
          # If ID belongs to an authorized personnel
          if result[0] != "Unauthorized" and result[1] == "Active":  
            # Insert ID and timestamp into Entry table
            cursor.execute("""insert into Entry values (%s, %s)""", (ID, time,))
            connection.commit()
            check = True
          
    except Error as e:
      print(e)

    finally:
      # Close connection
      if connection.is_connected():
        cursor.close()
        connection.close()
          
    return check

  # Check if an ID belongs to an Admin
  def check_admin(self, ID):
    
    check = False # Use for authorization
    
    try:
      # Establish connection to MySQL server
      connection = mysql.connector.connect(host = 'localhost',
                                           database = self.db,
                                           user = self.user,
                                           password = self.pwd)
      
      # If connected
      if connection.is_connected():
        # Create cursor to run SQL code
        cursor = connection.cursor()
          
        # Check ID
        cursor.execute("""select Type, Status from Users where ID = (%s)""", (ID,))
        result = cursor.fetchone()
                
        # If ID exists
        if result != None:
          # If ID belongs to an Admin
          if result[0] == "Admin" and result[1] == "Active": 
            check = True
          
    except Error as e:
      print(e)

    finally:
      # Close connection
      if connection.is_connected():
        cursor.close()
        connection.close()
          
    return check

  # Show all access history
  def show_history(self):
  
    hist_list = []
  
    try:
      # Establish connection to MySQL server
      connection = mysql.connector.connect(host = 'localhost',
                                           database = self.db,
                                           user = self.user,
                                           password = self.pwd)
      
      # If connected
      if connection.is_connected():
        # Create cursor to run SQL code
        cursor = connection.cursor()
          
        # Get entry history
        cursor.execute("""select * from Entry""")
        hist_list = cursor.fetchall()
                          
    except Error as e:
      print(e)

    finally:
      # Close connection
      if connection.is_connected():
        cursor.close()
        connection.close()
        
    return hist_list
    
  # Show access history filtered by date
  def show_history_by_date(self, date):
  
    date = str(date[0]) + '-' + str(date[1]) + '-' + str(date[2]) + '%'
    hist_list = []
  
    try:
      # Establish connection to MySQL server
      connection = mysql.connector.connect(host = 'localhost',
                                           database = self.db,
                                           user = self.user,
                                           password = self.pwd)
      
      # If connected
      if connection.is_connected():
        # Create cursor to run SQL code
        cursor = connection.cursor()
          
        # Get entry history
        cursor.execute("""select * from Entry where Date(Time) = (%s);""", (date,))
        hist_list = cursor.fetchall()
                          
    except Error as e:
      print(e)

    finally:
      # Close connection
      if connection.is_connected():
        cursor.close()
        connection.close()
        
    return hist_list
    
  # Show student access history
  def show_student_only(self):
  
    hist_list = []
  
    try:
      # Establish connection to MySQL server
      connection = mysql.connector.connect(host = 'localhost',
                                           database = self.db,
                                           user = self.user,
                                           password = self.pwd)
      
      # If connected
      if connection.is_connected():
        # Create cursor to run SQL code
        cursor = connection.cursor()
          
        # Get entry history
        cursor.execute("""select Entry.ID, Entry.Time from Entry inner join Users ON Entry.ID = Users.ID and Users.Type = "Student";""")
        hist_list = cursor.fetchall()
                          
    except Error as e:
      print(e)

    finally:
      # Close connection
      if connection.is_connected():
        cursor.close()
        connection.close()
        
    return hist_list  
    
  # Show student access history with specific ID
  def show_student_match(self, ID):
  
    hist_list = []
  
    try:
      # Establish connection to MySQL server
      connection = mysql.connector.connect(host = 'localhost',
                                           database = self.db,
                                           user = self.user,
                                           password = self.pwd)
      
      # If connected
      if connection.is_connected():
        # Create cursor to run SQL code
        cursor = connection.cursor()
          
        # Get entry history
        cursor.execute("""select Entry.ID, Entry.Time from Entry inner join Users ON Entry.ID = Users.ID and Entry.ID = %s and Users.Type = "Student";""", (ID,))
        hist_list = cursor.fetchall()
                          
    except Error as e:
      print(e)

    finally:
      # Close connection
      if connection.is_connected():
        cursor.close()
        connection.close()
        
    return hist_list  
    
  # Show access history filtered by time range
  def show_history_by_time(self, sTime, eTime):
          
    hist_list = []
  
    try:
      # Establish connection to MySQL server
      connection = mysql.connector.connect(host = 'localhost',
                                           database = self.db,
                                           user = self.user,
                                           password = self.pwd)
      
      # If connected
      if connection.is_connected():
        # Create cursor to run SQL code
        cursor = connection.cursor()
          
        # Get entry history
        cursor.execute("""select * from Entry where Time(Time) between (%s) and (%s) ;""", (sTime, eTime,))
        hist_list = cursor.fetchall()
                          
    except Error as e:
      print(e)

    finally:
      # Close connection
      if connection.is_connected():
        cursor.close()
        connection.close()
        
    return hist_list
    
  # Show all users  
  def show_user(self):
  
    user_list = []
  
    try:
      # Establish connection to MySQL server
      connection = mysql.connector.connect(host = 'localhost',
                                           database = self.db,
                                           user = self.user,
                                           password = self.pwd)
      
      # If connected
      if connection.is_connected():
        # Create cursor to run SQL code
        cursor = connection.cursor()
          
        # Get user list
        cursor.execute("""select * from Users""")
        user_list = cursor.fetchall()
                          
    except Error as e:
      print(e)

    finally:
      # Close connection
      if connection.is_connected():
        cursor.close()
        connection.close()
        
    return user_list
    
  # Activate & Reactivate User
  def activate(self, ID):
  
    check = 0 # Check if status has being changed
  
    try:
      # Establish connection to MySQL server
      connection = mysql.connector.connect(host = 'localhost',
                                           database = self.db,
                                           user = self.user,
                                           password = self.pwd)
      
      # If connected
      if connection.is_connected():
        # Create cursor to run SQL code
        cursor = connection.cursor()
          
        # Get user list
        cursor.execute("""select Status from Users where ID = (%s)""", (ID,))
        result = cursor.fetchone()
                
        # If ID exists
        if result != None:
          # If ID is inactive or suspend
          if result[0] == "Suspended": 
            cursor.execute("""update Users set Status = 'Active' where ID = (%s)""", (ID,))
            connection.commit()
            check = 1
        
        else:
          check = 2
                          
    except Error as e:
      print(e)

    finally:
      # Close connection
      if connection.is_connected():
        cursor.close()
        connection.close()
        
    return check
    
  # Suspend User
  def suspend(self, ID):
  
    check = 0 # Check if status has being changed
  
    try:
      # Establish connection to MySQL server
      connection = mysql.connector.connect(host = 'localhost',
                                           database = self.db,
                                           user = self.user,
                                           password = self.pwd)
      
      # If connected
      if connection.is_connected():
        # Create cursor to run SQL code
        cursor = connection.cursor()
          
        # Get user list
        cursor.execute("""select Status from Users where ID = (%s)""", (ID,))
        result = cursor.fetchone()
                
        # If ID exists
        if result != None:
          # If ID is active
          if result[0] == "Active": 
            cursor.execute("""update Users set Status = 'Suspended' where ID = (%s)""", (ID,))
            connection.commit()
            check = 1
        
        else:
          check = 2
                          
    except Error as e:
      print(e)

    finally:
      # Close connection
      if connection.is_connected():
        cursor.close()
        connection.close()
        
    return check
