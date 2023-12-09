import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd

a6_up = str(st.session_state["a6_up"])
b6_up = str(st.session_state["b6_up"])
Q6_UP_Text = st.session_state["Q6_UP"].replace('a', a6_up)
Q6_UP_Text = Q6_UP_Text.replace('b', b6_up)

st.header("고난도 문제 3번")
st.subheader(Q6_UP_Text)
answer1 = st.number_input("답 : ", key="1")
st.session_state["N6_UP"] = True

if "B21" not in st.session_state:
    st.session_state["B21"] = False

def make1():
    st.session_state["B21"] = True

st.write("고난도 문제는 채점 기회가 1번 뿐이니 신중하게 눌러주세요.")
if st.button("채점하기", key="a", on_click=make1, disabled=st.session_state["B21"]):
    if float(answer1) == float(st.session_state["x6_up"]):
        st.session_state["C5"] = st.session_state["C5"] + 1
        st.session_state["C6"] = st.session_state["C6"] + 1
        st.session_state["N6_UP"] = False
        st.write("정답입니다.")
    else:
        st.write("아쉽지만 오답입니다.")
        st.write("문제를 바탕으로 세운 식을 확인해보면 ", st.session_state["a6_up"], "\u00F7", st.session_state["b6_up"], "이 됩니다.")
        st.write("세운 식이 맞다면 계산 실수를 한 것이니 신중하게 풀도록 하고, 세운 식이 잘못되었다면 문제에서 위의 식을 어떻게 끌어냈는지 확인하고 다음 문제로 넘어가봅시다.")
        st.session_state["N6_UP"] = False


st.write("채점을 마친 후에만 클릭하여 다음 문제로 넘어갈 수 있습니다.")
if st.button("다음 문제로 넘어가기", disabled=st.session_state["N6_UP"]):
    switch_page("Q7")