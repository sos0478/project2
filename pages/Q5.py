import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd

Q5_Text = f'5. {st.session_state["a5"]} \u00F7 {st.session_state["b5"]} ='
st.title(Q5_Text)
answer1 = st.number_input("답 : ", key="1", value=None, placeholder="답을 입력하세요.", format="%f")

if "N5" not in st.session_state:
    st.session_state["N5"] = True

if "B15" not in st.session_state:
    st.session_state["B15"] = False
if "B16" not in st.session_state:
    st.session_state["B16"] = False
if "B17" not in st.session_state:
    st.session_state["B17"] = False

def make1():
    st.session_state["B15"] = True
def make2():
    st.session_state["B16"] = True
def make3():
    st.session_state["B17"] = True

if st.button("채점하기", key="a", on_click=make1, disabled=st.session_state["B15"]):
    if answer1 == None:
        answer1 = 0
    if float(answer1) == float(st.session_state["x5"]):
        st.session_state["C5"] = st.session_state["C5"] + 1
        st.session_state["N5"] = False
        st.write("정답입니다.")
    else:
        st.session_state["Q5"] = st.session_state["Q5"] + 1


if st.session_state["Q5"] == 1:
    st.write("혹시 계산 실수가 있었나요? 천천히 계산해보고 다시 답을 입력해주세요.")
    answer2 = st.number_input("답 : ", key="2", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="b", on_click=make2, disabled=st.session_state["B16"]):  
        if answer2 == None:
            answer2 = 0   
        if float(answer2) == float(st.session_state["x5"]):
            st.session_state["C5"] = st.session_state["C5"] + 1
            st.session_state["N5"] = False
            st.write("정답입니다.")
        else:
            st.session_state["Q5"] = st.session_state["Q5"] + 1
       

if st.session_state["Q5"] == 2:  
    st.write("소수의 나눗셈을 이해하는 데 어려움이 있는 것 같군요. 그렇다면 자연수의 나눗셈으로 바꿔봅시다.")
    a5 = int(st.session_state["a5"]*100)
    b5 = int(st.session_state["b5"]*100)
    st.write("나누는 수와 나누어지는 수에 같은 수를 곱해도 답은 변하지 않는다는 점을 이용하면 자연수로 쉽게 바꿀 수 있답니다.")
    st.write("지금 문제는 나누는 수와 나누어지는 수에 똑같이 100을 곱해주면 되겠네요.")
    st.write("그렇게 되면 ", st.session_state["a5"], "이 ", a5, "로 바뀌게 되고,")
    st.write(st.session_state["b5"], "이 ", b5, "로 바뀌게 됩니다.")
    st.write("그렇다면 자연수의 나눗셈으로 바꾼 식을 풀어봅시다.")
    Q5_easy_Text = f"5. {a5} \u00F7 {b5} ="
    st.markdown(Q5_easy_Text)
    answer3 = st.number_input("답 : ", key="3", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="c", on_click=make3, disabled=st.session_state["B17"]): 
        if answer3 == None:
            answer3 = 0
        if float(answer3) == float(st.session_state["x5"]):
            st.session_state["N5"] = False
            st.write("정답입니다. 처음 문제를 방금 푼 자연수의 나눗셈으로 바꾸듯이 소수의 나눗셈은 소수점을 이동하여 자연수의 나눗셈으로 만들어 풀면 됩니다.")
        else:
            st.session_state["Q5"] = st.session_state["Q5"] + 1


if st.session_state["Q5"] == 3:
    st.session_state["N5"] = False
    st.write("오답입니다. 자연수의 나눗셈에도 어려움이 있거나 계산 실수가 있는 것 같네요. 일단 다음 문제를 이어서 풀어봅시다.")

st.write("채점을 마친 후에만 클릭하여 다음 문제로 넘어갈 수 있습니다.")
if st.button("다음 문제로 넘어가기", disabled=st.session_state["N5"]):
    switch_page("Q6")