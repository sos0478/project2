import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd

Q8_Text = f'연습 8-1. {int(st.session_state["a8_p1"])} \u00F7 {st.session_state["b8_p1"]} ='
st.title(Q8_Text)
answer1 = st.number_input("답 : ", key="1", value=None, placeholder="답을 입력하세요.", format="%f")

if "B25_p1" not in st.session_state:
    st.session_state["B25_p1"] = False
if "B26_p1" not in st.session_state:
    st.session_state["B26_p1"] = False
if "B27_p1" not in st.session_state:
    st.session_state["B27_p1"] = False

def make1():
    st.session_state["B25_p1"] = True
def make2():
    st.session_state["B26_p1"] = True
def make3():
    st.session_state["B27_p1"] = True

if st.button("채점하기", key="a", on_click=make1, disabled=st.session_state["B25_p1"]):
    if float(answer1) == float(st.session_state["x8_p1"]):
        st.write("정답입니다.")
    else:
        st.session_state["Q8_p1"] = st.session_state["Q8_p1"] + 1

if st.session_state["Q8_p1"] == 1:
    st.write("혹시 계산 실수가 있었나요? 천천히 계산해보고 다시 답을 입력해주세요.")
    answer2 = st.number_input("답 : ", key="2", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="b", on_click=make2, disabled=st.session_state["B26_p1"]):     
        if float(answer2) == float(st.session_state["x8_p1"]):
            st.write("정답입니다.")
        else:
            st.session_state["Q8_p1"] = st.session_state["Q8_p1"] + 1
       

if st.session_state["Q8_p1"] == 2:    
    st.write("자연수를 소수로 나누는 나눗셈을 이해하는 데 어려움이 있는 것 같군요. 그렇다면 자연수끼리의 나눗셈으로 바꿔봅시다.")
    a8 = int(st.session_state["a8_p1"]*100)
    b8 = int(st.session_state["b8_p1"]*100)
    st.write("나누는 수와 나누어지는 수에 같은 수를 곱해도 답은 변하지 않는다는 점을 이용하면 자연수로 쉽게 바꿀 수 있답니다.")
    st.write("주의할 점은 나누어지는 수는 이미 자연수라도 나누는 수를 자연수로 만들기 위해 같은 수를 꼭 곱해줘야 한다는 것입니다.")
    st.write("지금 문제는 나누는 수와 나누어지는 수에 똑같이 100을 곱해주면 되겠네요.")
    st.write("그렇게 되면 ", int(st.session_state["a8_p1"]), "이 ", a8, "로 바뀌게 되고,")
    st.write(st.session_state["b8_p1"], "이 ", b8, "로 바뀌게 됩니다.")
    st.write("그렇다면 자연수의 나눗셈으로 바꾼 식을 풀어봅시다.")
    Q8_easy_Text = f"연습 8-1. {a8} \u00F7 {b8} ="
    st.markdown(Q8_easy_Text)
    answer3 = st.number_input("답 : ", key="3", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="c", on_click=make3, disabled=st.session_state["B27_p1"]): 
        if float(answer3) == float(st.session_state["x8_p1"]):
            st.write("정답입니다. 처음 문제를 방금 푼 자연수끼리의 나눗셈으로 바꾸듯이 자연수를 소수로 나누는 나눗셈은 자연수와 소수를 모두 소수점 이동하여 자연수끼리의 나눗셈으로 만들어 풀면 됩니다.")
        else:
            st.session_state["Q8_p1"] = st.session_state["Q8_p1"] + 1


if st.session_state["Q8_p1"] == 3:
    st.write("오답입니다. 자연수끼리의 나눗셈에도 어려움이 있거나 계산 실수가 있는 것 같네요. 더 연습해봅시다.")


Q8_Text_p2 = f'연습 8-2. {int(st.session_state["a8_p2"])} \u00F7 {st.session_state["b8_p2"]} ='
st.title(Q8_Text_p2)
answer1_p2 = st.number_input("답 : ", key="1_p2", value=None, placeholder="답을 입력하세요.", format="%f")

if "B25_p2" not in st.session_state:
    st.session_state["B25_p2"] = False
if "B26_p2" not in st.session_state:
    st.session_state["B26_p2"] = False
if "B27_p2" not in st.session_state:
    st.session_state["B27_p2"] = False

def make1_p2():
    st.session_state["B25_p2"] = True
def make2_p2():
    st.session_state["B26_p2"] = True
def make3_p2():
    st.session_state["B27_p2"] = True

if st.button("채점하기", key="a_p2", on_click=make1_p2, disabled=st.session_state["B25_p2"]):
    if float(answer1_p2) == float(st.session_state["x8_p2"]):
        st.write("정답입니다.")
    else:
        st.session_state["Q8_p2"] = st.session_state["Q8_p2"] + 1

if st.session_state["Q8_p2"] == 1:
    st.write("혹시 계산 실수가 있었나요? 천천히 계산해보고 다시 답을 입력해주세요.")
    answer2_p2 = st.number_input("답 : ", key="2_p2", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="b_p2", on_click=make2_p2, disabled=st.session_state["B26_p2"]):     
        if float(answer2_p2) == float(st.session_state["x8_p2"]):
            st.write("정답입니다.")
        else:
            st.session_state["Q8_p2"] = st.session_state["Q8_p2"] + 1
       

if st.session_state["Q8_p2"] == 2:    
    st.write("자연수를 소수로 나누는 나눗셈을 이해하는 데 어려움이 있는 것 같군요. 그렇다면 자연수끼리의 나눗셈으로 바꿔봅시다.")
    a8_p2 = int(st.session_state["a8_p2"]*100)
    b8_p2 = int(st.session_state["b8_p2"]*100)
    st.write("나누는 수와 나누어지는 수에 같은 수를 곱해도 답은 변하지 않는다는 점을 이용하면 자연수로 쉽게 바꿀 수 있답니다.")
    st.write("주의할 점은 나누어지는 수는 이미 자연수라도 나누는 수를 자연수로 만들기 위해 같은 수를 꼭 곱해줘야 한다는 것입니다.")
    st.write("지금 문제는 나누는 수와 나누어지는 수에 똑같이 100을 곱해주면 되겠네요.")
    st.write("그렇게 되면 ", int(st.session_state["a8_p2"]), "이 ", a8_p2, "로 바뀌게 되고,")
    st.write(st.session_state["b8_p2"], "이 ", b8_p2, "로 바뀌게 됩니다.")
    st.write("그렇다면 자연수의 나눗셈으로 바꾼 식을 풀어봅시다.")
    Q8_easy_Text_p2 = f"연습 8-2. {a8_p2} \u00F7 {b8_p2} ="
    st.markdown(Q8_easy_Text_p2)
    answer3_p2 = st.number_input("답 : ", key="3_p2", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="c_p2", on_click=make3_p2, disabled=st.session_state["B27_p2"]): 
        if float(answer3_p2) == float(st.session_state["x8_p2"]):
            st.write("정답입니다. 처음 문제를 방금 푼 자연수끼리의 나눗셈으로 바꾸듯이 자연수를 소수로 나누는 나눗셈은 자연수와 소수를 모두 소수점 이동하여 자연수끼리의 나눗셈으로 만들어 풀면 됩니다.")
        else:
            st.session_state["Q8_p2"] = st.session_state["Q8_p2"] + 1


if st.session_state["Q8_p2"] == 3:
    st.write("오답입니다. 자연수끼리의 나눗셈에도 어려움이 있거나 계산 실수가 있는 것 같네요. 더 연습해봅시다.")


practice = st.selectbox('연습하고 싶은 문제를 골라주세요.', st.session_state["R_Q_list"])
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

if st.button('분석 화면으로 돌아가기'):
    switch_page("Review")