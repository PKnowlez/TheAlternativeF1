import streamlit as st
from PIL import Image
import json
import hashlib
import os

DB_FILE = "users.json"

# Helper: Hash a password
def hash_password(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

# Helper: Load/Save Database
def load_users():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_user(username, password):
    users = load_users()
    users[username] = hash_password(password)
    with open(DB_FILE, "w") as f:
        json.dump(users, f)

def Sidebar():
    with st.sidebar:
        logo = Image.open("./Images/The Alternative F1 NEW Logo.png")
        st.image(logo)
        selection = st.selectbox("Page Selection", [
            "Home Page", "Regulations & Settings", "Season 1", 
            "Season 2", "Season 3", "Season 4", 
            "All Time Driver Statistics", "All Time Constructor Statistics", 
            "All Time Race Results"
        ])

        if not st.session_state.get("authenticated"):
            # Tabs for different auth actions
            tab1, tab2, tab3 = st.tabs(["Login", "Sign Up", "Reset"])

            with tab1:
                u = st.text_input("User")
                p = st.text_input("Pass", type="password")
                if st.button("Login"):
                    users = load_users()
                    if u in users and users[u] == hash_password(p):
                        st.session_state.authenticated = True
                        st.session_state.username = u
                        st.rerun()
                    else:
                        st.error("Invalid credentials")

            with tab2:
                new_u = st.text_input("New User")
                new_p = st.text_input("New Pass", type="password")
                if st.button("Register"):
                    users = load_users()
                    if new_u in users:
                        st.warning("User already exists!")
                    else:
                        save_user(new_u, new_p)
                        st.success("Account created! Go to Login tab.")

            with tab3:
                res_u = st.text_input("Username to Reset")
                res_p = st.text_input("New Password", type="password")
                # In a real app, you'd send an email here. 
                # For now, we'll just overwrite if they know the username.
                if st.button("Update Password"):
                    users = load_users()
                    if res_u in users:
                        save_user(res_u, res_p)
                        st.success("Password updated!")
                    else:
                        st.error("User not found.")
        else:
            st.write(f"Logged in as: **{st.session_state.username}**")
            if st.button("Logout"):
                st.session_state.authenticated = False
                st.rerun()

    return selection