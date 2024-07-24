import streamlit as st  # streamlit library is used to create web apps
import function as fun

# everything is put in order as of how they're shown on the app

todos = fun.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n" # session_state object type
    todos.append(todo)
    fun.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app will increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)  # key=todo checks which object is being picked
    if checkbox:
        todos.pop(index)
        fun.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")

