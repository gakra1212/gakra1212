import requests
from bs4 import BeautifulSoup

# Kullanıcı adı
username = "kullaniciAdiniz"  # Burada kendi kullanıcı adınızı girin

# Sosyal medya platformları için URL'leri oluşturma
social_media_urls = {
    "Instagram": f"https://www.instagram.com/{username}",
    "Twitter": f"https://twitter.com/{username}",
    "Facebook": f"https://www.facebook.com/{username}",
    "LinkedIn": f"https://www.linkedin.com/in/{username}",
    "TikTok": f"https://www.tiktok.com/@{username}",
    "Reddit": f"https://www.reddit.com/user/{username}",
    "Snapchat": f"https://www.snapchat.com/add/{username}"
}

# Sayfa kontrol fonksiyonu
def check_account(url):
    try:
        # URL'yi istekte bulunuyoruz
        response = requests.get(url)
        # Eğer HTTP yanıtı 200 ise sayfa var demektir
        if response.status_code == 200:
            return "Bulundu"
        elif response.status_code == 404:
            return "Bulunamadı"
        else:
            return "Erişim Sorunu"
    except Exception as e:
        return f"Hata: {str(e)}"

# Her bir sosyal medya platformu için kullanıcıyı kontrol etme
for platform, url in social_media_urls.items():
    result = check_account(url)
    print(f"{platform} - {result}")
    
