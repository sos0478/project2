import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd

Q14_Text = f'연습 14-1. {st.session_state["a14_p1"]} \u00F7 {st.session_state["b14_p1"]}의 {st.session_state["y14_p1"]}.'
st.subheader(Q14_Text)
answer1 = st.number_input("답 : ", key="1", value=None, placeholder="답을 입력하세요.", format="%f")

if 'a14__1' not in st.session_state:
    st.session_state['a14__1'] = 0
if 'b14__1' not in st.session_state:
    st.session_state['b14__1'] = 0

if "B52_p1" not in st.session_state:
    st.session_state["B52_p1"] = False
if "B53_p1" not in st.session_state:
    st.session_state["B53_p1"] = False
if "B54_p1" not in st.session_state:
    st.session_state["B54_p1"] = False
if "B55_p1" not in st.session_state:
    st.session_state["B55_p1"] = False
if "B56_p1" not in st.session_state:
    st.session_state["B56_p1"] = False
if "B57_p1" not in st.session_state:
    st.session_state["B57_p1"] = False


def make1():
    st.session_state["B52_p1"] = True
def make2():
    st.session_state["B53_p1"] = True
def make3():
    st.session_state["B54_p1"] = True
def make4():
    st.session_state["B55_p1"] = True
def make5():
    st.session_state["B56_p1"] = True
def make6():
    st.session_state["B57_p1"] = True


if st.button("채점하기", key="a", on_click=make1, disabled=st.session_state["B52_p1"]):
    if answer1 == None:
        answer1 = 0
    if float(answer1) == float(st.session_state["x14_p1"]):
        st.write("정답입니다.")
    else:
        st.session_state["Q14_p1"] = st.session_state["Q14_p1"] + 1


if st.session_state["Q14_p1"] == 1:
    st.write("혹시 계산 실수가 있었나요? 몫이 아니라 나머지를 구해야 한다는 것을 생각하고 다시 답을 입력해주세요.")
    answer2 = st.number_input("답 : ", key="2", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="b", on_click=make2, disabled=st.session_state["B53_p1"]):    
        if answer2 == None:
            answer2 = 0 
        if float(answer2) == float(st.session_state["x14_p1"]):
            st.write("정답입니다.")
        else:
            st.session_state["Q14_p1"] = st.session_state["Q14_p1"] + 1.1
       

if st.session_state["Q14_p1"] == 2.1:  
    st.write("나머지를 구하는 데 어려움이 있는 것 같군요.")
    st.write("이전처럼 소수의 나눗셈을 자연수로 바꾸면 몫은 유지되지만 나머지는 바뀌기 때문에 다른 방법으로 접근해봅시다.")
    st.write("우선 몫을 자연수 부분까지만 구한 후 답을 입력해봅시다.")
    Q14_easy_Text = f"연습 14-1. {st.session_state['a14_p1']} \u00F7 {st.session_state['b14_p1']}의 몫을 자연수 부분까지 구해보시오."
    st.markdown(Q14_easy_Text)
    answer3 = st.number_input("답 : ", key="3", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="c", on_click=make3, disabled=st.session_state["B54_p1"]): 
        if answer3 == None:
            answer3 = 0
        if int(answer3) == int(st.session_state['y14_2_p1']):
            st.write("정답입니다.")
            st.session_state["Q14_p1"] = st.session_state["Q14_p1"] + 0.4
        else:
            st.session_state["Q14_p1"] = st.session_state["Q14_p1"] + 1


if st.session_state["Q14_p1"] == 2.5:
    st.write("그럼 이제 몫의 자연수 부분을 이용하여 나머지를 구해봅시다.")
    st.write("방금 입력한 몫의 자연수 부분인 ", int(st.session_state['y14_2_p1']), "를 나누는 수인 ", st.session_state['b14_p1'], "에 곱해서 나누어지는 수인 ", st.session_state['a14_p1'], "에서 빼주면 됩니다.")
    st.write(Q14_Text)
    answer4 = st.number_input("답 : ", key="4", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="d", on_click=make4, disabled=st.session_state["B55_p1"]): 
        if answer4 == None:
            answer4 = 0
        if float(answer4) == float(st.session_state["x14_p1"]):
            st.write("정답입니다. 나머지는 이렇게 자연수 부분까지 몫을 구한 후 나누는 수에 곱해서 나누어지는 수에서 빼는 식으로 구할 수 있습니다.")
            st.write("하지만 더 쉬운 방법으로는 자연수 부분까지 몫을 구하는 과정을 세로셈으로 똑같이 한 후, 나누어지는 수의 소수점을 그대로 내려서 구한 나머지에 소수점을 찍어도 됩니다.")
            st.write("이 사실을 기억하면서 더 연습해봅시다.")
            st.session_state["Q14_p1"] = st.session_state["Q14_p1"] - 0.5
        else:
            st.write("오답입니다. 나머지를 구하는 방식을 이해하지 못하거나 계산 실수가 있었군요.")
            st.write("7을 2로 나누고 남은 나머지를 구할 때 7에서 몫인 3에 2를 곱한 후 빼주듯이")
            st.write(st.session_state['a14_p1'], "에서 ", int(st.session_state['y14_2_p1']), "에 ", st.session_state['b14_p1'], "를 곱하면 ", st.session_state['x14_p1'], "이 된답니다.")
            st.write("자신이 입력한 값과 비교해보면서 어떤 부분을 놓쳤는지 확인하고 더 연습해봅시다.")


if st.session_state["Q14_p1"] == 3.1:  
    st.write("소수의 나눗셈에서 몫을 자연수 부분을 나누는 방법에도 어려움이 있는 것 같군요. 몫의 자연수 부분까지만 구하는 것은 자연수의 나눗셈으로 바꾸어서 계산해도 괜찮습니다.")
    st.session_state['a14__1'] = int(st.session_state["a14_p1"]*100)
    st.session_state['b14__1'] = int(st.session_state["b14_p1"]*100)
    st.write("나누는 수와 나누어지는 수에 같은 수를 곱해도 몫은 변하지 않는다는 점을 이용하면 자연수로 쉽게 바꿀 수 있답니다.")
    st.write("주의할 점은 나누어지는 수는 이미 자연수라도 나누는 수를 자연수로 만들기 위해 같은 수를 꼭 곱해줘야 한다는 것입니다.")
    st.write("지금 문제는 나누는 수와 나누어지는 수에 똑같이 100을 곱해주면 되겠네요.")
    st.write("그렇게 되면 ", st.session_state["a14_p1"], "이 ", st.session_state['a14__1'], "로 바뀌게 되고,")
    st.write(st.session_state["b14_p1"], "이 ", st.session_state['b14__1'], "로 바뀌게 됩니다.")
    st.write("그렇다면 자연수의 나눗셈으로 바꾼 후 몫을 자연수 부분까지 구한 후 답을 입력해봅시다.")
    Q14_easy_Text_2 = f"연습 14-1. {st.session_state['a14__1']} \u00F7 {st.session_state['b14__1']}의 몫을 자연수 부분까지 구해보시오."
    st.markdown(Q14_easy_Text_2)
    answer5 = st.number_input("답 : ", key="5", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="e", on_click=make5, disabled=st.session_state["B56_p1"]): 
        if answer5 == None:
            answer5 = 0
        if int(answer5) == int(st.session_state['y14_2_p1']):
            st.write("정답입니다.")
            st.session_state["Q14_p1"] = st.session_state["Q14_p1"] + 0.4
        else:
            st.session_state["Q14_p1"] = st.session_state["Q14_p1"] + 0.9

if st.session_state["Q14_p1"] == 3.5:
    st.write("그럼 이제 몫의 자연수 부분을 이용하여 나머지를 구해봅시다. 나머지를 구할 때는 몫의 자연수 부분을 구하느라 자연수로 바꾸었던 숫자를 다시 소수로 돌려놓고 생각해야 합니다.")
    st.write("방금 입력한 몫의 자연수 부분인 ", int(st.session_state['y14_2_p1']), "를 나누는 수인 ", st.session_state['b14_p1'], "에 곱해서 나누어지는 수인 ", st.session_state['a14_p1'], "에서 빼주면 됩니다.")
    st.write(Q14_Text)
    answer6 = st.number_input("답 : ", key="6", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="f", on_click=make6, disabled=st.session_state["B57_p1"]): 
        if answer6 == None:
            answer6 = 0
        if float(answer6) == float(st.session_state["x14_p1"]):
            st.write("정답입니다. 나머지는 이렇게 자연수 부분까지 몫을 구한 후 나누는 수에 곱해서 나누어지는 수에서 빼는 식으로 구할 수 있습니다.")
            st.write("하지만 더 쉬운 방법으로는 자연수 부분까지 몫을 구하는 과정을 세로셈으로 똑같이 한 후, 나누어지는 수의 소수점을 그대로 내려서 구한 나머지에 소수점을 찍어도 됩니다.")
            st.write("이 사실을 기억하면서 더 연습해봅시다.")
            st.session_state["Q14_p1"] = st.session_state["Q14_p1"] - 0.5
        else:
            st.write("오답입니다. 나머지를 구하는 방식을 이해하지 못하거나 계산 실수가 있었군요.")
            st.write("7을 2로 나누고 남은 나머지를 구할 때 7에서 몫인 3에 2를 곱한 후 빼주듯이")
            st.write(st.session_state['a14_p1'], "에서 ", int(st.session_state['y14_2_p1']), "에 ", st.session_state['b14_p1'], "를 곱한 후 빼주면 ", st.session_state['x14_p1'], "이 된답니다.")
            st.write("자신이 입력한 값과 비교해보면서 어떤 부분을 놓쳤는지 확인하고 더 연습해봅시다.")

if st.session_state["Q14_p1"] == 4:
    st.write("오답입니다. 소수의 나눗셈과 나머지를 구하는 것에 모두 어려움이 있었군요.")
    st.write("그래도 나머지를 구하는 방법에 대해서는 다시 설명하겠습니다.")    
    st.write("위에서 풀지 못한 문제의 답을 이용해 나머지를 구하는 과정을 살펴봅시다.")
    st.write(f"{st.session_state['a14__1']} \u00F7 {st.session_state['b14__1']}의 몫을 자연수 부분까지 구하면 답은 {int(st.session_state['y14_2_p1'])}가 됩니다.")
    st.write("7을 2로 나누고 남은 나머지를 구할 때 7에서 몫인 3에 2를 곱한 후 빼주듯이")
    st.write(st.session_state['a14_p1'], "에서 ", int(st.session_state['y14_2_p1']), "에 ", st.session_state['b14_p1'], "를 곱한 후 빼주면 ", st.session_state['x14_p1'], "이 된답니다.")
    st.write("자신이 입력한 값과 비교해보면서 어떤 부분을 잘 몰랐는지 확인하고 더 연습해봅시다.")


Q14_Text_p2 = f'연습 14-2. {st.session_state["a14_p2"]} \u00F7 {st.session_state["b14_p2"]}의 {st.session_state["y14_p2"]}.'
st.subheader(Q14_Text_p2)
answer1_p2 = st.number_input("답 : ", key="1_p2", value=None, placeholder="답을 입력하세요.", format="%f")

if 'a14__2' not in st.session_state:
    st.session_state['a14__2'] = 0
if 'b14__2' not in st.session_state:
    st.session_state['b14__2'] = 0

if "B52_p2" not in st.session_state:
    st.session_state["B52_p2"] = False
if "B53_p2" not in st.session_state:
    st.session_state["B53_p2"] = False
if "B54_p2" not in st.session_state:
    st.session_state["B54_p2"] = False
if "B55_p2" not in st.session_state:
    st.session_state["B55_p2"] = False
if "B56_p2" not in st.session_state:
    st.session_state["B56_p2"] = False
if "B57_p2" not in st.session_state:
    st.session_state["B57_p2"] = False


def make1_p2():
    st.session_state["B52_p2"] = True
def make2_p2():
    st.session_state["B53_p2"] = True
def make3_p2():
    st.session_state["B54_p2"] = True
def make4_p2():
    st.session_state["B55_p2"] = True
def make5_p2():
    st.session_state["B56_p2"] = True
def make6_p2():
    st.session_state["B57_p2"] = True


if st.button("채점하기", key="a_p2", on_click=make1_p2, disabled=st.session_state["B52_p2"]):
    if answer1_p2 == None:
        answer1_p2 = 0
    if float(answer1_p2) == float(st.session_state["x14_p2"]):
        st.write("정답입니다.")
    else:
        st.session_state["Q14_p2"] = st.session_state["Q14_p2"] + 1


if st.session_state["Q14_p2"] == 1:
    st.write("혹시 계산 실수가 있었나요? 몫이 아니라 나머지를 구해야 한다는 것을 생각하고 다시 답을 입력해주세요.")
    answer2_p2 = st.number_input("답 : ", key="2_p2", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="b_p2", on_click=make2_p2, disabled=st.session_state["B53_p2"]):     
        if answer2_p2 == None:
            answer2_p2 = 0
        if float(answer2_p2) == float(st.session_state["x14_p2"]):
            st.write("정답입니다.")
        else:
            st.session_state["Q14_p2"] = st.session_state["Q14_p2"] + 1.1
       

if st.session_state["Q14_p2"] == 2.1:  
    st.write("나머지를 구하는 데 어려움이 있는 것 같군요.")
    st.write("이전처럼 소수의 나눗셈을 자연수로 바꾸면 몫은 유지되지만 나머지는 바뀌기 때문에 다른 방법으로 접근해봅시다.")
    st.write("우선 몫을 자연수 부분까지만 구한 후 답을 입력해봅시다.")
    Q14_easy_Text_p2 = f"연습 14-2. {st.session_state['a14_p2']} \u00F7 {st.session_state['b14_p2']}의 몫을 자연수 부분까지 구해보시오."
    st.markdown(Q14_easy_Text_p2)
    answer3_p2 = st.number_input("답 : ", key="3_p2", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="c_p2", on_click=make3_p2, disabled=st.session_state["B54_p2"]): 
        if answer3_p2 == None:
            answer3_p2 = 0
        if int(answer3_p2) == int(st.session_state['y14_2_p2']):
            st.write("정답입니다.")
            st.session_state["Q14_p2"] = st.session_state["Q14_p2"] + 0.4
        else:
            st.session_state["Q14_p2"] = st.session_state["Q14_p2"] + 1


if st.session_state["Q14_p2"] == 2.5:
    st.write("그럼 이제 몫의 자연수 부분을 이용하여 나머지를 구해봅시다.")
    st.write("방금 입력한 몫의 자연수 부분인 ", int(st.session_state['y14_2_p2']), "를 나누는 수인 ", st.session_state['b14_p2'], "에 곱해서 나누어지는 수인 ", st.session_state['a14_p2'], "에서 빼주면 됩니다.")
    st.write(Q14_Text_p2)
    answer4_p2 = st.number_input("답 : ", key="4_p2", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="d_p2", on_click=make4_p2, disabled=st.session_state["B55_p2"]): 
        if answer4_p2 == None:
            answer4_p2 = 0
        if float(answer4_p2) == float(st.session_state["x14_p2"]):
            st.write("정답입니다. 나머지는 이렇게 자연수 부분까지 몫을 구한 후 나누는 수에 곱해서 나누어지는 수에서 빼는 식으로 구할 수 있습니다.")
            st.write("하지만 더 쉬운 방법으로는 자연수 부분까지 몫을 구하는 과정을 세로셈으로 똑같이 한 후, 나누어지는 수의 소수점을 그대로 내려서 구한 나머지에 소수점을 찍어도 됩니다.")
            st.write("이 사실을 기억하면서 더 연습해봅시다.")
            st.session_state["Q14_p2"] = st.session_state["Q14_p2"] - 0.5
        else:
            st.write("오답입니다. 나머지를 구하는 방식을 이해하지 못하거나 계산 실수가 있었군요.")
            st.write("7을 2로 나누고 남은 나머지를 구할 때 7에서 몫인 3에 2를 곱한 후 빼주듯이")
            st.write(st.session_state['a14_p2'], "에서 ", int(st.session_state['y14_2_p2']), "에 ", st.session_state['b14_p2'], "를 곱하면 ", st.session_state['x14_p2'], "이 된답니다.")
            st.write("자신이 입력한 값과 비교해보면서 어떤 부분을 놓쳤는지 확인하고 더 연습해봅시다.")


if st.session_state["Q14_p2"] == 3.1:  
    st.write("소수의 나눗셈에서 몫을 자연수 부분을 나누는 방법에도 어려움이 있는 것 같군요. 몫의 자연수 부분까지만 구하는 것은 자연수의 나눗셈으로 바꾸어서 계산해도 괜찮습니다.")
    st.session_state['a14__2'] = int(st.session_state["a14_p2"]*100)
    st.session_state['b14__2'] = int(st.session_state["b14_p2"]*100)
    st.write("나누는 수와 나누어지는 수에 같은 수를 곱해도 몫은 변하지 않는다는 점을 이용하면 자연수로 쉽게 바꿀 수 있답니다.")
    st.write("주의할 점은 나누어지는 수는 이미 자연수라도 나누는 수를 자연수로 만들기 위해 같은 수를 꼭 곱해줘야 한다는 것입니다.")
    st.write("지금 문제는 나누는 수와 나누어지는 수에 똑같이 100을 곱해주면 되겠네요.")
    st.write("그렇게 되면 ", st.session_state["a14_p2"], "이 ", st.session_state['a14__2'], "로 바뀌게 되고,")
    st.write(st.session_state["b14_p2"], "이 ", st.session_state['b14__2'], "로 바뀌게 됩니다.")
    st.write("그렇다면 자연수의 나눗셈으로 바꾼 후 몫을 자연수 부분까지 구한 후 답을 입력해봅시다.")
    Q14_easy_Text_2_p2 = f"연습 14-2. {st.session_state['a14__2']} \u00F7 {st.session_state['b14__2']}의 몫을 자연수 부분까지 구해보시오."
    st.markdown(Q14_easy_Text_2_p2)
    answer5_p2 = st.number_input("답 : ", key="5_p2", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="e_p2", on_click=make5_p2, disabled=st.session_state["B56_p2"]): 
        if answer5_p2 == None:
            answer5_p2 = 0
        if int(answer5_p2) == int(st.session_state['y14_2_p2']):
            st.write("정답입니다.")
            st.session_state["Q14_p2"] = st.session_state["Q14_p2"] + 0.4
        else:
            st.session_state["Q14_p2"] = st.session_state["Q14_p2"] + 0.9

if st.session_state["Q14_p2"] == 3.5:
    st.write("그럼 이제 몫의 자연수 부분을 이용하여 나머지를 구해봅시다. 나머지를 구할 때는 몫의 자연수 부분을 구하느라 자연수로 바꾸었던 숫자를 다시 소수로 돌려놓고 생각해야 합니다.")
    st.write("방금 입력한 몫의 자연수 부분인 ", int(st.session_state['y14_2_p2']), "를 나누는 수인 ", st.session_state['b14_p2'], "에 곱해서 나누어지는 수인 ", st.session_state['a14_p2'], "에서 빼주면 됩니다.")
    st.write(Q14_Text_p2)
    answer6_p2 = st.number_input("답 : ", key="6_p2", value=None, placeholder="답을 입력하세요.", format="%f")
    if st.button("채점하기", key="f_p2", on_click=make6_p2, disabled=st.session_state["B57_p2"]): 
        if answer6_p2 == None:
            answer6_p2 = 0
        if float(answer6_p2) == float(st.session_state["x14_p2"]):
            st.write("정답입니다. 나머지는 이렇게 자연수 부분까지 몫을 구한 후 나누는 수에 곱해서 나누어지는 수에서 빼는 식으로 구할 수 있습니다.")
            st.write("하지만 더 쉬운 방법으로는 자연수 부분까지 몫을 구하는 과정을 세로셈으로 똑같이 한 후, 나누어지는 수의 소수점을 그대로 내려서 구한 나머지에 소수점을 찍어도 됩니다.")
            st.write("이 사실을 기억하면서 더 연습해봅시다.")
            st.session_state["Q14_p2"] = st.session_state["Q14_p2"] - 0.5
        else:
            st.write("오답입니다. 나머지를 구하는 방식을 이해하지 못하거나 계산 실수가 있었군요.")
            st.write("7을 2로 나누고 남은 나머지를 구할 때 7에서 몫인 3에 2를 곱한 후 빼주듯이")
            st.write(st.session_state['a14_p2'], "에서 ", int(st.session_state['y14_2_p2']), "에 ", st.session_state['b14_p2'], "를 곱한 후 빼주면 ", st.session_state['x14_p2'], "이 된답니다.")
            st.write("자신이 입력한 값과 비교해보면서 어떤 부분을 놓쳤는지 확인하고 더 연습해봅시다.")

if st.session_state["Q14_p2"] == 4:
    st.write("오답입니다. 소수의 나눗셈과 나머지를 구하는 것에 모두 어려움이 있었군요.")
    st.write("그래도 나머지를 구하는 방법에 대해서는 다시 설명하겠습니다.")    
    st.write("위에서 풀지 못한 문제의 답을 이용해 나머지를 구하는 과정을 살펴봅시다.")
    st.write(f"{st.session_state['a14__2']} \u00F7 {st.session_state['b14__2']}의 몫을 자연수 부분까지 구하면 답은 {int(st.session_state['y14_2_p2'])}가 됩니다.")
    st.write("7을 2로 나누고 남은 나머지를 구할 때 7에서 몫인 3에 2를 곱한 후 빼주듯이")
    st.write(st.session_state['a14_p2'], "에서 ", int(st.session_state['y14_2_p2']), "에 ", st.session_state['b14_p2'], "를 곱한 후 빼주면 ", st.session_state['x14_p2'], "이 된답니다.")
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
