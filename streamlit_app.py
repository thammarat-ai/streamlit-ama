import streamlit as st
import json

from google.cloud import firestore
from google.cloud.firestore import Client
from google.oauth2 import service_account




@st.cache_resource
def get_db():
    key_dict = json.loads(st.secrets["textkey"])
    creds = service_account.Credentials.from_service_account_info(key_dict)
    db = firestore.Client(credentials=creds, project="streamlit-ama-17e09")
    return db

def post_message(db: Client, name, message, is_private):
    payload = {"name": name, "message": message, "is_private": is_private}
    doc_ref = db.collection("messages").document()
    doc_ref.set(payload)
    return doc_ref.id
    

def main():
    st.title("Thammarat's AMA")
    st.write("Ask me anything!")
    
    db = get_db()
    
    with st.expander("Get all messages"):
        posts_ref = db.collection('messages')
        
        for doc in posts_ref.stream():
            # st.write("This id is: ", doc.id)
            st.write(doc.to_dict())

    
    with st.form("add message"):
        input_name = st.text_input("Your name (Optional)", help="can be anonymous")
        input_message = st.text_area("Your question")
        is_private = st.checkbox("Hide your message from the public board")
        submit = st.form_submit_button("Submit")

        if submit:
            post_message(db, input_name, input_message, is_private)
            st.success("Your message has been sent!")
            st.balloons()
            
if __name__ == "__main__":
    st.set_page_config(page_title="Thammarat's AMA", page_icon=":smile:")
    main()
    