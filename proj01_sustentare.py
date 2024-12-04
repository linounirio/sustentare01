from time import sleep
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='sustentare', layout='wide')

usuarios = ['Sergio', 'Salatiel', 'Ingrid', 'Lino']
senhas = ['sergio123','salatiel123','ingrid123', '123']
def login():
    with st.container(border=True):
        cols = st.columns(3)
        cols[1].image('sustentare.png',output_format='PNG')
        st.divider()
        nome_usuario = st.selectbox(label='Selecione o usuário', options=usuarios)
        senha = st.text_input('insira sua senha: ', type='password')
        if st.button('Logar'):
            if (nome_usuario=='Sergio' and senha=='sergio123') or (nome_usuario=='Salatiel' and senha=='salatiel123') or (nome_usuario=='Ingrid' and senha=='ingrid123') or (nome_usuario=='Lino' and senha=='123'):
                st.session_state['logado']=True
                st.success('Login realizado com sucesso')
                sleep(0.5)
                st.rerun()
            else:
                st.error('Senha incorreta')

def coleta():
    df = pd.DataFrame(pd.read_csv('coleta1_limpo.csv'))
    cols = st.columns(3)
    cols[1].image('sustentare.png',output_format='PNG')
    st.divider()
    tab_geral,tab_outros = st.tabs(['Informações Gerais','Interações e análises'])
    with tab_geral:
        with st.container(border=True):
            cols = st.columns(3)
            raca = pd.DataFrame(df['3 Raça/ Cor'].value_counts(normalize=True)*100)
            cols[0].markdown(f'''
                             Como pode ser observado no gráfico de setores, que é possível perceber o desbalanço na distribuição por Raça/Cor da população 
                             atendida,com {raca.index[0]}: {round(raca['proportion'][0],2)}% e {raca.index[1]}: {round(raca['proportion'][1],2)}%, se 
                             as duas categorias estivessem balanceadas seria aproximadamente 40% da distribuição da população, mas como pode ser observado, somando
                             as duas categorias acima, se tem {round(raca["proportion"][:2].sum(),2)}% da população atendida. Isso influenciará em todas as análises 
                             e resultados.   
                             ''')
            fig = px.pie(raca,values='proportion', names=raca.index, title='Distribuição da População por Raça/Cor')
            cols[1].plotly_chart(fig)
            cols[2].table(raca)
        #categoria_idade = cols[1].selectbox(label='Selecione a idade', options=raca.index )

def main():
    if not 'logado' in st.session_state:
        st.session_state['logado']= False
    if not st.session_state['logado']:
        login()
    else:
        coleta()
  
        
    
if __name__=='__main__':
    main()