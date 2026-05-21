import streamlit as st
st.title('vtn motors - imported cars🏎️')
st.sidebar.title('Escolha seu modelo🤷‍♂️')
st.sidebar.image('logo.png')

carros = ['Nissan Skyline GT‑R R34','Toyota Supra MK4','Dodge Charger 1970','Mazda RX‑7 FD','Mitsubishi Lancer Evolution VII','Nissan 350Z','Mitsubishi Eclipse','Nissan Silvia S15','Honda S2000','Honda Civic EJ1']
opcao= st.sidebar.selectbox('escolha o melhor carro para você',  carros)

st.image(f'{opcao}.png')
st.markdown(f'## Você alugou o modelo: {opcao}')
st.markdown('---')

dias = st.text_input(f'Por quantos dias o {opcao} foi alugado?')
km = st.text_input(f'Quantos  km você rodou com o {opcao}?')

if opcao == 'Nissan Skyline GT‑R R34':
    diaria = 12000

elif opcao == 'Toyota Supra MK4':
    diaria = 1000

elif opcao == 'Dodge Charger 1970' :
    diaria = 500

elif opcao == 'Mazda RX‑7 FD':
    diaria = 1500

elif opcao == 'Mitsubishi Lancer Evolution VII':
    diaria = 900

elif opcao == 'Mitsubishi Eclipse':
    diaria = 2000

elif opcao == 'Nissan 350Z':
    diaria = 2500

elif opcao == 'Nissan Silvia S15':
    diaria = 2500

elif opcao == 'Honda S2000':
    diaria = 2500

elif opcao == 'Honda Civic EJ1':
    diaria = 2500

else:
    diaria = 0

if st.button('calcular'):
     dias = int(dias)
     km = float(km)


     total_dias = dias * diaria
     taxa_km = km * 0.5
     aluguel_total = total_dias + taxa_km

     st.write(f'Você alugou o {opcao} por {dias} dias e rodou {km}km. O valor total a pagar é R${aluguel_total:.2f}')