import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd

Q11_Text = f'연습 11-1. {st.session_state["a11_p1"]} \u00F7 {st.session_state["b11_p1"]}의 {st.session_state["y11_p1"]}하시오.'
st.subheader(Q11_Text)
answer1 = st.number_input("답 : ", key="1", value=None, placeholder="답을 입력하세요.", format="%f")

if "right_answer2" not in st.session_state:
    st.session_state["right_answer2"] = 0
if "a11__1" not in st.session_state:
    st.session_state["a11__1"] = 0
if "b11__1" not in st.session_state:
    st.session_state["b11__1"] = 0

if "B33_p1" not in st.session_state:
    st.session_state["B33_p1"] = False
if "B34_p1" not in st.session_state:
    st.session_state["B34_p1"] = False
if "B35_p1" not in st.session_state:
    st.session_state["B35_p1"] = False
if "B36_p1" not in st.session_state:
    st.session_state["B36_p1"] = False
if "B37_p1" not in st.session_state:
    st.session_state["B37_p1"] = False
if "B38_p1" not in st.session_state:
    st.session_state["B38_p1"] = False


def make1():
    st.session_state["B33_p1"] = True
def make2():
    st.session_state["B34_p1"] = True
def make3():
    st.session_state["B35_p1"] = True
def make4():
    st.session_state["B36_p1"] = True
def make5():
    st.session_state["B37_p1"] = True
def make6():
    st.session_state["B38_p1"] = True

if "round_q1_p1" not in st.session_state:
    st.session_state["round_q1_p1"] = 0

if st.session_state['y11_2_p1'] == "소수 첫째 자리":
    st.session_state["round_q1_p1"] = 1
elif st.session_state['y11_2_p1'] == "소수 둘째 자리":
    st.session_state["round_q1_p1"] = 2


if st.button("채점하기", key="a", on_click=make1, disabled=st.session_state["B33_p1"]):
    if answer1 == None:
        answer1 = 0
    if float(answer1) == float(st.session_state["x11_p1"]):
        st.write("정답입니다.")
    else:
        st.session_state["Q11_p1"] = st.session_state["Q11_p1"] + 1


if st.session_state["Q11_p1"] == 1:
    st.write("혹시 계산 실수가 있었나요? 반올림을 해야 한다는 것을 생각하고 다시 답을 입력해주세요.")
    answer2 = st.number_input("답 : ", key="2", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="b", on_click=make2, disabled=st.session_state["B34_p1"]):     
        if answer2 == None:
            answer2 = 0
        if float(answer2) == float(st.session_state["x11_p1"]):
            st.write("정답입니다.")
        else:
            st.session_state["Q11_p1"] = st.session_state["Q11_p1"] + 1.1
       

if st.session_state["Q11_p1"] == 2.1:  
    st.write("몫을 반올림하여 구하는 데 어려움이 있는 것 같군요.")
    st.write("우선 몫을", st.session_state['y11_2_p1'], "까지 구한 후 답을 입력해봅시다.")
    Q11_easy_Text = f"연습 11-1. {st.session_state['a11_p1']} \u00F7 {st.session_state['b11_p1']}의 몫을 {st.session_state['y11_2_p1']}까지 구해보시오."
    st.markdown(Q11_easy_Text)
    answer3 = st.number_input("답 : ", key="3", value=None, placeholder="답을 입력하세요.", format="%f")
    st.session_state['right_answer2'] = float(st.session_state['a11_p1']/st.session_state['b11_p1'])
    st.session_state['right_answer2'] = f"{st.session_state['right_answer2']:.{st.session_state['round_q1_p1']}f}"
    if st.button("채점하기", key="c", on_click=make3, disabled=st.session_state["B35_p1"]): 
        if answer3 == None:
            answer3 = 0
        if float(answer3) == float(st.session_state['right_answer2']):
            st.write("정답입니다.")
            st.session_state["Q11_p1"] = st.session_state["Q11_p1"] + 0.4
        else:
            st.session_state["Q11_p1"] = st.session_state["Q11_p1"] + 1


if st.session_state["Q11_p1"] == 2.5:
    st.write("그럼 이제 구한 값을 반올림해보겠습니다. 특정 자리에서 반올림은 특정 자리가 4 이하면 버림, 5 이상이면 올림을 하면 됩니다.")
    st.write("방금 입력한 ", st.session_state['right_answer2'], "를 ", st.session_state['y11_2_p1'], "에서 반올림한 값을 입력해봅시다.")
    answer4 = st.number_input("답 : ", key="4", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="d", on_click=make4, disabled=st.session_state["B36_p1"]): 
        if answer4 == None:
            answer4 = 0
        if float(answer4) == float(st.session_state["x11_p1"]):
            st.write("정답입니다. 소수의 나눗셈에서 몫을 구하고 반올림을 할 수 있는데 2번이나 답을 틀린 것을 보니 반올림을 잘못 이해했거나 실수를 많이 한 것 같네요. 다음부터는 집중하여 문제를 풀도록 합시다.")
            st.session_state["Q11_p1"] = st.session_state["Q11_p1"] - 0.5
        else:
            st.write("오답입니다. 몫은 구할 수 있지만 반올림에 어려움이 있었군요.")
            st.write(st.session_state['right_answer2'], "를 ", st.session_state['y11_2_p1'], "에서 반올림하면 ", st.session_state['x11_p1'], "이 된답니다.")
            st.write("자신이 입력한 값과 비교해보면서 어떤 실수를 했는지 확인하고 더 연습해봅시다.")


if st.session_state["Q11_p1"] == 3.1:  
    st.write("소수의 나눗셈 자체에 어려움이 있는 것 같군요. 그렇다면 자연수로 바꿔서 나눗셈을 진행해봅시다.")
    st.session_state["a11__1"] = int(st.session_state["a11_p1"]*10)
    st.session_state["b11__1"] = int(st.session_state["b11_p1"]*10)
    st.write("나누는 수와 나누어지는 수에 같은 수를 곱해도 몫은 변하지 않는다는 점을 이용하면 자연수로 쉽게 바꿀 수 있답니다.")
    st.write("주의할 점은 나누어지는 수는 이미 자연수라도 나누는 수를 자연수로 만들기 위해 같은 수를 꼭 곱해줘야 한다는 것입니다.")
    st.write("지금 문제는 나누는 수와 나누어지는 수에 똑같이 10을 곱해주면 되겠네요.")
    st.write("그렇게 되면 ", st.session_state["a11_p1"], "이 ", st.session_state["a11__1"], "로 바뀌게 되고,")
    st.write(st.session_state["b11_p1"], "이 ", st.session_state["b11__1"], "로 바뀌게 됩니다.")
    st.write("그렇다면 자연수의 나눗셈으로 바꾼 후 몫을", st.session_state['y11_2_p1'], "까지 구한 후 답을 입력해봅시다.")
    Q11_easy_Text_2 = f"연습 11-1. {st.session_state['a11__1']} \u00F7 {st.session_state['b11__1']}의 {st.session_state['y11_p1']}하시오."
    st.markdown(Q11_easy_Text_2)
    answer5 = st.number_input("답 : ", key="5", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="e", on_click=make5, disabled=st.session_state["B37_p1"]): 
        if answer5 == None:
            answer5 = 0
        if float(answer5) == float(st.session_state['right_answer2']):
            st.write("정답입니다.")
            st.session_state["Q11_p1"] = st.session_state["Q11_p1"] + 0.4
        else:
            st.session_state["Q11_p1"] = st.session_state["Q11_p1"] + 0.9

if st.session_state["Q11_p1"] == 3.5:
    st.write("그럼 이제 구한 값을 반올림해보겠습니다. 특정 자리에서 반올림은 특정 자리가 4 이하면 버림, 5 이상이면 올림을 하면 됩니다.")
    st.write("방금 입력한 ", st.session_state['right_answer2'], "를 ", st.session_state['y11_2_p1'], "에서 반올림한 값을 입력해봅시다.")
    answer6 = st.number_input("답 : ", key="6", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="f", on_click=make6, disabled=st.session_state["B38_p1"]): 
        if answer6 == None:
            answer6 = 0
        if float(answer6) == float(st.session_state["x11_p1"]):
            st.write("정답입니다. 소수의 나눗셈에는 어려움이 있었지만 반올림에는 문제가 없었군요. 다음에는 자연수로 바꿔서 신중하게 계산해봅시다.")
            st.session_state["Q11_p1"] = st.session_state["Q11_p1"] - 0.5
        else:
            st.write("오답입니다. 소수의 나눗셈과 반올림에 모두 어려움이 있었군요.")
            st.write("그래도 반올림에 대해서는 다시 설명하겠습니다.")
            st.write(st.session_state['right_answer2'], "를 ", st.session_state['y11_2_p1'], "에서 반올림하면 ", st.session_state['x11_p1'], "이 된답니다.")
            st.write("자신이 입력한 값과 비교해보면서 어떤 실수를 했는지 확인하고 더 연습해봅시다.")

if st.session_state["Q11_p1"] == 4:
    st.write("오답입니다. 소수의 나눗셈과 반올림에 모두 어려움이 있었군요.")
    st.write("그래도 반올림에 대해서는 다시 설명하겠습니다. 특정 자리에서 반올림은 특정 자리가 4 이하면 버림, 5 이상이면 올림을 하면 됩니다.")
    st.write("위에서 풀지 못한 문제의 답을 이용해 반올림 과정을 살펴봅시다.")
    st.write(f"{st.session_state['a11__1']} \u00F7 {st.session_state['b11__1']}의 {st.session_state['y11_p1']}하면 답은 {st.session_state['right_answer2']}가 됩니다.")
    st.write("이때 ", st.session_state['right_answer2'], "를 ", st.session_state['y11_2_p1'], "에서 반올림하면 ", st.session_state['x11_p1'], "이 된답니다.")
    st.write("자신이 입력한 값과 비교해보면서 어떤 부분을 잘 몰랐는지 확인하고 더 연습해봅시다.")


Q11_Text_p2 = f'연습 11-2. {st.session_state["a11_p2"]} \u00F7 {st.session_state["b11_p2"]}의 {st.session_state["y11_p2"]}하시오.'
st.subheader(Q11_Text_p2)
answer1_p2 = st.number_input("답 : ", key="1_p2", value=None, placeholder="답을 입력하세요.", format="%f")

if "right_answer3" not in st.session_state:
    st.session_state["right_answer3"] = 0
if "a11__2" not in st.session_state:
    st.session_state["a11__2"] = 0
if "b11__2" not in st.session_state:
    st.session_state["b11__2"] = 0

if "B33_p2" not in st.session_state:
    st.session_state["B33_p2"] = False
if "B34_p2" not in st.session_state:
    st.session_state["B34_p2"] = False
if "B35_p2" not in st.session_state:
    st.session_state["B35_p2"] = False
if "B36_p2" not in st.session_state:
    st.session_state["B36_p2"] = False
if "B37_p2" not in st.session_state:
    st.session_state["B37_p2"] = False
if "B38_p2" not in st.session_state:
    st.session_state["B38_p2"] = False


def make1_p2():
    st.session_state["B33_p2"] = True
def make2_p2():
    st.session_state["B34_p2"] = True
def make3_p2():
    st.session_state["B35_p2"] = True
def make4_p2():
    st.session_state["B36_p2"] = True
def make5_p2():
    st.session_state["B37_p2"] = True
def make6_p2():
    st.session_state["B38_p2"] = True

if "round_q1_p2" not in st.session_state:
    st.session_state["round_q1_p2"] = 0

if st.session_state['y11_2_p2'] == "소수 첫째 자리":
    st.session_state["round_q1_p2"] = 1
elif st.session_state['y11_2_p2'] == "소수 둘째 자리":
    st.session_state["round_q1_p2"] = 2


if st.button("채점하기", key="a_p2", on_click=make1_p2, disabled=st.session_state["B33_p2"]):
    if answer1_p2 == None:
        answer1_p2 = 0
    if float(answer1_p2) == float(st.session_state["x11_p2"]):
        st.write("정답입니다.")
    else:
        st.session_state["Q11_p2"] = st.session_state["Q11_p2"] + 1


if st.session_state["Q11_p2"] == 1:
    st.write("혹시 계산 실수가 있었나요? 반올림을 해야 한다는 것을 생각하고 다시 답을 입력해주세요.")
    answer2_p2 = st.number_input("답 : ", key="2_p2", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="b_p2", on_click=make2_p2, disabled=st.session_state["B34_p2"]):     
        if answer2_p2 == None:
            answer2_p2 = 0
        if float(answer2_p2) == float(st.session_state["x11_p2"]):
            st.write("정답입니다.")
        else:
            st.session_state["Q11_p2"] = st.session_state["Q11_p2"] + 1.1
       

if st.session_state["Q11_p2"] == 2.1:  
    st.write("몫을 반올림하여 구하는 데 어려움이 있는 것 같군요.")
    st.write("우선 몫을", st.session_state['y11_2_p2'], "까지 구한 후 답을 입력해봅시다.")
    Q11_easy_Text_p2 = f"연습 11-2. {st.session_state['a11_p2']} \u00F7 {st.session_state['b11_p2']}의 몫을 {st.session_state['y11_2_p2']}까지 구해보시오."
    st.markdown(Q11_easy_Text_p2)
    answer3_p2 = st.number_input("답 : ", key="3_p2", value=None, placeholder="답을 입력하세요.", format="%f")
    st.session_state["right_answer3"] = float(st.session_state['a11_p2']/st.session_state['b11_p2'])
    st.session_state["right_answer3"] = f"{st.session_state['right_answer3']:.{st.session_state['round_q1_p2']}f}"
    if st.button("채점하기", key="c_p2", on_click=make3_p2, disabled=st.session_state["B35_p2"]): 
        if answer3_p2 == None:
            answer3_p2 = 0
        if float(answer3_p2) == float(st.session_state["right_answer3"]):
            st.write("정답입니다.")
            st.session_state["Q11_p2"] = st.session_state["Q11_p2"] + 0.4
        else:
            st.session_state["Q11_p2"] = st.session_state["Q11_p2"] + 1


if st.session_state["Q11_p2"] == 2.5:
    st.write("그럼 이제 구한 값을 반올림해보겠습니다. 특정 자리에서 반올림은 특정 자리가 4 이하면 버림, 5 이상이면 올림을 하면 됩니다.")
    st.write("방금 입력한 ", st.session_state['right_answer3'], "를 ", st.session_state['y11_2_p2'], "에서 반올림한 값을 입력해봅시다.")
    answer4_p2 = st.number_input("답 : ", key="4_p2", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="d_p2", on_click=make4_p2, disabled=st.session_state["B36_p2"]):
        if answer4_p2 == None:
            answer4_p2 = 0 
        if float(answer4_p2) == float(st.session_state["x11_p2"]):
            st.write("정답입니다. 소수의 나눗셈에서 몫을 구하고 반올림을 할 수 있는데 2번이나 답을 틀린 것을 보니 반올림을 잘못 이해했거나 실수를 많이 한 것 같네요. 다음부터는 집중하여 문제를 풀도록 합시다.")
            st.session_state["Q11_p2"] = st.session_state["Q11_p2"] - 0.5
        else:
            st.write("오답입니다. 몫은 구할 수 있지만 반올림에 어려움이 있었군요.")
            st.write(st.session_state["right_answer3"], "를 ", st.session_state['y11_2_p2'], "에서 반올림하면 ", st.session_state['x11_p2'], "이 된답니다.")
            st.write("자신이 입력한 값과 비교해보면서 어떤 실수를 했는지 확인하고 더 연습해봅시다.")


if st.session_state["Q11_p2"] == 3.1:  
    st.write("소수의 나눗셈 자체에 어려움이 있는 것 같군요. 그렇다면 자연수로 바꿔서 나눗셈을 진행해봅시다.")
    st.session_state['a11__2'] = int(st.session_state["a11_p2"]*10)
    st.session_state['b11__2'] = int(st.session_state["b11_p2"]*10)
    st.write("나누는 수와 나누어지는 수에 같은 수를 곱해도 몫은 변하지 않는다는 점을 이용하면 자연수로 쉽게 바꿀 수 있답니다.")
    st.write("주의할 점은 나누어지는 수는 이미 자연수라도 나누는 수를 자연수로 만들기 위해 같은 수를 꼭 곱해줘야 한다는 것입니다.")
    st.write("지금 문제는 나누는 수와 나누어지는 수에 똑같이 10을 곱해주면 되겠네요.")
    st.write("그렇게 되면 ", st.session_state["a11_p2"], "이 ", st.session_state['a11__2'], "로 바뀌게 되고,")
    st.write(st.session_state["b11_p2"], "이 ", st.session_state['b11__2'], "로 바뀌게 됩니다.")
    st.write("그렇다면 자연수의 나눗셈으로 바꾼 후 몫을", st.session_state['y11_2_p2'], "까지 구한 후 답을 입력해봅시다.")
    Q11_easy_Text_2_p2 = f"연습 11-2. {st.session_state['a11__2']} \u00F7 {st.session_state['b11__2']}의 {st.session_state['y11_p2']}하시오."
    st.markdown(Q11_easy_Text_2_p2)
    answer5_p2 = st.number_input("답 : ", key="5_p2", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="e_p2", on_click=make5_p2, disabled=st.session_state["B37_p2"]):
        if answer5_p2 == None:
            answer5_p2 = 0 
        if float(answer5_p2) == float(st.session_state["right_answer3"]):
            st.write("정답입니다.")
            st.session_state["Q11_p2"] = st.session_state["Q11_p2"] + 0.4
        else:
            st.session_state["Q11_p2"] = st.session_state["Q11_p2"] + 0.9

if st.session_state["Q11_p2"] == 3.5:
    st.write("그럼 이제 구한 값을 반올림해보겠습니다. 특정 자리에서 반올림은 특정 자리가 4 이하면 버림, 5 이상이면 올림을 하면 됩니다.")
    st.write("방금 입력한 ", st.session_state["right_answer3"], "를 ", st.session_state['y11_2_p2'], "에서 반올림한 값을 입력해봅시다.")
    answer6_p2 = st.number_input("답 : ", key="6_p2", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="f", on_click=make6_p2, disabled=st.session_state["B38_p2"]): 
        if answer6_p2 == None:
            answer6_p2 = 0
        if float(answer6_p2) == float(st.session_state["x11_p2"]):
            st.write("정답입니다. 소수의 나눗셈에는 어려움이 있었지만 반올림에는 문제가 없었군요. 다음에는 자연수로 바꿔서 신중하게 계산해봅시다.")
            st.session_state["Q11_p2"] = st.session_state["Q11_p2"] - 0.5
        else:
            st.write("오답입니다. 소수의 나눗셈과 반올림에 모두 어려움이 있었군요.")
            st.write("그래도 반올림에 대해서는 다시 설명하겠습니다.")
            st.write(st.session_state["right_answer3"], "를 ", st.session_state['y11_2_p2'], "에서 반올림하면 ", st.session_state['x11_p2'], "이 된답니다.")
            st.write("자신이 입력한 값과 비교해보면서 어떤 실수를 했는지 확인하고 더 연습해봅시다.")

if st.session_state["Q11_p2"] == 4:
    st.write("오답입니다. 소수의 나눗셈과 반올림에 모두 어려움이 있었군요.")
    st.write("그래도 반올림에 대해서는 다시 설명하겠습니다. 특정 자리에서 반올림은 특정 자리가 4 이하면 버림, 5 이상이면 올림을 하면 됩니다.")
    st.write("위에서 풀지 못한 문제의 답을 이용해 반올림 과정을 살펴봅시다.")
    st.write(f"{st.session_state['a11__2']} \u00F7 {st.session_state['b11__2']}의 {st.session_state['y11_p2']}하면 답은 {st.session_state["right_answer3"]}가 됩니다.")
    st.write("이때 ", st.session_state["right_answer3"], "를 ", st.session_state['y11_2_p2'], "에서 반올림하면 ", st.session_state['x11_p2'], "이 된답니다.")
    st.write("자신이 입력한 값과 비교해보면서 어떤 부분을 잘 몰랐는지 확인하고 더 연습해봅시다.")

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
