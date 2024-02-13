import streamlit as st



st.set_page_config(
    page_title="경기북부병무지청 생계심사 자가진단",
    page_icon=":pickup_truck:",
    initial_sidebar_state="expanded",
)

st.write("# 경기북부병무지청 생계 자가진단")

st.sidebar.success("여긴")

st.markdown(
    """##### 테스트중!

"""
) 

{
    "English": {
        "page1_title": "Diagnosis Assistant",
        "bmc_0": "Let's keep MDxApp free!",
        "bmc_1": "By clicking here:",
        "bmc_2": "Or use this QR code:",
        "page1_header": "Medical Diagnosis Assistant",
        "page1_subheader": "Experience the future of healthcare with our ChatGPT-powered <br>medical diagnostic and symptom checking tool.", 
        "htu_0": "How to use this app:", 
        "htu_1": "Fill out the report below (some symptoms are at least required)", 
        "htu_2": "Check the summary of the report", 
        "htu_3": "Submit the report (None of the provided data are saved or shared)",
        "report_header": "Report",
        "gender": "Gender", 
        "male": "Male",
        "female": "Female", 
        "age": "Age", 
        "pregnant": "Pregnant", 
        "no": "No", 
        "yes": "Yes", 
        "history": "History", 
        "hist_example": "(Example: gone to an outdoor music festival in north america, shared drinks and cigarettes with friends with similar symptoms)",
        "hist_ph": "none", 
        "hist_help": "Enter patient's known background information, including their past medical conditions, medications, family history, lifestyle, and other relevant information that can help in diagnosis and treatment", 
        "symptoms": "Symptoms", 
        "symp_example": "(Example: high-grade fever, lethargy, headache, and abdominal pain for two days)",
        "symp_ph": "none", 
        "symp_help": "List all symptoms indicating the presence of an underlying medical condition", 
        "exam": "Examination findings", 
        "exam_example": "(Example: petechial lesions on the palms of his hands and feet, bug bites)",
        "exam_ph": "none", 
        "exam_help": "List all the information gathered through visual inspection, palpation, percussion, and auscultation during the examination", 
        "lab": "Laboratory test results", 
        "lab_example": "(Example: w/IgE levels > 3000 IU/m)",
        "lab_ph": "none", 
        "lab_help": "List output of tests performed on samples of bodily fluids, tissues, or other substances to help diagnose, monitor, or treat medical conditions. These tests can include blood tests, urine tests, imaging tests, biopsies, and other diagnostic procedures", 
        "summary": "Summary",
        "vissum_patient": "Patient: ",
        "vissum_yrsold": " years old",
        "vissum_pregnancy": "Pregnancy: ", 
        "vissum_history": "History: ",
        "vissum_symp": "Symptoms: ",
        "vissum_exam": "Examination findings: ",  
        "vissum_lab": "Laboratory test results: ", 
        "submit": "SUBMIT", 
        "submit_help": "Submit the report for diagnostic",
        "diagnostic": "Diagnostic", 
        "none": "none", 
        "submit_warning": "Please, enter at least some symptoms before submission.",
        "submit_wait": "Please wait...", 
        "caution": "Caution message",
        "caution_message": "Please be aware that while the app is designed to assist medical decision-making and check symptoms, the final diagnosis should be made by a licensed medical professional. We recommend seeking additional evaluations and opinions before making any treatment decisions.  ",     
        "no_response": "The server does not respond or is overloaded with requests... Try again.", 
        "no_diagnostic": "No diagnostic yet. Please fill out the report and click SUBMIT above.", 
        "language_selection": "Select a language: ", 
        "invest": "Invest in your health, and support our mission in keeping the MDxApp free!"
    }
