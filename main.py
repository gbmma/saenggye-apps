import streamlit as st

def military_exemption_diagnosis():
    st.title("병역감면 자가진단")

    # 사용자로부터 나이를 입력받습니다.
    age = st.slider("나이를 입력하세요", min_value=18, max_value=40, value=20)

    # 사용자로부터 건강 상태를 입력받습니다.
    health_status = st.selectbox("건강 상태를 선택하세요", ["건강함", "질병/장해 있음"])

    # 사용자로부터 군 복무 경력을 입력받습니다.
    military_service = st.selectbox("군 복무 경력이 있습니까?", ["없음", "있음"])

    # 병역감면 자가진단 로직을 수행합니다.
    if age >= 28 and health_status == "건강함" and military_service == "없음":
        result = "병역감면이 가능할 수 있습니다."
    else:
        result = "병역감면이 어려울 수 있습니다."

    # 결과를 출력합니다.
    st.subheader("병역감면 자가진단 결과:")
    st.write(result)

# Streamlit 앱 실행
if __name__ == '__main__':
    military_exemption_diagnosis()
