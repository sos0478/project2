import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd

Q11_Text = f'11. {st.session_state["a11"]} \u00F7 {st.session_state["b11"]}의 {st.session_state["y11"]}하시오.'
st.subheader(Q11_Text)
answer1 = st.number_input("답 : ", key="1", value=None, placeholder="답을 입력하세요.", format="%f")

if "N11" not in st.session_state:
    st.session_state["N11"] = True

if "B33" not in st.session_state:
    st.session_state["B33"] = False
if "B34" not in st.session_state:
    st.session_state["B34"] = False
if "B35" not in st.session_state:
    st.session_state["B35"] = False
if "B36" not in st.session_state:
    st.session_state["B36"] = False
if "B37" not in st.session_state:
    st.session_state["B37"] = False
if "B38" not in st.session_state:
    st.session_state["B38"] = False


def make1():
    st.session_state["B33"] = True
def make2():
    st.session_state["B34"] = True
def make3():
    st.session_state["B35"] = True
def make4():
    st.session_state["B36"] = True
def make5():
    st.session_state["B37"] = True
def make6():
    st.session_state["B38"] = True

if "round_q1" not in st.session_state:
    st.session_state["round_q1"] = 0

if st.session_state['y11_2'] == "소수 첫째 자리":
    st.session_state["round_q1"] = 1
elif st.session_state['y11_2'] == "소수 둘째 자리":
    st.session_state["round_q1"] = 2


if st.button("채점하기", key="a", on_click=make1, disabled=st.session_state["B33"]):
    if answer1 == None:
        answer1 = 0
    if float(answer1) == float(st.session_state["x11"]):
        st.session_state["C11"] = st.session_state["C11"] + 1
        st.session_state["N11"] = False
        st.write("정답입니다.")
    else:
        st.session_state["Q11"] = st.session_state["Q11"] + 1


if st.session_state["Q11"] == 1:
    st.write("혹시 계산 실수가 있었나요? 반올림을 해야 한다는 것을 생각하고 다시 답을 입력해주세요.")
    answer2 = st.number_input("답 : ", key="2", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="b", on_click=make2, disabled=st.session_state["B34"]):   
        if answer2 == None:
            answer2 = 0  
        if float(answer2) == float(st.session_state["x11"]):
            st.session_state["C11"] = st.session_state["C11"] + 1
            st.session_state["N11"] = False
            st.write("정답입니다.")
        else:
            st.session_state["Q11"] = st.session_state["Q11"] + 1.1
       

if st.session_state["Q11"] == 2.1:  
    st.write("몫을 반올림하여 구하는 데 어려움이 있는 것 같군요.")
    st.write("우선 몫을", st.session_state['y11_2'], "까지 구한 후 답을 입력해봅시다.")
    Q11_easy_Text = f"11. {st.session_state['a11']} \u00F7 {st.session_state['b11']}의 몫을 {st.session_state['y11_2']}까지 구해보시오."
    st.markdown(Q11_easy_Text)
    answer3 = st.number_input("답 : ", key="3", value=None, placeholder="답을 입력하세요.", format="%f")
    right_answer = float(st.session_state['a11']/st.session_state['b11'])
    right_answer = f"{right_answer:.{st.session_state['round_q1']}f}"
    if st.button("채점하기", key="c", on_click=make3, disabled=st.session_state["B35"]): 
        if answer3 == None:
            answer3 = 0
        if float(answer3) == float(right_answer):
            st.write("정답입니다.")
            st.session_state["Q11"] = st.session_state["Q11"] + 0.4
        else:
            st.session_state["Q11"] = st.session_state["Q11"] + 1


if st.session_state["Q11"] == 2.5:
    st.write("그럼 이제 구한 값을 반올림해보겠습니다. 특정 자리에서 반올림은 특정 자리가 4 이하면 버림, 5 이상이면 올림을 하면 됩니다.")
    st.write("방금 입력한 ", right_answer, "를 ", st.session_state['y11_2'], "에서 반올림한 값을 입력해봅시다.")
    answer4 = st.number_input("답 : ", key="4", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="d", on_click=make4, disabled=st.session_state["B36"]): 
        if answer4 == None:
            answer4 = 0
        if float(answer4) == float(st.session_state["x11"]):
            st.session_state["N11"] = False
            st.write("정답입니다. 소수의 나눗셈에서 몫을 구하고 반올림을 할 수 있는데 2번이나 답을 틀린 것을 보니 반올림을 잘못 이해했거나 실수를 많이 한 것 같네요. 다음부터는 집중하여 문제를 풀도록 합시다.")
            st.session_state["Q11"] = st.session_state["Q11"] - 0.5
        else:
            st.session_state["N11"] = False
            st.write("오답입니다. 몫은 구할 수 있지만 반올림에 어려움이 있었군요.")
            st.write(right_answer, "를 ", st.session_state['y11_2'], "에서 반올림하면 ", st.session_state['x11'], "이 된답니다.")
            st.write("자신이 입력한 값과 비교해보면서 어떤 실수를 했는지 확인하고 다음 문제로 넘어가도록 합시다.")


if st.session_state["Q11"] == 3.1:  
    st.write("소수의 나눗셈 자체에 어려움이 있는 것 같군요. 그렇다면 자연수로 바꿔서 나눗셈을 진행해봅시다.")
    a11 = int(st.session_state["a11"]*10)
    b11 = int(st.session_state["b11"]*10)
    st.write("나누는 수와 나누어지는 수에 같은 수를 곱해도 몫은 변하지 않는다는 점을 이용하면 자연수로 쉽게 바꿀 수 있답니다.")
    st.write("주의할 점은 나누어지는 수는 이미 자연수라도 나누는 수를 자연수로 만들기 위해 같은 수를 꼭 곱해줘야 한다는 것입니다.")
    st.write("지금 문제는 나누는 수와 나누어지는 수에 똑같이 10을 곱해주면 되겠네요.")
    st.write("그렇게 되면 ", st.session_state["a11"], "이 ", a11, "로 바뀌게 되고,")
    st.write(st.session_state["b11"], "이 ", b11, "로 바뀌게 됩니다.")
    st.write("그렇다면 자연수의 나눗셈으로 바꾼 후 몫을", st.session_state['y11_2'], "까지 구한 후 답을 입력해봅시다.")
    Q11_easy_Text_2 = f"11. {a11} \u00F7 {b11}의 {st.session_state['y11']}하시오."
    st.markdown(Q11_easy_Text_2)
    answer5 = st.number_input("답 : ", key="5", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="e", on_click=make5, disabled=st.session_state["B37"]): 
        if answer5 == None:
            answer5 = 0
        if float(answer5) == float(right_answer):
            st.write("정답입니다.")
            st.session_state["Q11"] = st.session_state["Q11"] + 0.4
        else:
            st.session_state["Q11"] = st.session_state["Q11"] + 0.9

if st.session_state["Q11"] == 3.5:
    st.write("그럼 이제 구한 값을 반올림해보겠습니다. 특정 자리에서 반올림은 특정 자리가 4 이하면 버림, 5 이상이면 올림을 하면 됩니다.")
    st.write("방금 입력한 ", right_answer, "를 ", st.session_state['y11_2'], "에서 반올림한 값을 입력해봅시다.")
    answer6 = st.number_input("답 : ", key="6", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="f", on_click=make6, disabled=st.session_state["B38"]):
        if answer6 == None:
            answer6 = 0 
        if float(answer6) == float(st.session_state["x11"]):
            st.session_state["N11"] = False
            st.write("정답입니다. 소수의 나눗셈에는 어려움이 있었지만 반올림에는 문제가 없었군요. 다음에는 자연수로 바꿔서 신중하게 계산해봅시다.")
            st.session_state["Q11"] = st.session_state["Q11"] - 0.5
        else:
            st.session_state["N11"] = False
            st.write("오답입니다. 소수의 나눗셈과 반올림에 모두 어려움이 있었군요.")
            st.write("그래도 반올림에 대해서는 다시 설명하겠습니다.")
            st.write(right_answer, "를 ", st.session_state['y11_2'], "에서 반올림하면 ", st.session_state['x11'], "이 된답니다.")
            st.write("자신이 입력한 값과 비교해보면서 어떤 실수를 했는지 확인하고 다음 문제로 넘어가도록 합시다.")

if st.session_state["Q11"] == 4:
    st.session_state["N11"] = False
    st.write("오답입니다. 소수의 나눗셈과 반올림에 모두 어려움이 있었군요.")
    st.write("그래도 반올림에 대해서는 다시 설명하겠습니다. 특정 자리에서 반올림은 특정 자리가 4 이하면 버림, 5 이상이면 올림을 하면 됩니다.")
    st.write("위에서 풀지 못한 문제의 답을 이용해 반올림 과정을 살펴봅시다.")
    st.write(f"{a11} \u00F7 {b11}의 {st.session_state['y11']}하면 답은 {right_answer}가 됩니다.")
    st.write("이때 ", right_answer, "를 ", st.session_state['y11_2'], "에서 반올림하면 ", st.session_state['x11'], "이 된답니다.")
    st.write("자신이 입력한 값과 비교해보면서 어떤 부분을 잘 몰랐는지 확인하고 다음 문제로 넘어가도록 합시다.")


st.write("채점을 마친 후에만 클릭하여 다음 문제로 넘어갈 수 있습니다.")
if st.button("다음 문제로 넘어가기", disabled=st.session_state["N11"]):
    switch_page("Q12")