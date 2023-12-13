import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd

Q2_Text = f'2. {st.session_state["a2"]} \u00F7 {st.session_state["b2"]} ='
st.title(Q2_Text)
answer1 = st.number_input("답 : ", key="1", value=None, placeholder="답을 입력하세요.", format="%f")


if "N2" not in st.session_state:
    st.session_state["N2"] = True
if "N2-UP" not in st.session_state:
    st.session_state["N2-UP"] = True

if "B4" not in st.session_state:
    st.session_state["B4"] = False
if "B5" not in st.session_state:
    st.session_state["B5"] = False
if "B6" not in st.session_state:
    st.session_state["B6"] = False

def make1():
    st.session_state["B4"] = True
def make2():
    st.session_state["B5"] = True
def make3():
    st.session_state["B6"] = True

if st.button("채점하기", key="a", on_click=make1, disabled=st.session_state["B4"]):
    if answer1 == None:
        answer1 = 0
    if float(answer1) == float(st.session_state["x2"]):
        st.session_state["C2"] = st.session_state["C2"] + 1
        st.session_state["N2"] = False
        st.write("정답입니다.")
    else:
        st.session_state["Q2"] = st.session_state["Q2"] + 1

if st.session_state["Q2"] == 1:
    st.write("혹시 계산 실수가 있었나요? 천천히 계산해보고 다시 답을 입력해주세요.")
    answer2 = st.number_input("답 : ", key="2", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="b", on_click=make2, disabled=st.session_state["B5"]):     
        if answer2 == None:
            answer2 = 0
        if float(answer2) == float(st.session_state["x2"]):
            st.session_state["C2"] = st.session_state["C2"] + 1
            st.session_state["N2"] = False
            st.write("정답입니다.")
        else:
            st.session_state["Q2"] = st.session_state["Q2"] + 1
       

if st.session_state["Q2"] == 2:    
    st.write("소수의 나눗셈을 이해하는 데 어려움이 있는 것 같군요. 그렇다면 자연수의 나눗셈으로 바꿔봅시다.")
    a2 = int(st.session_state["a2"]*10)
    b2 = int(st.session_state["b2"]*10)
    st.write("나누는 수와 나누어지는 수에 같은 수를 곱해도 답은 변하지 않는다는 점을 이용하면 자연수로 쉽게 바꿀 수 있답니다.")
    st.write("지금 문제는 나누는 수와 나누어지는 수에 똑같이 10을 곱해주면 되겠네요.")
    st.write("그렇게 되면 ", st.session_state["a2"], "이 ", a2, "로 바뀌게 되고,")
    st.write(st.session_state["b2"], "이 ", b2, "로 바뀌게 됩니다.")
    st.write("그렇다면 자연수의 나눗셈으로 바꾼 식을 풀어봅시다.")
    Q2_easy_Text = f"2. {a2} \u00F7 {b2} ="
    st.markdown(Q2_easy_Text)
    answer3 = st.number_input("답 : ", key="3", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="c", on_click=make3, disabled=st.session_state["B6"]): 
        if answer3 == None:
            answer3 = 0
        if float(answer3) == float(st.session_state["x2"]):
            st.session_state["N2"] = False
            st.write("정답입니다. 처음 문제를 방금 푼 자연수의 나눗셈으로 바꾸듯이 소수의 나눗셈은 소수점을 이동하여 자연수의 나눗셈으로 만들어 풀면 됩니다.")
        else:
            st.session_state["Q2"] = st.session_state["Q2"] + 1


if st.session_state["Q2"] == 3:
    st.session_state["N2"] = False
    st.write("오답입니다. 자연수의 나눗셈에도 어려움이 있거나 계산 실수가 있는 것 같네요. 일단 다음 문제를 이어서 풀어봅시다.")

if st.session_state["C1"] == 1 and st.session_state["C2"] == 1:
    st.session_state["N2-UP"] = False
    st.session_state["N2"] = True

st.write("채점을 마친 후에만 클릭하여 다음 문제로 넘어갈 수 있습니다.")
if st.button("다음 문제로 넘어가기", disabled=st.session_state["N2"]):
    switch_page("Q3")

st.write("1번 문제와 2번 문제를 성공적으로 풀었다면 고난도 문제에 도전할 수 있습니다.")
if st.button("고난도 문제 풀어보기", disabled=st.session_state["N2-UP"]):
    switch_page("Q2-UP")