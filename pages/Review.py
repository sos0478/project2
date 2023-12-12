import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
import matplotlib.font_manager as fm

font_dirs = [os.getcwd() + '/customFonts']
font_files = fm.findSystemFonts(fontpaths=font_dirs)
for font_file in font_files:
    fm.fontManager.addfont(font_file)
fm._load_fontmanager(try_read_cache=False)
plt.rc('font', family='NanumSquareRound')
mpl.rcParams['axes.unicode_minus'] = False


st.header("6학년 2학기 소수의 나눗셈 맞춤형 단원 평가 결과 분석")


Q_score = [
    st.session_state["C1"], st.session_state["C2"], st.session_state["C3"], st.session_state["C4"],
    st.session_state["C5"], st.session_state["C6"], st.session_state["C7"], st.session_state["C8"],
    st.session_state["C9"], st.session_state["C10"], st.session_state["C11"], st.session_state["C12"],
    st.session_state["C13"], st.session_state["C14"]             
]

Q_score_up = [
    st.session_state["UP1"], st.session_state["UP2"], st.session_state["UP3"], st.session_state["UP4"],
    st.session_state["UP5"], st.session_state["UP6"]
]

Q_type = [
    st.session_state["Q1"], st.session_state["Q2"], st.session_state["Q3"], st.session_state["Q4"],
    st.session_state["Q5"], st.session_state["Q6"], st.session_state["Q7"], st.session_state["Q8"],
    st.session_state["Q9"], st.session_state["Q10"], st.session_state["Q11"], st.session_state["Q12"],
    st.session_state["Q13"], st.session_state["Q14"]
]


#Q9, 10은 제외(객관식이라서), 수치 1
type_mistake = "유형 1"

#Q9, 10, 11, 12, 13, 14는 제외, 수치 2, 3 순서
type_decimal = "유형 2"
type_natural = "유형 9"

#Q9, 10에만 해당, 수치 2, 3 순서
type_estimate = "유형 3"
type_estimate_natural = "유형 4"

#Q11, 12에만 해당, 수치 2, 2.5, 3, 3.5, 4
type_mistake_rounds = "유형 5"
type_rounds = "유형 6"
type_decimal2 = "유형 2"
type_decimal_rounds = "유형 2, 유형 6"
type_natural2 = "유형 9"

#Q13, 14에만 해당, 수치 2, 2.5, 3, 3.5, 4
type_mistake_remain = "유형 7"
type_remain = "유형 8"
type_decimal3 = "유형 2"
type_decimal_remain = "유형 2, 유형 8"
type_natural3 = "유형 9"

A1 = ""
A2 = ""
A3 = ""
A4 = ""
A5 = ""
A6 = ""
A7 = ""
A8 = ""
A9 = ""
A10 = ""
A11 = ""
A12 = ""
A13 = ""
A14 = ""

if st.session_state["Q1"] == 1:
    A1 = type_mistake
elif st.session_state["Q1"] == 2:
    A1 = type_decimal
elif st.session_state["Q1"] == 3:
    A1 = type_natural


if st.session_state["Q2"] == 1:
    A2 = type_mistake
elif st.session_state["Q2"] == 2:
    A2 = type_decimal
elif st.session_state["Q2"] == 3:
    A2 = type_natural


if st.session_state["Q3"] == 1:
    A3 = type_mistake
elif st.session_state["Q3"] == 2:
    A3 = type_decimal
elif st.session_state["Q3"] == 3:
    A3 = type_natural


if st.session_state["Q4"] == 1:
    A4 = type_mistake
elif st.session_state["Q4"] == 2:
    A4 = type_decimal
elif st.session_state["Q4"] == 3:
    A4 = type_natural


if st.session_state["Q5"] == 1:
    A5 = type_mistake
elif st.session_state["Q5"] == 2:
    A5 = type_decimal
elif st.session_state["Q5"] == 3:
    A5 = type_natural


if st.session_state["Q6"] == 1:
    A6 = type_mistake
elif st.session_state["Q6"] == 2:
    A6 = type_decimal
elif st.session_state["Q6"] == 3:
    A6 = type_natural


if st.session_state["Q7"] == 1:
    A7 = type_mistake
elif st.session_state["Q7"] == 2:
    A7 = type_decimal
elif st.session_state["Q7"] == 3:
    A7 = type_natural


if st.session_state["Q8"] == 1:
    A8 = type_mistake
elif st.session_state["Q8"] == 2:
    A8 = type_decimal
elif st.session_state["Q8"] == 3:
    A8 = type_natural

if st.session_state["Q9"] == 2:
    A9 = type_estimate
elif st.session_state["Q9"] == 3:
    A9 = type_estimate_natural

if st.session_state["Q10"] == 2:
    A10 = type_estimate
elif st.session_state["Q10"] == 3:
    A10 = type_estimate_natural

if st.session_state["Q11"] == 2:
    A11 = type_mistake_rounds
elif st.session_state["Q11"] == 2.5:
    A11 = type_rounds
elif st.session_state["Q11"] == 3:
    A11 = type_decimal2
elif st.session_state["Q11"] == 3.5:
    A11 = type_decimal_rounds
elif st.session_state["Q11"] == 4:
    A11 = type_natural2

if st.session_state["Q12"] == 2:
    A12 = type_mistake_rounds
elif st.session_state["Q12"] == 2.5:
    A12 = type_rounds
elif st.session_state["Q12"] == 3:
    A12 = type_decimal2
elif st.session_state["Q12"] == 3.5:
    A12 = type_decimal_rounds
elif st.session_state["Q12"] == 4:
    A12 = type_natural2

if st.session_state["Q13"] == 2:
    A13 = type_mistake_remain
elif st.session_state["Q13"] == 2.5:
    A13 = type_remain
elif st.session_state["Q13"] == 3:
    A13 = type_decimal3
elif st.session_state["Q13"] == 3.5:
    A13 = type_decimal_remain
elif st.session_state["Q13"] == 4:
    A13 = type_natural3

if st.session_state["Q14"] == 2:
    A14 = type_mistake_remain
elif st.session_state["Q14"] == 2.5:
    A14 = type_remain
elif st.session_state["Q14"] == 3:
    A14 = type_decimal3
elif st.session_state["Q14"] == 3.5:
    A14 = type_decimal_remain
elif st.session_state["Q14"] == 4:
    A14 = type_natural3


Q_type_text = [A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14]

mistake_score = sum("유형 1" in element for element in Q_type_text)
decimal_score = sum("유형 2" in element for element in Q_type_text)
estimate_score = sum("유형 3" in element for element in Q_type_text)
estimate_natural_score = sum("유형 4" in element for element in Q_type_text)
rounds_mistake_score = sum("유형 5" in element for element in Q_type_text)
rounds_score = sum("유형 6" in element for element in Q_type_text)
remain_mistake_score = sum("유형 7" in element for element in Q_type_text)
remain_score = sum("유형 8" in element for element in Q_type_text)
natural_score = sum("유형 9" in element for element in Q_type_text)

type_score_list = [mistake_score, decimal_score, estimate_score, estimate_natural_score, rounds_mistake_score, rounds_score, remain_mistake_score, remain_score, natural_score]
type_score_text_list = ["유형 1", "유형 2", "유형 3", "유형 4", "유형 5", "유형 6", "유형 7", "유형 8", "유형 9"]

Q_list = ["1번", "2번", "3번", "4번", "5번", "6번", "7번", "8번", "9번", "10번", "11번", "12번", "13번", "14번"]
Q_list_up = ["고난도 1번", "고난도 2번", "고난도 3번", "고난도 4번", "고난도 5번", "고난도 6번"]


project = {'문제 번호' : Q_list, '맞춘 문제' : Q_score, '오답 유형 번호' : Q_type}
project_up = {'문제 번호' : Q_list_up, '맞춘 문제' : Q_score_up}
project_type = {'오답 유형 번호' : type_score_text_list, '오답 수' : type_score_list}
project_type_Q = {'문제 번호' : Q_list, '오답 유형' : Q_type_text}

df = pd.DataFrame(project)
df = df.set_index('문제 번호')
df_up = pd.DataFrame(project_up)
df_up = df_up.set_index('문제 번호')
df_type = pd.DataFrame(project_type)
df_type = df_type.set_index('오답 유형 번호')
df_type_Q = pd.DataFrame(project_type_Q)
df_type_Q = df_type_Q.set_index('문제 번호')

recommend_Q_list = df[(df['맞춘 문제'] == df['맞춘 문제'].min()) & (df['오답 유형 번호'] != 1)].index.tolist()
type_list = df_type[df_type['오답 수'] == df_type['오답 수'].max()].index.tolist()


x1 = 14
X1 = range(1, x1+1)
x2 = 6
X2 = range(1, x2+1)
x3 = 9
X3 = range(1, x3+1)



fig1 = plt.figure()
plt.bar(X1, Q_score)
plt.title('소수의 나눗셈 맞춤형 단원 평가 결과 - 일반 문제')
plt.xlabel('문제 번호', fontsize=15)
plt.ylabel('정답 수', fontsize=15)
plt.xticks(X1, Q_list, fontsize=12)
st.pyplot(fig1)

st.write("1번의 계산 실수 이후에 맞춘 경우 정답으로 처리하였습니다. 다만 계산 실수한 것은 기록되어 오답 유형에 나타납니다.")
st.subheader("문제 유형 설명")
st.write("유형 1 (1번, 2번) : 소수 첫째 자리끼리의 나눗셈")
st.write("유형 2 (3번, 4번) : 소수 둘째 자리끼리의 나눗셈")
st.write("유형 3 (5번, 6번) : 소수 첫째 자리와 둘째 자리끼리의 나눗셈")
st.write("유형 4 (7번, 8번) : 자연수를 소수로 나누는 나눗셈")
st.write("유형 5 (9번, 10번) : 소수의 나눗셈에서 몫의 소수점 위치를 확인하여 어림하기")
st.write("유형 6 (11번, 12번) : 소수의 나눗셈에서 몫을 반올림하여 나타내기")
st.write("유형 7 (13번, 14번) : 소수의 나눗셈에서 나머지 구하기")

fig2 = plt.figure()
plt.bar(X2, Q_score_up)
plt.title('소수의 나눗셈 맞춤형 단원 평가 결과 - 고난도 문제')
plt.xlabel('문제 번호', fontsize=15)
plt.ylabel('정답 수', fontsize=15)
plt.xticks(X2, Q_list_up, fontsize=12)
st.pyplot(fig2)
st.write("같은 유형의 문제를 2번의 기회 안에 모두 맞춰야만 고난도 문제를 풀 수 있습니다.")
st.subheader("고난도 문제 유형")
st.write("유형 1(고난도 1번), 유형 2(고난도 2번), 유형 3(고난도 3번), 유형 4(고난도 4번), 유형 6(고난도 5번), 유형 7(고난도 6번)")
st.write("유형 5는 고난도 문제가 없습니다.")


st.subheader("소수의 나눗셈 맞춤형 단원 평가 결과 - 문제별 오답 유형")
st.dataframe(df_type_Q)

fig4 = plt.figure()
plt.bar(X3, type_score_list)
plt.title('소수의 나눗셈 맞춤형 단원 평가 결과 - 오답 유형 분석', fontsize=18)
plt.xlabel('오답 유형', fontsize=15)
plt.ylabel('오답 수', fontsize=15)
plt.xticks(X3, type_score_text_list, fontsize=12)
st.pyplot(fig4)

st.subheader("오답 유형 설명")
st.write("유형 1 : 단순 계산 실수")
st.write("유형 2 : 소수의 나눗셈을 자연수의 나눗셈으로 바꾸는 데 어려움이 있으나, 자연수의 나눗셈은 계산할 수 있음")
st.write("유형 3 : 소수의 나눗셈에서 어림하는 데 어려움이 있으나, 자연수의 나눗셈으로 바꾸면 몫을 어림할 수 있음")
st.write("유형 4 : 소수의 나눗셈과 자연수의 나눗셈에서 몫을 어림하지 못함")
st.write("유형 5 : 소수의 나눗셈에서 반올림하는 과정에서 실수함")
st.write("유형 6 : 소수의 나눗셈에서 반올림하는 방법을 이해하지 못함")
st.write("유형 7 : 소수의 나눗셈에서 나머지를 구하는 과정에서 실수함")
st.write("유형 8 : 소수의 나눗셈에서 나머지를 구하는 방법을 이해하지 못함")
st.write("유형 9 : 소수의 나눗셈과 자연수의 나눗셈을 모두 이해하지 못함")


st.subheader("분석 결과 요약")
st.write("총 14문제 중에서 ", Q_score.count(1), "문제를 맞혔습니다.")
st.write("또한 고난도 문제 6문제 중에서 ", Q_score_up.count(1), "문제를 맞혔습니다.")
st.write("계산 실수를 제외하면 ", ', '.join(recommend_Q_list), " 문제를 틀렸습니다.")
st.write("가장 많은 오답 유형은 ", ', '.join(type_list), "입니다.")

st.session_state["R_Q_list"] = recommend_Q_list
practice = st.selectbox('틀린 문제 중에서 연습하고 싶은 문제를 골라주세요.', st.session_state["R_Q_list"])
if st.button('연습 문제로 이동하기'):
    if practice == "1번":
        switch_page("Q1-P")
    elif practice == "2번":
        switch_page("Q2-P")
    elif practice == "3번":
        switch_page("Q3-P")
    elif practice == "4번":
        switch_page("Q4-P")
    elif practice == "5번":
        switch_page("Q5-P")
    elif practice == "6번":
        switch_page("Q6-P")
    elif practice == "7번":
        switch_page("Q7-P")
    elif practice == "8번":
        switch_page("Q8-P")
    elif practice == "9번":
        switch_page("Q9-P")
    elif practice == "10번":
        switch_page("Q10-P")
    elif practice == "11번":
        switch_page("Q11-P")
    elif practice == "12번":
        switch_page("Q12-P")
    elif practice == "13번":
        switch_page("Q13-P")
    elif practice == "14번":
        switch_page("Q14-P")


st.session_state["Q_up_list"] = Q_list_up
practice_up = st.selectbox('풀지 못했던 고난도 문제 중에서 도전하고 싶은 문제를 골라주세요.', st.session_state["Q_up_list"])
if st.button('고난도 문제로 이동하기'):
    if practice_up == "고난도 1번":
        switch_page("Q2-UP-P")
    elif practice_up == "고난도 2번":
        switch_page("Q4-UP-P")
    elif practice_up == "고난도 3번":
        switch_page("Q6-UP-P")
    elif practice_up == "고난도 4번":
        switch_page("Q8-UP-P")
    elif practice_up == "고난도 5번":
        switch_page("Q12-UP-P")
    elif practice_up == "고난도 6번":
        switch_page("Q14-UP-P")
