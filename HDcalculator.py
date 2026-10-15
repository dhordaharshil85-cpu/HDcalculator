import streamlit as st

st.set_page_config(page_title="Calculator", page_icon="🧮")

st.title("🧮 Calculator App")

# Store calculation state
if "expr" not in st.session_state:
    st.session_state.expr = ""

# Display screen
st.text_input("Display", value=st.session_state.expr, key="display", disabled=True)

# Button click handler
def press(val):
    if val == "=":
        try:
            st.session_state.expr = str(eval(st.session_state.expr))
        except Exception:
            st.session_state.expr = "Error"
    elif val == "C":
        st.session_state.expr = ""
    else:
        if st.session_state.expr == "Error":
            st.session_state.expr = ""
        st.session_state.expr += str(val)

# Calculator button grid layout
grid = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in grid:
    cols = st.columns(4)
    for i, btn in enumerate(row):
        cols[i].button(btn, use_container_width=True, on_click=press, args=(btn,))