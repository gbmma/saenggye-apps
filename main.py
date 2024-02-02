import streamlit as st



st.set_page_config(
    page_title="경기북부병무지청 생계심사 자가진단",
    page_icon=":pickup_truck:",
    initial_sidebar_state="expanded",
)

st.write("# 경기북부병무지청 생계 자가진단")

st.sidebar.success("Select a demo above.")

st.markdown(
    """##### 테스트중2

"""
)
openai.api_key = st.secrets["openai_api_key"]

def openai_create(prompt):

    response = openai.ChatCompletion.create(
    model=st.secrets["openai_api_model"],
    messages=[{"role": "system", "content": st.secrets["prompt_canvas"]["prompt_system"]}, 
              {"role": "user", "content": prompt}], 
    temperature=float(st.secrets["openai_api_temp"]), 
    max_tokens=int(st.secrets["openai_api_maxtok"]),
    frequency_penalty=int(st.secrets["openai_api_freqp"]),
    presence_penalty=float(st.secrets["openai_api_presp"]), 
    stop = None
    )

    return response['choices'][0]['message']['content']
