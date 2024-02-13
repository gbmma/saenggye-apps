import streamlit as st

st.sidebar.title('🌸생계심사 자가진단 테스트🌸')
select_species = st.sidebar.selectbox(
    '확인하고 싶은 종을 선택하세요',
    ['setosa','versicolor','virginica']
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
