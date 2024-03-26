import pandas as pd
from geopy.geocoders import GoogleV3

# Função para geocodificar um endereço e retornar a latitude e longitude
def geocode_address(address):
    geolocator = GoogleV3(api_key='AIzaSyAr_9XaY9GYG-r6ZC9Vozd8D4Z3CGkwXxM')
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

# Função para ler a planilha do Excel, geocodificar os endereços e salvar as coordenadas na planilha
def geocode_excel(input_file, output_file):
    # Carregar a planilha do Excel
    df = pd.read_excel(input_file)
    
    # Verificar se a coluna 'Endereço' existe
    if 'Endereço' in df.columns:
        # Criar duas novas colunas para as coordenadas
        df['Latitude'] = None
        df['Longitude'] = None
        
        # Iterar sobre as linhas da planilha e geocodificar os endereços
        for index, row in df.iterrows():
            address = row['Endereço']
            lat, lng = geocode_address(address)
            df.at[index, 'Latitude'] = lat
            df.at[index, 'Longitude'] = lng
        
        # Salvar a planilha com as coordenadas geográficas
        df.to_excel(output_file, index=False)
        print("Coordenadas geográficas adicionadas à planilha com sucesso!")
    else:
        print("A coluna 'Endereço' não foi encontrada na planilha.")

# Exemplo de uso
geocode_excel('Endereco_publico.xlsx', 'planilha_com_publicos.xlsx')
