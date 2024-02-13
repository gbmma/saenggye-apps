import streamlit as st
st.sidebar.title("병무청 생계곤란사유 병역감면원이란?")
select_species = st.sidebar.selectbox(
    '✔️확인하고 싶은 사항을 선택하세요',
    ['📝자가진단하기','📖제도 개요']
)

def military_exemption_diagnosis(income, family_members, health_status, military_service):
    # 생계곤란사유 병역감면 진단 로직을 수행합니다.
    income_criteria = income < 3000000  # 가계 소득이 3,000,000원 미만인 경우
    family_criteria = family_members <= 4  # 가족 수가 4명 이하인 경우
    health_criteria = health_status == "질병/장해 있음"  # 건강 상태가 질병/장해 있는 경우
    military_criteria = military_service == "있음"  # 군 복무 경력이 있는 경우

    # 결과를 반환합니다.
    if income_criteria or family_criteria or health_criteria or military_criteria:
        return "생계곤란사유로 병역감면이 가능할 수 있습니다. 자세한 사항은 담당자에게 문의 바랍니다."
    else:
        return "현재 조건으로는 병역감면이 어려울 수 있습니다."

# Streamlit 앱 실행
if __name__ == '__main__':
    st.title("생계곤란사유 병역감면 진단")

    # 사용자로부터 다양한 정보를 입력받습니다.
    age = st.slider("나이를 입력하세요", min_value=18, max_value=40, value=20)
    military_service = st.selectbox("군 복무 경력이 있습니까?", ["없음", "있음"])
    income = st.number_input("가계 소득을 입력하세요 (원)", min_value=0, step=1000000, value=0)
    family_members = st.slider("가족 수를 입력하세요", min_value=1, max_value=10, value=1)
    health_status = st.selectbox("건강 상태를 선택하세요", ["건강함", "질병/장해 있음"]) 

    # ""결과 확인하기" 버튼을 생성합니다.
    if st.button("결과 확인하기"):
        result = military_exemption_diagnosis(income, family_members, health_status, military_service)
        st.subheader("생계곤란사유 병역감면 진단 결과:")
        st.write(result)
