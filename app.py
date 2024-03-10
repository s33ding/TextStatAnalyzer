import streamlit as st

#input de números
input_num = st.number_input(
       'Escreva um número entre 0 e 10',
       min_value = 0,
       max_value = 10,
       value = 0,
       step = 1
)

st.write('O número inputado foi: ', input_num)
#input de texto
input_txt = st.text_input(
      'Escreva uma palavra com até 5 letras',
      value = 'juiz',
      max_chars = 5
)
st.write('A palavra inputada foi: ', input_txt)