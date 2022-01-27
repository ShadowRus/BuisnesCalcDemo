import streamlit as st
import pandas as pd
import  numpy as np

# Dictionary and data.......
#--------STATUS-----------------------
dict_status = {'Дистрибьютер':'D', 'Премиум партнер':'PP','Партнер':'P'}
list_status= list(dict_status.keys())
list_status_short= list(dict_status.values())
#----------PRODUCT-DIRECT----------------

product_direct_list = list(['Retail', 'SIGMA', 'Девайс', 'Мобильные решения'])
#--------------------------------
list_Retail =list(['Фискальные регистраторы','АТОЛ Connect','Frontol 6 + Frontol xPOS','Frontol Release Pack 6/xPos 1 год'])
list_AMS= list(['Все','ТСД','ПО Mark.Scan'])
#---------READ-BUISNESS PLAN-------
df_pda = pd.read_csv('PDA22-27_.csv',sep=';',index_col = 'Year')

df_soft = pd.read_csv('Soft22-27_.csv',sep=';',index_col = 'Year')
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
#....VARIABLES.......................
lt_saas = 0.48
#------------Year=plan----------

dff= pd.read_csv('buisnes-roadmap.csv')

def col_dppp(status_partner):
    col_d = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    col_p = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    col_pp = [2, 3, 4, 5, 6, 12, 13, 14, 15, 16]

    if status_partner == list_status[0]:
        col_f=col_d
    elif status_partner == list_status[1]:
        col_f= col_pp
    elif status_partner == list_status[2]:
        col_f= col_p
    else:
        col_f= col_pp
    return col_f
#---------------------
st.title('Бизнес-калькулятор партнеров АТОЛ')

add_selectbox = st.sidebar.selectbox(
    "Бизнес-калькулятор",
    ("Бизнес-план", "Рассчитать свои выгоды","Ценность SaaS", "О Бизнес-калькуляторе")
)
if add_selectbox == 'Бизнес-план':
    status_partner = st.radio(
        "Выберите Ваш статус",
        list_status, help='Выберите свой статус партнера')

    product_direct = st.selectbox('Выберите продуктовое направление', product_direct_list, index=3)
    if product_direct == product_direct_list[3]:
        product_AMS = st.selectbox("Выберите товары:", list_AMS, index=0)
        text1 = 'План продаж на 2022-2027 год категории ' + product_direct + ' для партнера со статусом ' + status_partner
        st.subheader(text1)

        df_f = dff[dff['Продуктовое направление'] == product_direct].drop(dff.columns[col_dppp(status_partner)], axis=1)
        st.dataframe(df_f)
        if product_AMS == list_AMS[1]:
            temp1 = df_pda[[dict_status[status_partner]]]
            temp1.rename(columns={dict_status[status_partner]: product_AMS}, inplace=True)
            st.dataframe(temp1)
        if product_AMS == list_AMS[2]:
            temp1 = df_soft[[dict_status[status_partner]]]
            temp1.rename(columns={dict_status[status_partner]: product_AMS}, inplace=True)
            st.dataframe(temp1)
        if product_AMS == list_AMS[0]:
            temp1 = df_pda[[dict_status[status_partner]]]
            temp1.rename(columns={dict_status[status_partner]: product_AMS}, inplace=True)
            temp1 = pd.concat([temp1, df_soft[[dict_status[status_partner]]]], axis=1)
            temp1.columns = ['ТСД', 'ПО Mark.Scan']
            temp1['Mark.Scan LifeTime'] = temp1.iloc[:, 1] * lt_saas
            temp1['Mark.Scan LifeTime'] = temp1['Mark.Scan LifeTime'].apply(lambda x: f"{x:.0f}")
            temp1['Mark.Scan SAAS'] = temp1.iloc[:, 1] * (1 - lt_saas)
            temp1['Mark.Scan SAAS'] = temp1['Mark.Scan SAAS'].apply(lambda x: f"{x:.0f}")
            st.dataframe(temp1)
            del temp1
    else:
        st.write('Для выбранного направления бизнес-калькулятор временно недоступен.Зайдите в раздел чуточку позднее')
else:
    add_selecradio = st.sidebar.radio('Next',('second','third'))