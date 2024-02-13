import streamlit as st   

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
def corona_self_diagnosis():
    # 사용자로부터 나이를 입력받습니다.
    age = int(input("나이를 입력하세요: "))

    # 사용자로부터 증상 유무를 입력받습니다.
    symptoms = input("코로나 증상이 있습니까? (예/아니오): ").lower()

    # 자가진단 로직을 수행합니다.
    if age >= 65 or symptoms == '예':
        result = "자가격리 및 코로나 검사가 권장됩니다."
    else:
        result = "증상이 없거나 경미한 경우, 주의사항을 준수하세요."

    # 결과를 출력합니다.
    print("자가진단 결과:", result)

# 자가진단 함수를 호출합니다.
corona_self_diagnosis()
