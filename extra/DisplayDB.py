import streamlit as st
import sqlite3

# Connect to the database
conn = sqlite3.connect('label_data.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              email TEXT)''')
conn.commit()

# Define functions for CRUD operations
def create_user(name, email):
    c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()

def read_users():
    # c.execute("SELECT * FROM users")
    # c.execute("SELECT * FROM users WHERE id = ?", (2,))
    c.execute("SELECT * FROM users WHERE name = ?", ("Atharva",))
    return c.fetchall()

def update_user(id, name, email):
    c.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, id))
    conn.commit()

def delete_user(id):
    c.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()

# Streamlit app
st.title("SQLite CRUD Operations")

# Create user
st.header("Create User")
name = st.text_input("Name",key="1")
email = st.text_input("Email",key="12")
if st.button("Add User"):
    create_user(name, email)
    st.success("User added successfully!")

# Read users
st.header("Read Users")
users = read_users()
if not users:
    st.warning("No users found.")
else:
    for user in users:
        st.write(user)

# Update user
st.header("Update User")
user_id = st.number_input("User ID", min_value=1,key="12345")
name = st.text_input("Name",key="123")
email = st.text_input("Email",key="1234")
if st.button("Update User"):
    update_user(user_id, name, email)
    st.success("User updated successfully!")

# Delete user
st.header("Delete User")
user_id = st.number_input("User ID", min_value=1,key="123567")
if st.button("Delete User"):
    delete_user(user_id)
    st.success("User deleted successfully!")
