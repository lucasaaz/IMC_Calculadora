import streamlit as st

with st.sidebar:
    st.title('Calculadora IMC')

    st.header('IMC: Definição?')

    st.write('Índice de Massa Corporal (IMC)')

    st.write('É um índice que relaciona peso e altura de uma pessoa')

    st.write('É utilizado como uma medida de saúde geral e para determinar se uma pessoa está em um peso saudável para sua altura')


st.title('Calculadora')

peso = st.number_input(label='Digite o seu Peso em kg', min_value=0.0)
altura = st.number_input(label='Digite o seu Altura em metros', min_value=0.0)

if st.button('calcular'):
    imc = peso / (altura ** 2)
    imc_ideal = 21.7
    imc_delta = imc - imc_ideal

    if imc < 18.5:
        resultado = {
            'classe': 'Abaixo do peso normal',
            'delta': imc_delta
        }
    elif 18.5 <= imc < 25:
        resultado = {
            'classe': 'Peso normal',
            'delta': imc_delta
        }
    elif 25 <= imc < 30:
        resultado = {
            'classe': 'Excesso de peso',
            'delta': imc_delta
        }
    elif 30 <= imc < 35:
        resultado = {
            'classe': 'Obesidade classe I',
            'delta': imc_delta
        }
    elif 35 <= imc < 40:
        resultado = {
            'classe': 'Obesidade classe II',
            'delta': imc_delta
        }
    elif imc > 40:
        resultado = {
            'classe': 'Obesidade classe III',
            'delta': imc_delta
        }

    st.code(f'O resultado é {resultado}')

    col1, col2 = st.columns(2)

    col1.metric('IMC Classificado', resultado['classe'], resultado['delta'], delta_color='inverse')
    col2.metric('IMC Calculado', round(imc, 2), resultado['delta'], delta_color='inverse')

    st.divider()
    st.text('Fonte')
    st.image('./tabela_IMC.png')



