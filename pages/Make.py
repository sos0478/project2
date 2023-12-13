import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import gspread

st.subheader("소수의 나눗셈 문제 만들기")
make_q = st.text_input("문제를 입력해주세요.", "문제 입력")
make_a = st.text_input("만든 문제의 답을 입력해주세요.", "답 입력")

make_list = [make_q, make_a]

credentials = {
    "type": "service_account",
    "project_id": "project-408011",
    "private_key_id": "50384da5e2a15451378e8fb9d6cf203e5fcf1920",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDGVknrPae17tcq\nkjJQPD71rcNYkUC+BdZwSeRSGESm+nPwjcZWM7WN98PmAsOzvrvbGOixfuuZHkqL\nZcZdzjIA9ZeIR+GXPtxP4Mku/ssbOMqN6CA6MBR9u3qaRPh7OVYR3s7BR07bBC65\nJqFDvS8h2VIfLaMfdiDBkO4bM3X6n2GIiCHbGTR92x28uUsCviGTmYM95zheuQPo\nKMfeePDRej6FjxkD0h27WWtj4m6dPDUf02NXctHamVNYcpHvki2/aGnc+4BSqFke\nfnG57TeuTxhByicOb0sfI9pQeN7VBz7CQYaONRhf1isPUQka0S2u7/DeTNomi7xv\nI0IERitZAgMBAAECggEAE/GmG/i+kjO+0PXzx3/xZE7JcZDkod8QJ8k0Y4FzeNd/\nPFmjT7SCLZEUMr9FKuBTf1YHQx70RbjHLfKJYpIrEs/fYZm50HXGnWUpEdfW+Gkq\n7B9jCzrduqF1NAlas7hppGEjaQnYvvsSEDX3WiqOUGDsKjyydiXQqCpA2T0g4FdE\nNhhG6JGOelIxPmbznsmddPdFpzjSDsTaX+70wcFoTgOloPWciYzStdqS63ZjonP9\nBzajIdLZEjhvty/Zp8OI4Vg+0KbsCMeLTlxhIFaIMcX7MFESno57k/Y1AoXhlkn6\n+VZs9ZAPFGAuBdo+5kIuEKjtooEpsj2O/Kj41W/+8QKBgQD7e9uokTm1VmlBNfZG\npO2nKImOo7aOlFgGs90ZVISha+SJa+vGivYcgHtoSMp5TBswXpBWpyyxZY19NFMI\nUXewids5GnBAafYCsR/Bm3Gg61A6b8bLFcAvNR9VUMEPYexNzxwtg79DzFHhti1x\nTXIl2+UCIjpDfbHdzdqfvr0oMQKBgQDJ5hmgRYxEcDEeAKXpK3mySkltqUcmKYkd\nw/lhD+EWt/vgZkvMIapOSKk9KiTlI4nV5Npdl3xxQ5IZt/ku6t7Pqh0gzFflz/pS\nHndoues8ZN/l4keJVqnAtfK1sXFUaHQ2szMWeA8HU4NC019CptF+B36pq0jQiL6h\nOHbYplsTqQKBgQDsojAfnn9BrYye6srQ0HI6/v7otA2cfeOScv5RzmB6j85crKsP\niERqr07v4sZ6em1/BwwkLWv1hIwtSuXyhs3r1NvuEH2dbtco00gBYmX6OFGmmvTg\ntZfAE+lm2vS+p7K1yHNINJbtkb1eeJCr82a8TvxfFJvkU8rg3cmg1NaikQKBgQDC\nYpHlp1BHTCVeF42lk0AWEkPkGwjviyoCyH4/n0Q91WHiSVtM7FTGDlszEnJ3UuIQ\nV8iON52Oh1oQ/Poi2+st0UE+JL+z+auuiLq6z9XWTeDruhLZ/eBuND+8A11zwSWy\nzJGxXmJJ0XQdUNj0mRw11Q10Wf8/F4lCO9Tg/jnOEQKBgQCYNp3w2kyTnLZHB8cf\nDF14WYZgJEIjl0+hEmwsLBjPYR3iPBi0ejvpGJCPmoe05brUFHzFtxWskPlW7Yfk\n+SMQSM6QSlkC8qMIpsWgbD+nDBp+e6+mzo69/ufAa5yS0fQoH9z4It22vFUF4QAJ\nT9YMEy3P8ub/jctoW31aB1txTQ==\n-----END PRIVATE KEY-----\n",
    "client_email": "project@project-408011.iam.gserviceaccount.com",
    "client_id": "109610279499970516707",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/project%40project-408011.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

gc = gspread.service_account_from_dict(credentials)
doc = gc.open_by_key('1vdm5nZU4dgLxMxroKaOrmEvAmYhboeIuL2Lb8poksSk')
worksheet = doc.worksheet('data')

st.write('제출은 문제와 답을 입력한 후 한 번만 눌러주세요.')

if st.button('제출하기'):
    worksheet.append_row(make_list)
    st.write('제출이 완료되었습니다.')
    st.write('문제를 더 만들고 싶으면 문제와 답을 수정한 후 제출하기 버튼을 다시 눌러주세요.')

if st.button('분석 화면으로 돌아가기'):
    switch_page("Review")