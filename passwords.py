import pymysql.cursors, hashlib, uuid                      # UUID is a “Universally Unique ID”

# Connect to the database

connection = pymysql.connect(host='mrbartucz.com',

                             user='sc3460ze',

                             password='Jas4863009*',

                             db='sc3460ze_uni',

                             charset='utf8mb4',

                             cursorclass=pymysql.cursors.DictCursor)

try:

    with connection.cursor() as cursor:
        
        password = input("What is your password?") 

        # this creates a brand new guaranteed unique salt every time you run it
        salt = uuid.uuid4().hex 

        print ("password + salt is: " + password + str(salt))

        # this is an open-source method to ONE-WAY hash a password
        hashed_password = hashlib.sha512((password + salt).encode('utf-8')).hexdigest()

        print ("the hashed password is: ", hashed_password)

        # Select all Students
        #sql = "SELECT * from sc3460ze_students"
        # Select student by searching with first name
        #sql = "SELECT * from sc3460ze_students where First_Name = '"+input_user+"'"
        #sql = "SELECT * from Students WHERE Name LIKE '%s'"
        #cursor.execute(sql, input_name)

        sql = "INSERT INTO sc3460ze_HashedPassword (hashed_password) VALUES (%s)"
                
        cursor.execute(sql, hashed_password)
              
        # execute the SQL command
        connection.commit();
        
        # get the results

        #for result in cursor:

            #print (result)

        # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
        # So you must commit to save your changes. 
        # connection.commit()  

finally:

    connection.close()
    
password1=input ("Verify Password")

if password1 == password:
    print ("Password Correct")
    
else:
    print ("Password Incorrect")

