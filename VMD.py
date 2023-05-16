import streamlit as st
import requests,os,json,pandas,logging,time
from datetime import datetime

st.title('Media Delivery')
house_id = st.text_input('Insira o ID')

##Gera Token Azure##
url = "https://login.microsoftonline.com/a7cdc447-3b29-4b41-b73e-8a2cb54b06c6/oauth2/token"
payload = 'grant_type=client_credentials&resource=aa6d59c7-d681-40c3-874a-63bbac02b756&client_secret=2eC8Q~7jieXxHEbMLEaIjqky5IMzDJWHBj4ChaUb&client_id=9cec1867-1eae-40d5-a528-b9356516c36f'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie'      : 'fpc=AhsUmuM909FFi6MzdM61r4S2KOJeAQAAAHegdNsOAAAA; stsservicecookie=estsfd; x-ms-gateway-slice=estsfd'
}
response   = requests.request("POST", url, headers=headers, data=payload)
token_json = response.json()
token      = token_json['access_token']

##Busca Oferta##
url = f"https://apis.g.globo/ibms-api/v1/medias/{house_id}/offers?status.code=VODOFR__DISP"
        
payload = {}
headers = {
        'x-api-key'    : 'TMl5DfwHW03vKoUVeejzTBGAUWsb7VIKyNNVLcAriqLGEFzV',
        'Authorization': f'Bearer {token}',
        'Cookie'       : '2d0e861c58af3b9b30cc7646f388d953=cbe1cb81da8f1191acca90b14adf3417; 7fef0b4aa6565e88842b8e33e4074685=4d6d68c7f50f54883a53e7e70b3dc792'
        }
response2 = requests.request("GET", url, headers=headers, data=payload)
st.write(response2)
status2 = response2.status_code

if status2 == 200:
    ofertas_json = response2.json()
    lista_ofertas = (ofertas_json[0])
    id_oferta = str(lista_ofertas['id'])

    def form_callback():
        st.write(st.session_state.my_checkbox)
        if "SKY" in st.session_state.my_checkbox:
            url     = f"https://apis.g.globo/ibms-api/v1/offers/{id_oferta}/metadata-to-export/SKY"
            headers = {
                'x-api-key'    : 'TMl5DfwHW03vKoUVeejzTBGAUWsb7VIKyNNVLcAriqLGEFzV',
                'Authorization': f'Bearer {token}',
                'Content-Type' : 'application/json',
                'Cookie'       : 'b704e3bd59d9dd2e560b963402dc47d7=644c718ab9f3c449d61e74a975b4e675'
                }
            response3 = requests.request("POST", url, headers=headers, data=payload)
            status3 = response3.status_code
            print (status3)
            if status3 == 200:
                adi = (response3.text)
                parent_dir  = "\\\\10.3.44.125\\edit7\\AVALIACAO\\EDITORES\\HENRY\\TESTE_SKY_COURIER\\PACOTES"
            path = os.path.join(parent_dir, house_id)
            if os.path.exists(path):
                with open(path+"\\ADI.xml", "w") as f:
                    f.write(adi)
            else:
                os.makedirs(path)
                with open(path+"\\ADI.xml", "w") as f:                
                    f.write(adi)

            st.write(adi)

        if "VIVO" in st.session_state.my_checkbox:
            url     = f"https://apis.g.globo/ibms-api/v1/offers/{id_oferta}/metadata-to-export/VIVO"
            headers = {
                'x-api-key'    : 'TMl5DfwHW03vKoUVeejzTBGAUWsb7VIKyNNVLcAriqLGEFzV',
                'Authorization': f'Bearer {token}',
                'Content-Type' : 'application/json',
                'Cookie'       : 'b704e3bd59d9dd2e560b963402dc47d7=644c718ab9f3c449d61e74a975b4e675'
                }
            response3 = requests.request("POST", url, headers=headers, data=payload)
            status3 = response3.status_code
            print (status3)
            if status3 == 200:
                adi = (response3.text)
                parent_dir = "\\\\10.3.44.125\\edit7\\AVALIACAO\\EDITORES\\HENRY\\TESTE_VIVO_COURIER\\PACOTES"
            path = os.path.join(parent_dir, house_id)
            if os.path.exists(path):
                with open(path+"\\ADI.xml", "w") as f:
                    f.write(adi)
            else:
                os.makedirs(path)
                with open(path+"\\ADI.xml", "w") as f:                
                    f.write(adi)

            st.write(adi)

        if "CLARO" in st.session_state.my_checkbox:
            url = f"https://apis.g.globo/ibms-api/v1/offers/{id_oferta}/metadata-to-export/NET"
            headers = {
                'x-api-key'    : 'TMl5DfwHW03vKoUVeejzTBGAUWsb7VIKyNNVLcAriqLGEFzV',
                'Authorization': f'Bearer {token}',
                'Content-Type' : 'application/json',
                'Cookie'       : 'b704e3bd59d9dd2e560b963402dc47d7=644c718ab9f3c449d61e74a975b4e675'
                }
            response3 = requests.request("POST", url, headers=headers, data=payload)
            status3 = response3.status_code
            print (status3)
            if status3 == 200:
                adi = (response3.text)
                # parent_dir = ("\\\\10.3.44.125\\edit7\\AVALIACAO\\EDITORES\\HENRY\\TESTE_CLARO_COURIER\\PACOTES")
            path = ("\\\\10.3.44.125\\edit7\\AVALIACAO\\EDITORES\\HENRY\\TESTE_CLARO_COURIER\\PACOTES"+ house_id)
            if not os.path.exists(path):
                os.makedirs(path)
                with open(path+"\\ADI.xml", "w") as f:
                    f.write(adi)
            else:
                # os.makedirs(path)
                with open(path+"\\ADI.xml", "w") as f:                
                    f.write(adi)

            st.write(adi)

        if "OI" in st.session_state.my_checkbox:
            url = f"https://apis.g.globo/ibms-api/v1/offers/{id_oferta}/metadata-to-export/OI"
            headers = {
                'x-api-key'    : 'TMl5DfwHW03vKoUVeejzTBGAUWsb7VIKyNNVLcAriqLGEFzV',
                'Authorization': f'Bearer {token}',
                'Content-Type' : 'application/json',
                'Cookie'       : 'b704e3bd59d9dd2e560b963402dc47d7=644c718ab9f3c449d61e74a975b4e675'
                }
            response3 = requests.request("POST", url, headers=headers, data=payload)
            status3 = response3.status_code
            print (status3)
            if status3 == 200:
                adi = (response3.text)
                parent_dir = "\\\\10.3.44.125\\edit7\\AVALIACAO\\EDITORES\\HENRY\\TESTE_OI_COURIER\\PACOTES"
            path = os.path.join(parent_dir, house_id)
            if os.path.exists(path):
                with open(path+"\\ADI.xml", "w") as f:
                    f.write(adi)
            else:
                os.makedirs(path)
                with open(path+"\\ADI.xml", "w") as f:                
                    f.write(adi)

            st.write(adi)

    with st.form(key='my_form'):
        options = st.multiselect(
            'Escolha as operadoras',
            ['CLARO', 'OI', 'VIVO', 'SKY'],key='my_checkbox')
        submit_button = st.form_submit_button(label='Submit', on_click=form_callback)