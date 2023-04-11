import streamlit as st
import sqlite3

st.set_page_config(
    # page_title="CSS-Admin Panel",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    # menu_items={
    #     'Get Help': 'https://www.extremelycoolapp.com/help',
    #     'Report a bug': "https://www.extremelycoolapp.com/bug",
    #     'About': "# This is a header. This is an *extremely* cool app!"
    # }
)

# Connect to the database
conn = sqlite3.connect('label_data.db')
c = conn.cursor()

# # Create table if it doesn't exist
# c.execute('''CREATE TABLE IF NOT EXISTS label_data (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 userName TEXT,
#                 simplehash TEXT,
#                 saltHash TEXT,
#                 pepperHash TEXT,
#                 lastLogin TEXT,
#                 loginStatus TEXT
#             )''')
# conn.commit()

# Define functions for CRUD operations
def create_user(userName, simplehash, saltHash, pepperHash):
    c.execute("INSERT INTO label_data (userName, simplehash, saltHash, pepperHash) VALUES (?, ?,?, ?)", (userName, simplehash, saltHash, pepperHash))
    conn.commit()

def read_users():
    c.execute("SELECT * FROM label_data")
    return c.fetchall()

def read_refTable_users():
    conn12 = sqlite3.connect('refsaltpepper.db')
    c12 = conn12.cursor()
    c12.execute('SELECT * FROM refsaltpepper')
    result = c12.fetchall()
    conn12.close()

    return result


def read_selected_users_by_id(user_id):
    c.execute("SELECT * FROM label_data WHERE id = ?", (user_id,))
    return c.fetchone()

def update_user(id, userName, simplehash, saltHash, pepperHash):
    c.execute("UPDATE label_data SET userName = ?, simplehash = ?, saltHash = ?, pepperHash = ? WHERE id = ?", (userName, simplehash, saltHash, pepperHash, id))
    conn.commit()

def delete_user(id):
    c.execute("DELETE FROM label_data WHERE id = ?", (id,))
    conn.commit()

# Streamlit app
st.markdown('''<h1 style="color: aquamarine;">Admin Panel :</h1><hr><h4 style="color: aquamarine;">Hashing with Salt and Pepper</h4><br>''', unsafe_allow_html=True)

options = ['Create', 'Read', 'Update', 'Delete']
selected_option = st.selectbox('Select an option:', options)

# st.write('You selected:', selected_option)

if selected_option == "Create":
    # Create user
    st.header("Create User")
    userName = st.text_input("Username",key="Create1")
    simplehash = st.text_input("Simplehash",key="Create2")
    saltHash = st.text_input("Salt Hash",key="Create3")
    pepperHash = st.text_input("Pepper Hash",key="Create4")

    if st.button("Add User"):
        create_user(userName, simplehash, saltHash, pepperHash)
        st.success("User added successfully!")

if selected_option == "Read":
    # Read users
    st.header("Read Users Database")
    users = read_users()
    if not users:
        st.warning("No users found.")
    else:
        st.table(users)
        mainDB = st.button('main db View')
        if mainDB:
            for user in users:
                st.write(user)

    st.header("Read Ref Users Database")
    refUsers = read_refTable_users()
    if not refUsers:
        st.warning("No Ref users found.")
    else:
        st.table(refUsers)
        refDB = st.button('ref db View')
        if refDB:
            for rUse in refUsers:
                st.write(rUse)


if selected_option == "Update":
    # Update user
    st.header("Update User")
    user_id = st.number_input("User ID", min_value=1,key="Update1")
    userName = st.text_input("Username",key="Update2")
    simplehash = st.text_input("Simplehash",key="Update3")
    saltHash = st.text_input("Salt Hash",key="Update4")
    pepperHash = st.text_input("Pepper Hash",key="Update5")

    if st.button("Update User"):
        update_user(user_id, userName, simplehash, saltHash, pepperHash)
        st.success("User updated successfully!")

if selected_option == "Delete":
    # Delete user
    st.header("Delete User")
    user_id = st.number_input("User ID", min_value=1,key="Delete1")
    st.write(read_selected_users_by_id(user_id))

    if st.button("Delete User"):
        delete_user(user_id)
        st.success("User deleted successfully!")
