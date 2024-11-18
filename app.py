import requests
from bs4 import BeautifulSoup

# URL situs web yang ingin diambil
url = "https://www.bca.co.id/mybca"

# Mengirim request ke situs web
response = requests.get(url)

# Mengecek apakah request berhasil
if response.status_code == 200:
    # Parsing konten HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Menampilkan semua teks di halaman
    print(soup.get_text())
    
    # Menemukan dan menampilkan semua tautan di halaman
    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))
else:
    print("Gagal mengakses situs")
