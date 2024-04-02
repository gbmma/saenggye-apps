import streamlit as st

st.set_page_config(
  page_icon="✅",
  page_title="경기북부청 생계감면 진단",
)

def self_diagnosis_page():
    st.title("생계곤란사유 병역감면 자가진단")

    # 사용자로부터 다양한 정보를 입력받습니다.
    age = st.slider("나이를 입력하세요", min_value=18, max_value=40, value=20)
    military_service = st.selectbox("군 복무 경력이 있습니까?", ["없음", "있음"])
    income = st.number_input("가계 소득을 입력하세요 (원)", min_value=0, step=1000000, value=0)
    property = st.number_input("재산 금액을 입력하세요 (원)", min_value=0, step=1000000, value=0)
    family_members = st.slider("가족 수를 입력하세요", min_value=1, max_value=10, value=1)
    health_status = st.selectbox("건강 상태를 선택하세요", ["질병/장해 있음", "질병/장해 없음"]) 

    # "결과 확인하기" 버튼을 생성합니다.
    if st.button("결과 확인하기"):
        result = military_exemption_diagnosis(income, family_members, health_status, military_service)
        st.subheader("생계곤란사유 병역감면 진단 결과:")
        st.write(result)

def military_exemption_diagnosis(income, family_members, health_status, military_service):
    # 생계곤란사유 병역감면 진단 로직을 수행합니다.
    income_criteria = income < 3000000  # 가계 소득이 3,000,000원 미만인 경우
    property_criteria = income < 10000000  # 재산 금액이 10,000,000원 미만인 경우
    family_criteria = family_members <= 4  # 가족 수가 4명 이하인 경우
    health_criteria = health_status == "질병/장해 있음"  # 건강 상태가 질병/장해 있는 경우
    military_criteria = military_service == "있음"  # 군 복무 경력이 있는 경우

    # 결과를 반환합니다.
    if income_criteria or family_criteria or health_criteria or military_criteria:
        return "생계곤란사유로 병역감면이 가능할 수 있습니다. 자세한 사항은 담당자에게 문의 바랍니다."
    else:
        return "현재 조건으로는 병역감면이 어려울 수 있습니다."

def home_page():
    st.title("병역감면 자가진단 시스템")

    st.write("병역감면 자가진단 시스템에 오신 것을 환영합니다!\n이 시스템을 통해 생계곤란사유를 기반으로 한 병역감면 여부를 진단할 수 있습니다. 상세한 심사는 담당자에게 문의하시기 바랍니다.")
    
    st.header("생계유지 곤란사유 병역감면제도란?")
    st.write("본인이 아니면 가족의 생계를 유지할 수 없는 사람에 대해 1️⃣가족의 부양비, 2️⃣재산액, 3️⃣월수입액이 병역감면 기준에 모두 해당되는 경우 전시근로역으로 편입되어 경제적 배려대상자의 생활 안정을 도모하기 위한 제도입니다.")

link_url = "https://blog.naver.com/mma9090/223372410453"

# 바로가기 버튼 생성
if st.button("병무청 블로그 바로가기"):
    # 버튼 클릭 시 해당 링크로 이동
    st.markdown(f"[생계유지 곤란사유 병역감면 개선사항, 한눈에 알아보아요!]({link_url})")
  
    st.header("자가진단 방법")
    st.write("1. 왼쪽의 사이드바에서 '자가진단하기'를 선택합니다.")
    st.write("2. 나타난 페이지에서 가계 소득, 가족 수, 건강 상태, 군 복무 경력 등을 입력합니다.")
    st.write("3. '결과 확인하기' 버튼을 클릭하여 병역감면 여부를 확인합니다.")
    

# Streamlit 앱 실행
if __name__ == '__main__':
    st.sidebar.title("경기북부병무청 생계심사")
    page_options = ["📝자가진단하기","📖안내 사항"]
    selected_page = st.sidebar.selectbox("🔎확인하고 싶은 사항을 선택하세요", page_options)

    # 선택된 페이지에 따라 내용 출력
    if selected_page == "📝자가진단하기":
        self_diagnosis_page() 
    elif selected_page == "📖안내 사항":
        home_page()
