import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd

a14_up = str(st.session_state["a14_up"])
b14_up = str(st.session_state["b14_up"])
Q14_UP_Text = st.session_state["Q14_UP"].replace('a', a14_up)
Q14_UP_Text = Q14_UP_Text.replace('b', b14_up)
right_answer = float(st.session_state['a14_up']/st.session_state['b14_up'])

st.header("고난도 문제 6번")
st.subheader(Q14_UP_Text)
answer1 = st.number_input("답 : ", key="1", value=None, placeholder="답을 입력하세요.", format="%f")

if "N14_UP" not in st.session_state:
    st.session_state["N14_UP"] = True

if "B58" not in st.session_state:
    st.session_state["B58"] = False

def make1():
    st.session_state["B58"] = True

st.write("고난도 문제는 채점 기회가 1번 뿐이니 신중하게 눌러주세요.")
if st.button("채점하기", key="a", on_click=make1, disabled=st.session_state["B58"]):
    if float(answer1) == float(st.session_state["x14_up"]):
        st.session_state["UP6"] = st.session_state["UP6"] + 1
        st.session_state["N14_UP"] = False
        st.write("정답입니다.")
    else:
        st.write("아쉽지만 오답입니다.")
        st.write("문제를 바탕으로 세운 식을 확인해보면 ", st.session_state["a14_up"], "\u00F7", st.session_state["b14_up"], "이 됩니다.")
        st.write("이 식에서 몫을 자연수 부분까지만 구하고 남은 나머지를 나누어지는 수의 소수점 위치에 맞게 소수점을 찍으면 ", st.session_state["x14_up"], "이 됩니다.")
        st.write("혹시나 나머지에 소수점을 제대로 찍었는지 확인해보기 바랍니다.")
        st.session_state["N14_UP"] = False


st.write("이번 문제가 마지막이므로 채점을 마친 후에만 클릭하여 결과 분석으로 넘어갈 수 있습니다.")
if st.button("결과 분석으로 넘어가기", disabled=st.session_state["N14_UP"]):
    switch_page("Review")