import streamlit as st
import pandas as pd

# Dictionary and data.......
dict_status = {'Дистрибьютер', 'Премиум партнер', 'Партнер'}
product_direct_dict = {'Retail', 'SIGMA', 'Девайс', 'Мобильные решения'}
dict_Retail ={'Фискальные регистраторы','АТОЛ Connect','Frontol 6 + Frontol xPOS','Frontol Release Pack 6/xPos 1 год'}
dict_AMS ={'ТСД','ПО Mark.Scan'}
df = pd.read_csv('buisnes-roadmap.csv')
#...PageSettings..................
st.set_page_config(
     page_title="Ex-stream-ly Cool App",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="auto",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )
#...........................



st.title('Бизнес-калькулятор партнеров АТОЛ"')

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

status_partner = st.radio(
     "Выберите Ваш статус",
    dict_status, help='Выберите свой статус партнера')

product_direct = st.selectbox('Выберите продуктовое направление',product_direct_dict)
if product_direct == 'Мобильные решения':
     product_AMS = st.multiselect(
         'Выберите товары:',
         dict_AMS,
         dict_AMS)

     st.write('You selected:', product_AMS)
     st.write('You selected:', product_AMS[0])
else:
    st.write('Для выбранного направления бизнес-калькулятор временно недоступен.Зайдите в раздел чуточку позднее')


st.header('Ваш план продаж на 2022 год')