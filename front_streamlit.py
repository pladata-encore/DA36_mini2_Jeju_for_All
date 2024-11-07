import streamlit as st

# 배경색 설정 (고정)
sidebar_bg_color = "#ffe8be"  # 사이드바 배경색
main_bg_color = "#fffee1"     # 메인 페이지 배경색

# CSS 스타일을 적용하여 배경 색 변경
st.markdown(f"""
    <style>
    /* 사이드바 배경 색 설정 */
    section[data-testid="stSidebar"] > div:first-child {{
        background-color: {sidebar_bg_color};
    }}
    /* 메인 페이지 배경 색 설정 */
    .stApp {{
        background-color: {main_bg_color};
    }}
    </style>
    """, unsafe_allow_html=True)

# 페이지 제목
st.title('🍊모두를 위한 제주🍊')

# sidebar input
with st.sidebar:
    st.header('여행객 정보를 입력해주세요 😄')

    # 연령대 선택
    age_group = st.selectbox(
        "연령대",
        ("10대", "20대", "30대", "40대", "50대", "60대 이상")
    )

    # 성별 선택
    gender = st.radio(
        "성별",
        ("여성", "남성")
    )

    # 동반객 인원수 선택
    companion_count = st.number_input(
        "동반객 인원수 (최대 10명)",
        min_value=0,
        max_value=10,
        value=0,
        step=1
    )

    # 여행 스타일 선택 (여러 개 선택 가능)
    travel_style = st.multiselect(
        "여행 스타일",
        ["자연 탐방", "도시 탐험", "문화 체험", "휴식", "액티비티", "미식 탐방"]
    )

    # Barrier Free 옵션 체크박스
    st.write("베리어 프리 여부")
    barrier_free_options = {
        "시각 장애인 지원": st.checkbox("시각 장애인"),
        "청각 장애인 지원": st.checkbox("청각 장애인"),
        "지체 장애인 지원": st.checkbox("지체 장애인")
    }
selected_barrier_free = [key for key, value in barrier_free_options.items() if value]


# 첫 번째 구간
# 선택된 옵션 - 메인 페이지에 표시

st.subheader('📌 여행객 정보')
st.markdown(f"""
- **연령대**: {age_group}
- **성별**: {gender}
- **동반객 인원수**: {companion_count}명
- **여행 스타일**: {", ".join(travel_style) if travel_style else "선택 없음"}
- **베리어프리 옵션**: {", ".join(selected_barrier_free) if selected_barrier_free else "선택 없음"}
---
""")

st.subheader('📌 추천 장소')
