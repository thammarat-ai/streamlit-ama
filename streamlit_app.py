import streamlit as st

st.title("Thammarat's AMA")

def send_message(name, message, is_private):
    if is_private:
        st.write("Your message has been sent privately to Thammarat.")
    else:
        st.write("Your message has been sent to Thammarat.")
    


with st.expander("Checklist"):
    st.checkbox("Form to add message")
    st.checkbox("Submit message")
    st.checkbox("Read message")

with st.form("add message"):
    input_name = st.text_input("Your name (Optional)", help="can be anonymous")
    input_message = st.text_area("Your question")
    is_private = st.checkbox("Hide your message from the public board")
    submit = st.form_submit_button("Submit")

    if submit:
        send_message(input_name, input_message, is_private)