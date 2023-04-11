# API handle
# Backend Server

import datetime
import sqlite3
from fastapi import FastAPI
app = FastAPI()
import hashlib
import os

'''   
    # def genSalt():
    #     rand_bytes = secrets.token_bytes(14)

    #     # convert bytes to a binary string
    #     rand_bits = ''.join(f'{byte:08b}' for byte in rand_bytes)

    #     # add 2 more random bits to make 114 bits
    #     rand_bits += secrets.choice(['0', '1'])
    #     rand_bits += secrets.choice(['0', '1'])

    #     # convert the binary string to hex
    #     rand_hex = hex(int(rand_bits, 2))

    #     # remove the '0x' prefix from the hex string and pad with zeros if necessary
    #     rand_str = rand_hex[2:].zfill(29)
    #     return rand_str


    # def genPepper():
    #     rand_bits = ''.join(secrets.choice(['0', '1']) for i in range(2)) # generate a random 2-bit string
    #     return rand_bits


    # def mainGenProcess(userPassword):
    #     st.subheader("Simple Hashing:")
        
    #     # normal hash
    #     simpleHash = str(hash(userPassword))
    #     st.write(simpleHash)
    #     # -----------------------------------------------------------------------------------------
    #     # Hash + Salt
    #     hashSalt = str(userPassword) + str(genSalt())
    #     saltHashing = str(hash(hashSalt))
    #     # print("The string hash + salt value is : " + saltHashing)
    #     st.subheader("Salted Hashing:")
    #     st.write(saltHashing)
    #     # -----------------------------------------------------------------------------------------
    #     # pepper generator (Hash + salt + pepper)
    #     hashPeperval = str(userPassword) + str(genSalt()) + str(genPepper())
    #     pepperHashing = str(hash(hashPeperval))
    #     print("The string hash Pepper is : " + pepperHashing)
    #     st.subheader("Pepper Hashing:")
    #     st.write(pepperHashing)
        
    #     return [simpleHash, saltHashing, pepperHashing]


    #                 # userName = "Atharva"
    #                 # simplehash = "simplehashAedtfb23"
    #                 # saltHash = "simpsaltHashshAedtfb23"
    #                 # pepperHash = "simpepperHashfb23"
'''

def exp6HashSaltPepperSignUP(userPassword):

    # Generate a simple hash of the password
    password = userPassword.encode('utf-8')
    simple_hash = hashlib.sha256(password).hexdigest()

    # Generate a salted password
    salt = os.urandom(16)
    salted_password = hashlib.pbkdf2_hmac('sha256', password, salt, 100000).hex()

    # Generate a peppered password

    # Function to hash a password with salt and pepper
    def hash_password(password, salt, pepper):
        # Concatenate salt and password
        salted_password = salt + password + pepper.encode('utf-8')
        # Hash the salted password using SHA-256
        hashed_password = hashlib.sha256(salted_password).hexdigest()
        return hashed_password

    
    # Example usage
    # password = "password123"
    salt = os.urandom(16)
    pepper = "randompepper"
    peppered_password = hash_password(password, salt, pepper)

    # pepper = b'my_secret_pepper'
    # peppered_password = hashlib.sha256(pepper + password).hexdigest()

    return [simple_hash, salted_password, peppered_password, salt,pepper]




def exp6HashSaltPepperLogin(userName, login_password,formatted_time):
    def read_selected_users_by_id(user_id):
        # Open a    connection to the database
        connref123 = sqlite3.connect('RefSaltPepper.db')
        cref123 = connref123.cursor()

        cref123.execute("SELECT salt, pepper FROM RefSaltPepper WHERE id = ?", (user_id,))
        return cref123.fetchone()
    

    # Open a connection to the database
    conn = sqlite3.connect('label_data.db')
    c = conn.cursor()

    # Retrieve the user's password hashes from the database
    c.execute("SELECT id, simplehash, saltHash, pepperHash FROM label_data WHERE userName = ?", (userName,))
    result = c.fetchone()
    if result is None:
        print('User not found')
        return

    user_id,simple_hash, salted_password, peppered_password = result
    salt,pepper = read_selected_users_by_id(user_id)


    """    # User login process
    # login_password = input('Enter your password: ').encode('utf-8')


    # # Verify the simple hash
    # if simple_hash == hashlib.sha256(login_password.encode('utf-8')).hexdigest():
    #     # print('Login successful!')

    #     # Update lastLogin and loginStatus fields
    #     c.execute("UPDATE label_data SET lastLogin=?, loginStatus=? WHERE id=?", (formatted_time, 'True', user_id))
    #     conn.commit()
    #     return True"""

    # Verify the salted password
    if salted_password == hashlib.pbkdf2_hmac('sha256', login_password.encode('utf-8'), salt, 100000).hex():
        # print('Login successful!')
        # Update lastLogin and loginStatus fields
        c.execute("UPDATE label_data SET lastLogin=?, loginStatus=? WHERE id=?", (formatted_time, 'True', user_id))
        conn.commit()
        return True


        """    # Verify the peppered password
    # if peppered_password == hashlib.sha256(pepper + login_password.encode('utf-8')).hexdigest():
    #     # print('Login successful!')
    #     # Update lastLogin and loginStatus fields
    #     c.execute("UPDATE label_data SET lastLogin=?, loginStatus=? WHERE id=?", (formatted_time, 'True', user_id))
    #     conn.commit()
    #     return True

    # def hash_password(login_password, salt, pepper):
    #     # Concatenate salt and password
    #     salted_password = salt + login_password.encode('utf-8') + pepper.encode('utf-8')
    #     # Hash the salted password using SHA-256
    #     hashed_password = hashlib.sha256(salted_password).hexdigest()
    #     return hashed_password

    # # Function to verify a password against a stored hash
    # def verify_password(login_password, salt, pepper, peppered_password):
    #     # Hash the provided password using the same salt and pepper as the stored hash
    #     hashed_password = hash_password(login_password, salt, pepper)
    #     # Compare the hashed password with the stored hash
    #     return hashed_password == peppered_password
    
    # if verify_password(login_password, salt, pepper, peppered_password):
    #     print("Password is correct!")
    #     c.execute("UPDATE label_data SET lastLogin=?, loginStatus=? WHERE id=?", (formatted_time, 'True', user_id))
    #     conn.commit()"""

    else:
        # Update loginStatus field
        c.execute("UPDATE label_data SET loginStatus=? WHERE id=?", ('False', user_id))
        conn.commit()
        return False


# ------------------------------------------------------------------------



def dbConnect():
    conn = sqlite3.connect('label_data.db')
    c = conn.cursor()

    # Create a table to store the label data if it does not exist
    c.execute('''CREATE TABLE IF NOT EXISTS label_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                userName TEXT,
                simplehash TEXT,
                saltHash TEXT,
                pepperHash TEXT,
                lastLogin TEXT,
                loginStatus TEXT
            )''')
    conn.commit()
    conn.close()


def RefdbConnect():
    conn = sqlite3.connect('refsaltpepper.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS refsaltpepper (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    salt TEXT,
                    pepper TEXT
                )''')
    conn.commit()
    conn.close()


def uploadData(userName, simplehash, saltHash, pepperHash, lastLogin, loginStatus):
    # Create a connection to the database
    conn = sqlite3.connect('label_data.db')
    c = conn.cursor()

    # Insert the label data into the table
    c.execute('INSERT INTO label_data (userName, simplehash, saltHash, pepperHash, lastLogin, loginStatus) VALUES (?, ?, ?, ?, ?, ?)',
              (userName, simplehash, saltHash, pepperHash, lastLogin, loginStatus))
    conn.commit()
    conn.close()


def RefuploadData(salt, pepper):
    # Create a connection to the database
    conn = sqlite3.connect('refsaltpepper.db')
    c = conn.cursor()

    # Insert the label data into the table
    c.execute('INSERT INTO refsaltpepper (salt, pepper) VALUES (?, ?)',
              (salt, pepper))
    conn.commit()
    conn.close()




    """    # Define the label data
    # userName = "Atharva"
    # simplehash = "simplehashAedtfb23"
    # saltHash = "simpsaltHashshAedtfb23"
    # pepperHash = "simpepperHashfb23"

    # Display the label data from the database
    # st.write('Label Data:')
    # for row in c.execute('SELECT * FROM label_data'):
    #     st.write(row)

    # c.execute('DELETE FROM label_data')
    # conn.commit()"""



    # Close the database connection
    conn.close()

# http://localhost:8000/createDB
@app.get("/createDB")
def createDB():
    dbConnect()
    RefdbConnect()
    return {
            "message": "DB created",
        }


# http://localhost:8000/signup/Aditya/talktoaditya@gmail.com/456@MySecretPassword
# http://localhost:8000/signup/Atharva/talktoprashant108@gmail.comm/456@MySecretPassword

@app.get("/signup/{username}/{email}/{password}")
def signup(username: str, email: str, password: str):
    conn = sqlite3.connect('label_data.db')
    c = conn.cursor()

    # Check if a specific userName is present in the label_data table
    # user_name = 'John Doe'
    c.execute("SELECT * FROM label_data WHERE userName=?", (username,))
    result = c.fetchone()

    if result:
        print(f"User {username} found in the database!")
        return {
            "message": f"{username} account already exist, try login",

        }
    else:
        print(f"User {username} not found in the database.")
        data = exp6HashSaltPepperSignUP(password)
        # data = mainGenProcess(password)
        # Get the current timestamp
        current_time = datetime.datetime.now()

        # Format the timestamp
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        loginStatus = False

        uploadData(username, data[0], data[1], data[2],formatted_time,loginStatus)
        RefuploadData(data[3], data[4])
        return {
            "message": "account created",
            "data" : data,
            "time" : formatted_time,
            "loginStatus" : loginStatus,
        }



"""    # return {
    #     "username": username,
    #     "email": email,
    #     "password": password
    # }"""
# http://localhost:8000/login/Atharva/456@MySecretPassword
# http://localhost:8000/login/Aditya/456@MySecretPassword
@app.get("/login/{username}/{password}")
def login(username: str, password: str):
    # Get the current timestamp
    current_time = datetime.datetime.now()

    # Format the timestamp
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    retvar = exp6HashSaltPepperLogin(username, password,formatted_time)
    return {
        "username": username,
        "password": password,
        "login_status" : retvar
    }


@app.get("/hello")
def hello():
    return {"message": "Hello World"}

"""# dbConnect()
# user_input = st.text_input("Enter your name:")
# if st.button("Submit"):
#     response = requests.get("http://localhost:8000/hello")
#     st.write(response.json())"""


