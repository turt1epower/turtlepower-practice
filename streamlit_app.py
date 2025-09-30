import streamlit as st
import pandas as pd
import numpy as np

st.title("성적 데이터 시각화 앱")  # 앱 제목
st.write("성적 데이터를 CSV로 직접 입력하거나 업로드하면 다양한 통계와 시각화를 볼 수 있습니다.")

# 1. CSV 직접 입력
st.subheader("CSV 데이터 직접 입력 또는 업로드")
csv_text = st.text_area("CSV 데이터를 직접 입력하세요 (예: 이름,국어,수학,영어\n홍길동,90,80,70)", "이름,국어,수학,영어\n홍길동,90,80,70\n김철수,85,95,100\n이영희,60,75,80")
uploaded_file = st.file_uploader("또는 CSV 파일을 업로드하세요", type=["csv"])

# 2. 데이터프레임 생성
df = None
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("파일 업로드 성공!")
elif csv_text:
    from io import StringIO
    try:
        df = pd.read_csv(StringIO(csv_text))
    except Exception as e:
        st.error(f"CSV 파싱 오류: {e}")

if df is not None:
    st.subheader("입력된 성적 데이터")
    st.dataframe(df)

    # 통계 정보
    st.subheader("통계 정보")
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    if numeric_cols:
        st.write("과목별 평균 점수:")
        st.table(df[numeric_cols].mean())
        st.write("과목별 최고 점수:")
        st.table(df[numeric_cols].max())
        st.write("과목별 최저 점수:")
        st.table(df[numeric_cols].min())

    # 3. 그래프 옵션
    st.subheader("그래프 시각화")
    graph_type = st.radio("그래프 종류를 선택하세요", ["히스토그램", "막대그래프", "산점도", "상자그림"])

    # 4. 변수 선택 및 그래프 그리기
    import matplotlib.pyplot as plt
    import seaborn as sns

    if graph_type == "히스토그램":
        col = st.selectbox("히스토그램을 그릴 변수(숫자형)", numeric_cols)
        if col:
            fig, ax = plt.subplots()
            sns.histplot(df[col], kde=True, ax=ax)
            ax.set_title(f"{col} 히스토그램")
            st.pyplot(fig)
    elif graph_type == "막대그래프":
        x_col = st.selectbox("X축 변수", df.columns)
        y_col = st.selectbox("Y축 변수(숫자형)", numeric_cols)
        if x_col and y_col:
            fig, ax = plt.subplots()
            sns.barplot(x=df[x_col], y=df[y_col], ax=ax)
            ax.set_title(f"{x_col}별 {y_col} 막대그래프")
            st.pyplot(fig)
    elif graph_type == "산점도":
        x_col = st.selectbox("X축 변수(숫자형)", numeric_cols, key="scatter_x")
        y_col = st.selectbox("Y축 변수(숫자형)", numeric_cols, key="scatter_y")
        if x_col and y_col:
            fig, ax = plt.subplots()
            sns.scatterplot(x=df[x_col], y=df[y_col], ax=ax)
            ax.set_title(f"{x_col} vs {y_col} 산점도")
            st.pyplot(fig)
    elif graph_type == "상자그림":
        col = st.selectbox("상자그림을 그릴 변수(숫자형)", numeric_cols, key="box_col")
        group_col = st.selectbox("그룹 변수(선택)", [c for c in df.columns if c not in numeric_cols], key="box_group")
        fig, ax = plt.subplots()
        if group_col:
            sns.boxplot(x=df[group_col], y=df[col], ax=ax)
            ax.set_title(f"{group_col}별 {col} 상자그림")
        else:
            sns.boxplot(y=df[col], ax=ax)
            ax.set_title(f"{col} 상자그림")
        st.pyplot(fig)
