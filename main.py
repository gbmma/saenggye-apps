import streamlit as st

st.sidebar.title('🌸생계유지곤란사유 병역감면원🌸')
select_species = st.sidebar.selectbox(
    '확인하고 싶은 사항을 선택하세요',
    ['자가진단 참고사항','병역감면 제도 개요','자가진단 시작하기']
)

st.set_page_config(
    page_title="경기북부병무지청 생계심사 자가진단",
    page_icon=":pickup_truck:",
    initial_sidebar_state="expanded",
)

st.write("# 경기북부병무지청 생계 자가진단")
 

st.markdown(
    """##### 테스트중!

"""
)  
