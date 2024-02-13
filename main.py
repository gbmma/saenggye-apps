import streamlit as st

def military_exemption_diagnosis():
    st.title("생계곤란사유 병역감면 진단")

    # 사용자로부터 다양한 정보를 입력받습니다.
    income = st.number_input("가계 소득을 입력하세요", min_value=0, step=1000000, value=0)
    family_members = st.slider("가족 수를 입력하세요", min_value=1, max_value=10, value=1)
    health_status = st.selectbox("건강 상태를 선택하세요", ["건강함", "질병/장해 있음"])
    military_service = st.selectbox("군 복무 경력이 있습니까?", ["없음", "있음"])

    # 생계곤란사유 병역감면 진단 로직을 수행합니다.
    income_criteria = income < 3000000  # 가계 소득이 3,000,000원 미만인 경우
    family_criteria = family_members <= 4  # 가족 수가 4명 이하인 경우
    health_criteria = health_status == "질병/장해 있음"  # 건강 상태가 질병/장해 있는 경우
    military_criteria = military_service == "있음"  # 군 복무 경력이 있는 경우

    # 결과를 출력합니다.
    st.subheader("생계곤란사유 병역감면 진단 결과:")
    if income_criteria or family_criteria or health_criteria or military_criteria:
        result = "생계곤란사유로 병역감면이 가능할 수 있습니다."
    else:
        result = "현재 조건으로는 병역감면이 어려울 수 있습니다."

    st.write(result)

# Streamlit 앱 실행
if __name__ == '__main__':
    military_exemption_diagnosis()
