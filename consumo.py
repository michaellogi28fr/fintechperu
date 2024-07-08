import requests

url = "https://api.linkedin.com/v2/me"  # URL de la API que deseas consultar
access_token = "TU_TOKEN_DE_ACCESO"  # Reemplaza con tu token

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("Datos del perfil de LinkedIn:")
    print(f"Nombre: {data.get('localizedFirstName')} {data.get('localizedLastName')}")
    # Agrega más campos según tus necesidades
else:
    print(f"Error al consultar la API: {response.status_code}")
