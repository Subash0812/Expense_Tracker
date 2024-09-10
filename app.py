import streamlit as st
import pandas as pd
import openai

# OpenAI API Key
openai.api_key = "your-openai-api-key"

# Initialize a DataFrame to store expenses
if 'expenses' not in st.session_state:
    st.session_state.expenses = pd.read_csv('Expense.csv')

# Streamlit UI layout
st.title("Expense Tracker")

# Function to add expense
def add_expense(date, category, amount):
    new_expense = pd.DataFrame([[date, category, amount]], columns=["Date", "Category", "Amount"])
    st.session_state.expenses = pd.concat([st.session_state.expenses, new_expense], ignore_index=True)
    st.session_state.expenses.to_csv('Expense.csv',index=False)

# Input form for expenses
st.header("Add a New Expense")
with st.form("expense_form"):
    date = st.date_input("Date")
    category = st.selectbox("Category", ["Travel", "Rent", "Tea & Snacks", "Entertainment", "Food","Other"])
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")
    submit = st.form_submit_button("Add Expense")

    if submit:
        add_expense(date, category, amount)
        st.success("Expense added!")

# Display current expenses
st.subheader("Current Expenses")
if st.button("Show the Data Table"):
    data = pd.read_csv('Expense.csv')
    st.dataframe(data)