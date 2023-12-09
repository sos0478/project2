import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd

a12_up = str(st.session_state["a12_up"])
b12_up = str(st.session_state["b12_up"])
Q12_UP_Text = st.session_state["Q12_UP"].replace('a', a12_up)
Q12_UP_Text = Q12_UP_Text.replace('b', b12_up)
right_answer = float(st.session_state['a12_up']/st.session_state['b12_up'])

st.header("고난도 문제 5번")
st.subheader(Q12_UP_Text, "단, 답을 ", st.session_state["y12_up"],"하시오.")
answer1 = st.number_input("답 : ", key="1")
st.session_state["N12_UP"] = True

if "B45" not in st.session_state:
    st.session_state["B45"] = False

def make1():
    st.session_state["B45"] = True

st.write("고난도 문제는 채점 기회가 1번 뿐이니 신중하게 눌러주세요.")
if st.button("채점하기", key="a", on_click=make1, disabled=st.session_state["B45"]):
    if float(answer1) == float(st.session_state["x12_up"]):
        st.session_state["C11"] = st.session_state["C11"] + 1
        st.session_state["C12"] = st.session_state["C12"] + 1
        st.session_state["N12_UP"] = False
        st.write("정답입니다.")
    else:
        st.write("아쉽지만 오답입니다.")
        st.write("문제를 바탕으로 세운 식을 확인해보면 ", st.session_state["a12_up"], "\u00F7", st.session_state["b12_up"], "이 됩니다.")
        st.write("이 식에서 구한 몫을 ", st.session_state["a12_up"], "에서 반올림하면 됩니다.")
        st.write("세운 식이 맞다면 계산 실수나 반올림 실수를 한 것이니 신중하게 풀도록 하고, 세운 식이 잘못되었다면 문제에서 위의 식을 어떻게 끌어냈는지 확인하고 다음 문제로 넘어가봅시다.")
        st.session_state["N12_UP"] = False


st.write("채점을 마친 후에만 클릭하여 다음 문제로 넘어갈 수 있습니다.")
if st.button("다음 문제로 넘어가기", disabled=st.session_state["N12_UP"]):
    switch_page("Q13")