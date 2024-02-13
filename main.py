import streamlit as st

def military_exemption_diagnosis():
    st.title("병역감면 진단")

    # 사용자로부터 다양한 정보를 입력받습니다.
    age = st.slider("나이를 입력하세요", min_value=18, max_value=40, value=20)
    health_status = st.selectbox("건강 상태를 선택하세요", ["건강함", "질병/장해 있음"])
    military_service = st.selectbox("군 복무 경력이 있습니까?", ["없음", "있음"])
    education_level = st.selectbox("최종 학력을 선택하세요", ["고졸 이하", "대졸", "대학원 이상"])
    family_status = st.selectbox("가족 상태를 선택하세요", ["독신", "결혼"])

    # 병역감면 진단 로직을 수행합니다.
    exemption_eligible = age >= 28 and health_status == "건강함" and military_service == "없음"
    education_criteria = education_level == "대학원 이상"
    family_criteria = family_status == "독신"

    # 결과를 출력합니다.
    st.subheader("병역감면 진단 결과:")
    if exemption_eligible and (education_criteria or family_criteria):
        result = "복잡한 조건에 부합하여 병역감면이 가능할 수 있습니다."
    else:
        result = "현재 조건으로는 병역감면이 어려울 수 있습니다."

    st.write(result)

# Streamlit 앱 실행
if __name__ == '__main__':
    military_exemption_diagnosis()
