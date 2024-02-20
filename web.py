import streamlit as st
import functions as fn


todos = fn.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"  # get the new todo and add to the list
    todos.append(todo)
    fn.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase my productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fn.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a new todo:", placeholder="Add new todo...",
              on_change=add_todo, key = 'new_todo')