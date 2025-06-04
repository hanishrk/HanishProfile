import streamlit as st 

st.set_page_config (
    page_title="multipage app",
    page_icon="🚀"
)
st.title("main page")
st.sidebar.success ("select a page above")


#st.sidebar.header("this is sidebar")

#st.set_page_config (
   # page_title="multipage app",
    #page_icon="🚀"
#)

#st.sidebar.success ("select a page above")
# Sidebar title 
#st.sidebar.title("Connect with Me")

# UserName = st.text_input ("Enter your Name ")
# Lastname = st.text_input ("Enter your LastName")
# Adr = st.text_area ("Enter your text Area :")
# Classdat = st.selectbox ("Enter YOur Class :" ,(1,2,3,4,5,6))

# Button =st.button("Done")
# if Button :
#     st.markdown (f"""
# Name : {UserName} 
# last: {Lastname}
# adrress:{Adr}
# calss : {Classdat}""")
    


# # Apply custom CSS for background color
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-color: #e3e8e8  /* light blue background */
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )


# # Custom CSS to change sidebar background color
# st.markdown(
#     """
#     <style>
#     [data-testid="stSidebar"] {
#         background-color: #e6f2ff;  /* Light blue */
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
