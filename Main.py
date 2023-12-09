import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd

st.set_page_config(initial_sidebar_state="collapsed")

question_data = pd.read_excel("question data.xlsx")
Q1 = question_data.iloc[:6]
Q1_S = Q1.sample(6, replace=False)
st.session_state["a1"] = Q1_S.iat[0, 1]
st.session_state["b1"] = Q1_S.iat[0, 2]
st.session_state["x1"] = Q1_S.iat[0, 3]

Q2 = question_data.iloc[6:12,:6]
Q2_S = Q2.sample(6, replace=False)
st.session_state["a2"] = Q2_S.iat[0, 1]
st.session_state["b2"] = Q2_S.iat[0, 2]
st.session_state["x2"] = Q2_S.iat[0, 3]

Q3 = question_data.iloc[12:20,:6]
Q3_S = Q3.sample(8, replace=False)
st.session_state["a3"] = Q3_S.iat[0, 1]
st.session_state["b3"] = Q3_S.iat[0, 2]
st.session_state["x3"] = Q3_S.iat[0, 3]

Q4 = question_data.iloc[20:28,:6]
Q4_S = Q4.sample(8, replace=False)
st.session_state["a4"] = Q4_S.iat[0, 1]
st.session_state["b4"] = Q4_S.iat[0, 2]
st.session_state["x4"] = Q4_S.iat[0, 3]

Q5 = question_data.iloc[28:32,:6]
Q5_S = Q5.sample(4, replace=False)
st.session_state["a5"] = Q5_S.iat[0, 1]
st.session_state["b5"] = Q5_S.iat[0, 2]
st.session_state["x5"] = Q5_S.iat[0, 3]

Q6 = question_data.iloc[32:36,:6]
Q6_S = Q6.sample(4, replace=False)
st.session_state["a6"] = Q6_S.iat[0, 1]
st.session_state["b6"] = Q6_S.iat[0, 2]
st.session_state["x6"] = Q6_S.iat[0, 3]

Q7 = question_data.iloc[36:40,:6]
Q7_S = Q7.sample(4, replace=False)
st.session_state["a7"] = Q7_S.iat[0, 1]
st.session_state["b7"] = Q7_S.iat[0, 2]
st.session_state["x7"] = Q7_S.iat[0, 3]

Q8 = question_data.iloc[40:48,:6]
Q8_S = Q8.sample(8, replace=False)
st.session_state["a8"] = Q8_S.iat[0, 1]
st.session_state["b8"] = Q8_S.iat[0, 2]
st.session_state["x8"] = Q8_S.iat[0, 3]

Q9 = question_data.iloc[48:52,:9]
Q9_S = Q9.sample(4, replace=False)
st.session_state["a9"] = Q9_S.iat[0, 1]
st.session_state["b9"] = Q9_S.iat[0, 2]
st.session_state["x9"] = Q9_S.iat[0, 3]
st.session_state["y9-1"] = Q9_S.iat[0, 4]
st.session_state["y9-2"] = Q9_S.iat[0, 5]
st.session_state["y9-3"] = Q9_S.iat[0, 6]
st.session_state["a9_2"] = Q9_S.iat[0, 7]
st.session_state["b9_2"] = Q9_S.iat[0, 8]

Q10 = question_data.iloc[52:56,:11]
Q10_S = Q10.sample(4, replace=False)
st.session_state["a10"] = Q10_S.iat[0, 1]
st.session_state["b10"] = Q10_S.iat[0, 2]
st.session_state["x10"] = Q10_S.iat[0, 3]
st.session_state["y10-1"] = Q10_S.iat[0, 4]
st.session_state["y10-2"] = Q10_S.iat[0, 5]
st.session_state["y10-3"] = Q10_S.iat[0, 6]
st.session_state["a10_2"] = Q10_S.iat[0, 7]
st.session_state["b10_2"] = Q10_S.iat[0, 8]
st.session_state["a10_3"] = Q10_S.iat[0, 9]
st.session_state["b10_3"] = Q10_S.iat[0, 10]

Q11 = question_data.iloc[56:64,:7]
Q11_S = Q11.sample(8, replace=False)
st.session_state["a11"] = Q11_S.iat[0, 1]
st.session_state["b11"] = Q11_S.iat[0, 2]
st.session_state["x11"] = Q11_S.iat[0, 3]
st.session_state["y11"] = Q11_S.iat[0, 4]
st.session_state["y11_2"] = Q11_S.iat[0, 5]

Q12 = question_data.iloc[64:68,:7]
Q12_S = Q12.sample(4, replace=False)
st.session_state["a12"] = Q12_S.iat[0, 1]
st.session_state["b12"] = Q12_S.iat[0, 2]
st.session_state["x12"] = Q12_S.iat[0, 3]
st.session_state["y12"] = Q12_S.iat[0, 4]
st.session_state["y12_2"] = Q12_S.iat[0, 5]

Q13 = question_data.iloc[68:72,:7]
Q13_S = Q13.sample(4, replace=False)
st.session_state["a13"] = Q13_S.iat[0, 1]
st.session_state["b13"] = Q13_S.iat[0, 2]
st.session_state["x13"] = Q13_S.iat[0, 3]
st.session_state["y13"] = Q13_S.iat[0, 4]
st.session_state["y13_2"] = Q13_S.iat[0, 5]

Q14 = question_data.iloc[72:76,:7]
Q14_S = Q14.sample(4, replace=False)
st.session_state["a14"] = Q14_S.iat[0, 1]
st.session_state["b14"] = Q14_S.iat[0, 2]
st.session_state["x14"] = Q14_S.iat[0, 3]
st.session_state["y14"] = Q14_S.iat[0, 4]
st.session_state["y14_2"] = Q14_S.iat[0, 5]


situation_data = pd.read_excel("situation data.xlsx")
Q2_UP = situation_data.sample(20, replace=False)
st.session_state["Q2_UP"] = Q2_UP.iat[0, 1]
st.session_state["a2_up"] = Q2_S.iat[1, 1]
st.session_state["b2_up"] = Q2_S.iat[1, 2]
st.session_state["x2_up"] = Q2_S.iat[1, 3]

st.session_state["Q4_UP"] = Q2_UP.iat[1, 1]
st.session_state["a4_up"] = Q4_S.iat[1, 1]
st.session_state["b4_up"] = Q4_S.iat[1, 2]
st.session_state["x4_up"] = Q4_S.iat[1, 3]

st.session_state["Q6_UP"] = Q2_UP.iat[2, 1]
st.session_state["a6_up"] = Q6_S.iat[1, 1]
st.session_state["b6_up"] = Q6_S.iat[1, 2]
st.session_state["x6_up"] = Q6_S.iat[1, 3]

st.session_state["Q8_UP"] = Q2_UP.iat[3, 1]
st.session_state["a8_up"] = Q8_S.iat[1, 1]
st.session_state["b8_up"] = Q8_S.iat[1, 2]
st.session_state["x8_up"] = Q8_S.iat[1, 3]

st.session_state["Q12_UP"] = Q2_UP.iat[4, 1]
st.session_state["a12_up"] = Q12_S.iat[1, 1]
st.session_state["b12_up"] = Q12_S.iat[1, 2]
st.session_state["x12_up"] = Q12_S.iat[1, 3]
st.session_state["y12_up"] = Q12_S.iat[1, 4]
st.session_state["y12_up_2"] = Q12_S.iat[1, 5]

Q14_UP = situation_data.sample(5, replace=False)
st.session_state["Q14_UP"] = Q14_UP.iat[0, 2]
st.session_state["a14_up"] = Q14_S.iat[1, 1]
st.session_state["b14_up"] = Q14_S.iat[1, 2]
st.session_state["x14_up"] = Q14_S.iat[1, 3]
st.session_state["y14_up"] = Q14_S.iat[1, 4]
st.session_state["y14_up_2"] = Q14_S.iat[1, 5]


st.header("6학년 2학기 소수의 나눗셈 맞춤형 단원 평가")
st.write("문제를 맞힐수록 조금 더 어려운 문제가, 문제를 틀릴수록 조금 더 쉬운 문제가 제공됩니다.")
st.write("나중에 자신의 약점을 그래프로 확인할 수 있고, 약점 연습 문제를 풀어볼 수 있습니다.")
if st.button("평가 시작하기"):
    switch_page("Q1")

st.session_state["C1"] = 0
st.session_state["C2"] = 0
st.session_state["C3"] = 0
st.session_state["C4"] = 0
st.session_state["C5"] = 0
st.session_state["C6"] = 0
st.session_state["C7"] = 0
st.session_state["C8"] = 0
st.session_state["C9"] = 0
st.session_state["C10"] = 0
st.session_state["C11"] = 0
st.session_state["C12"] = 0
st.session_state["C13"] = 0
st.session_state["C14"] = 0

st.session_state["Q1"] = 0
st.session_state["Q2"] = 0
st.session_state["Q3"] = 0
st.session_state["Q4"] = 0
st.session_state["Q5"] = 0
st.session_state["Q6"] = 0
st.session_state["Q7"] = 0
st.session_state["Q8"] = 0
st.session_state["Q9"] = 0
st.session_state["Q10"] = 0
st.session_state["Q11"] = 0
st.session_state["Q12"] = 0
st.session_state["Q13"] = 0
st.session_state["Q14"] = 0
