import streamlit as st
from functions import get_todos, write_todos

todos = get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    write_todos(todos)


st.title("My ToDo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        # deletes the todo from the session state dictionary
        del st.session_state[todo]
        # this is used to automatically refresh the checkbox list
        st.experimental_rerun()


st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")

# print("hello")
# st.session_state
