import streamlit as st
from pathlib import Path


st.sidebar.image("profile-pic.png", use_container_width=True,)

st.sidebar.markdown(
    """      
    <div style="text-align: center;">

    <a href="https://www.linkedin.com/in/hanish-khatri-09107418/" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="23" style="margin: 0 5px;" />
    </a>
    <a href="https://github.com/hanishrk" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="23" style="margin: 0 5px;" />
    </a>
    <a href="https://x.com/hrbkharry" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/128/14417/14417709.png" width="23" style="margin: 0 5px;" />
    </a>
    """,
    unsafe_allow_html=True
)


#--General Settimg ---
PAGE_TITLE = "Hanish Khatri"
PAGE_ICON = ":wave:"
Description = """" IT Manager, Assiting Enterprises data-driven Decision-making."""
EMAIL = "Khatrihanish26@gmail.com"

#----Path Setting ----
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "assets"/ "CV.pdf"

#---LOAD CSS,PDF & PROFILE PIC ---
with open (resume_file,"rb") as pdf_file:
  PDFbyte = pdf_file.read()


st.title("H@NISH")
st.write("Website Creator,Python Coding in New innovation ideas in Technology")
st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",

    )
st.write("📫", EMAIL)

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 10 Years expereince extracting actionable insights from AD Usercontrol.
- ✔️ Strong hands on experience and knowledge in Python .
- ✔️ Good understanding of statistical principles and their respective applications.
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python Beginnner.
- 💽 Networking, sVMware, Lan wifi, Hardware Maintained, TCP/IP,
- 💽 Infrastructures, Network Configuration, Laptop 
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**IT Manager | Bonn Nutrients Pvt Ltd**")
st.write("Present")
st.write(
    """
- ► Managed and monitored the operational activities like installation, configuration, maintenance and security.
- ► Hand over specified, configured, installed and maintained local area network hardware, software such as system software.
- ► Work with Users Creation and managed profile configuration, installation with laptops.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**IT Assistant | Sandhu Auto Pvt Ltd**")
st.write("04/2016 - 06/2018")
st.write(
    """
- ► Handling Networking and software with technical expertise in the implementation, Operations and support functions using IT .
- ► Managed all Branches to updates for systems troubleshooting of network problem, Configure router and modem for Local area .
- ► Managed to server system and troubleshoot to network domain, entire local area network. 
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Executive | Tam Media Research Pvt Ltd**")
st.write("04/2016 - 06/2018")
st.write(
    """
- ► Monitoring networks maintain activities and ensuring prompt troubleshoot of network Problems and updates to software to providing.
- ► Diagnostics laptops problem and hardware issue, software issue, network issue, etc.
- ► Specialized in maintain systems and engineers as well as resolving.
"""
)

