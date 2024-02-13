import streamlit as st

def corona_self_diagnosis():
    # 사용자로부터 나이를 입력받습니다.
    age = st.slider("나이를 입력하세요", min_value=1, max_value=100, value=30)

    # 사용자로부터 증상 유무를 입력받습니다.
    symptoms = st.radio("코로나 증상이 있습니까?", ('예', '아니오'))

    # 자가진단 로직을 수행합니다.
    if age >= 65 or symptoms == '예':
        result = "자가격리 및 코로나 검사가 권장됩니다."
    else:
        result = "증상이 없거나 경미한 경우, 주의사항을 준수하세요."

    # 결과를 출력합니다.
    st.subheader("자가진단 결과:")
    st.write(result)

# Streamlit 앱 실행
if __name__ == '__main__':
    st.title("생계유지곤란사유 병역감면 자가진단")
    corona_self_diagnosis()
