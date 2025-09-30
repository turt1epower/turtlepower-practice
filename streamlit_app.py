import streamlit as st

# 1. 제목
st.title("Streamlit 주요 요소 예시")  # 페이지의 제목

# 2. 텍스트
st.header("텍스트 요소")  # 섹션 헤더
st.subheader("서브헤더 예시")  # 서브헤더
st.text("일반 텍스트 예시")  # 일반 텍스트
st.markdown("**마크다운 텍스트** _예시_ ")  # 마크다운 지원
st.caption("캡션(설명) 예시")  # 작은 설명 텍스트
st.code("print('Hello Streamlit!')", language='python')  # 코드 블록
st.latex(r"E=mc^2")  # LaTeX 수식

# 3. 미디어
st.header("미디어 요소")
st.image("https://static.streamlit.io/examples/dog.jpg", caption="이미지 예시")  # 이미지
st.audio(
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    format="audio/mp3",
    start_time=0
)  # 오디오
st.video(
    "https://www.w3schools.com/html/mov_bbb.mp4"
)  # 비디오

# 4. 입력 위젯
st.header("입력 위젯 예시")
st.button("버튼")  # 버튼
st.checkbox("체크박스")  # 체크박스
st.radio("라디오 버튼", ["A", "B", "C"])  # 라디오 버튼
st.selectbox("셀렉트박스", ["옵션1", "옵션2", "옵션3"])  # 셀렉트박스
st.multiselect("멀티셀렉트", ["옵션1", "옵션2", "옵션3"])  # 다중 선택
st.slider("슬라이더", 0, 100, 50)  # 슬라이더
st.text_input("텍스트 입력")  # 텍스트 입력
st.text_area("텍스트 영역")  # 여러 줄 텍스트 입력
st.date_input("날짜 입력")  # 날짜 입력
st.time_input("시간 입력")  # 시간 입력
st.file_uploader("파일 업로더")  # 파일 업로드

# 5. 데이터 표시
st.header("데이터 표시 예시")
import pandas as pd
import numpy as np
df = pd.DataFrame(
    np.random.randn(5, 3),
    columns=["a", "b", "c"]
)
st.dataframe(df)  # 동적 데이터프레임
st.table(df)  # 정적 테이블

# 6. 차트
st.header("차트 예시")
st.line_chart(df)  # 라인 차트
st.bar_chart(df)  # 바 차트
st.area_chart(df)  # 영역 차트

# 7. 상태/알림
st.header("상태/알림 예시")
st.success("성공 메시지")  # 성공 메시지
st.info("정보 메시지")  # 정보 메시지
st.warning("경고 메시지")  # 경고 메시지
st.error("에러 메시지")  # 에러 메시지
st.exception(Exception("예외 메시지 예시"))  # 예외 메시지

# 8. 진행률/스피너
st.header("진행률/스피너 예시")
import time
with st.spinner("로딩 중..."):
    time.sleep(1)
st.progress(70)  # 진행률 바

# 9. 사이드바
st.sidebar.title("사이드바 예시")  # 사이드바 제목
st.sidebar.button("사이드바 버튼")  # 사이드바 버튼

# 10. 기타
st.header("기타 요소")
st.help(st.slider)  # 함수 도움말

# 각 요소별 각주: 각 코드 라인 끝에 # 으로 설명
