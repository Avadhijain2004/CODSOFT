import streamlit as st
import random

st.title('Password Generator')

char_set_1 = '~```!@#$%^&*()_-+={[}]|\:;"\'<,>.?/'
char_set_1_mobile_friendly = '`!@$&*()-:;",.?/'
char_set_2 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

col1, col2 = st.columns(2)

with col1:
    is_mobile = st.checkbox('Mobile Friendly', value=True)
    length = st.number_input('Enter the length of password: ',value=1)

with col2:
    chosen_set = char_set_1_mobile_friendly if is_mobile else char_set_1
    char_set_1 = st.text_input('Specials', value = chosen_set)
    char_set_2 = st.text_input('Numbers and Letters', value=char_set_2)

st.header('Generated Password')
password_space = char_set_1 + char_set_2

def generate_password(space, length):
    for _ in range(length):
        yield random.SystemRandom().choice(space)

st.info(''.join(generate_password(password_space, length)))