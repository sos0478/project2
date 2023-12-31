import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd

a14_up = str(st.session_state["a14_up_p"])
b14_up = str(st.session_state["b14_up_p"])
Q14_UP_Text = st.session_state["Q14_UP_p"].replace('a', a14_up)
Q14_UP_Text = Q14_UP_Text.replace('b', b14_up)
right_answer = float(st.session_state['a14_up_p']/st.session_state['b14_up_p'])

st.header("고난도 문제 연습 6번")
st.subheader(Q14_UP_Text)
answer1 = st.number_input("답 : ", key="1", value=None, placeholder="답을 입력하세요.", format="%f")

if "B58_p" not in st.session_state:
    st.session_state["B58_p"] = False

def make1():
    st.session_state["B58_p"] = True

st.write("고난도 문제는 채점 기회가 1번 뿐이니 신중하게 눌러주세요.")
if st.button("채점하기", key="a", on_click=make1, disabled=st.session_state["B58_p"]):
    if answer1 == None:
        answer1 = 0
    if float(answer1) == float(st.session_state["x14_up_p"]):
        st.write("정답입니다.")
    else:
        st.write("아쉽지만 오답입니다.")
        st.write("문제를 바탕으로 세운 식을 확인해보면 ", st.session_state["a14_up_p"], "\u00F7", st.session_state["b14_up_p"], "이 됩니다.")
        st.write("이 식에서 몫을 자연수 부분까지만 구하고 남은 나머지를 나누어지는 수의 소수점 위치에 맞게 소수점을 찍으면 ", st.session_state["x14_up_p"], "이 됩니다.")
        st.write("혹시나 나머지에 소수점을 제대로 찍었는지 확인해보기 바랍니다.")

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


if st.button('분석 화면으로 돌아가기'):
    switch_page("Review")