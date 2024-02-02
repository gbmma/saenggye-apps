import streamlit as st



st.set_page_config(
    page_title="경기북부병무지청 생계심사 자가진단",
    page_icon=":pickup_truck:",
    initial_sidebar_state="expanded",
)

st.write("# 경기북부병무지청 생계 자가진단")

st.sidebar.success("Select a demo above.")

st.markdown(
    """##### 테스트중

"""
)
#OpenAI API key
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

st.set_page_config(
    page_title="Diagnosis_Assistant",
    page_icon="🏥",
    layout="wide"
)

st.markdown("""
  <style>
      .css-zck4sz p {
        font-weight: bold;
        font-size: 18px;
      }
  </style>""", unsafe_allow_html=True)

# Add the language selection dropdown    
if 'lang_tmp' not in st.session_state:
    st.session_state['lang_tmp'] = 'English'

if 'lang_changed' not in st.session_state:
    st.session_state['lang_changed'] = False

if 'lang_select' in st.session_state:
    #st.sidebar.markdown("<h3 style='text-align: center; color: black;'>{}</h3>".format(transl[st.session_state['lang_select']]["language_selection"]), unsafe_allow_html=True)
    lang = st.sidebar.selectbox(transl[st.session_state['lang_select']]["language_selection"], options=list(transl.keys()), key='lang_select')
else:
    #st.sidebar.markdown("<h3 style='text-align: center; color: black;'>{}</h3>".format(transl[st.session_state['lang_tmp']]["language_selection"]), unsafe_allow_html=True)
    lang = st.sidebar.selectbox(transl[st.session_state['lang_tmp']]["language_selection"], options=list(transl.keys()), key='lang_select')

if lang != st.session_state['lang_tmp']:
    st.session_state['lang_tmp'] = lang
    st.session_state['lang_changed'] = True
else:
    st.session_state['lang_changed'] = False

