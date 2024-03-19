import os
import requests
from bs4 import BeautifulSoup
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_logo():
    lazyboy_logo = """
                                          _.oo.
                 _.u[[/;:,.         .odMMMMMM'
              .o888UU[[[/;:-.  .o@P^    MMM^
             oN88888UU[[[/;::-.        dP^
            dNMMNN888UU[[[/;:--.   .o@P^
           ,MMMMMMN888UU[[/;::-. o@^
           NNMMMNN888UU[[[/~.o@P^
           888888888UU[[[/o@^-..
          oI8888UU[[[/o@P^:--..
       .@^  YUU[[[/o@^;::---..
     oMP     ^/o@P^;:::---..
  .dMMM    .o@^ ^;::---...
 dMMMMMMM@^`       `^^^^
YMMMUP^
 ^^
    """
    print(lazyboy_logo)
    print("\nLazyBoy OSSINT")

def search_on_social_media_by_username(query):
    social_media_sites = [
        "facebook.com", "instagram.com", "twitter.com", "whatsapp.com", "tiktok.com", "reddit.com",
        "linkedin.com", "pinterest.com", "vk.com", "perselisihan.com", "oke.ru", "zhihu.com",
        "messenger.com", "line.me", "telegram.org", "peachavocado.com", "snapchat.com", "namu.wiki",
        "tumblr.com", "ameblo.jp", "pintu berikutnya.com", "weibo.com", "xiaohongshu.com", "heylink.me",
        "kendur.com", "patreon.com", "kwai.com", "zalo.me", "thread.net", "komikcast.lol", "pinterest.es",
        "benciblog.com", "atid.me", "slideshare.net", "jurnal langsung.com", "discordapp.com", "pinterest.com.mx",
        "ssstik.io", "otakudesu.media", "bakusai.com", "pinterest.co.uk", "fb.com", "ptt.cc", "pinterest.fr",
        "snaptik.app", "zaloapp.com", "dcard.tw", "pinterest.de", "youtubekids.com", "ameba.jp", "xanga.com",
        "viadeo.com", "twitpic.com", "renren.com", "orkut.com", "odnoklassniki.ru", "newsvine.com",
        "netlog.com", "mixi.jp", "hi5.com", "getsatisfaction.com", "friendster.com", "friendfeed.com",
        "github.com", "breachforums.com"  # Menambahkan breach forum ke dalam daftar
    ]

    scanned_urls = set()

    for site in social_media_sites:
        url = f"https://{site}/{query}"
        if url not in scanned_urls:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    if soup.find_all("div"):
                        print(f"\033[94mResults from {site}:\033[0m")
                        for div in soup.find_all("div"):
                            print(div.text.strip())
                        print("\033[92mLink:\033[0m", url)  # Link hijau jika hasil ditemukan
                        print()
                    else:
                        print(f"\033[91mNo results found on {site}\033[0m")
                        print("\033[91mLink:\033[0m", url)  # Link merah jika tidak ada hasil
                else:
                    print(f"Failed to fetch data from {site}")
                scanned_urls.add(url)
            except Exception as e:
                print(f"Error: {e}")
            time.sleep(0.5)  # Delay 0.5 detik untuk setiap spam

def search_on_social_media_by_number(phone_number):
    social_media_by_number = [
        "whatsapp.com", "facebook.com", "instagram.com", "twitter.com", "telegram.org", "snapchat.com",
        "linkedin.com"  # Menambahkan situs media sosial yang menggunakan nomor telepon
    ]

    scanned_urls = set()

    print("\033[92mResults from social media using phone number:\033[0m")
    for site in social_media_by_number:
        url = f"https://{site}/{phone_number}"
        if url not in scanned_urls:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    print(f"\033[94mResults from {site}:\033[0m")
                    print("\033[92mLink:\033[0m", url)  # Link hijau jika hasil ditemukan
                    print()
                else:
                    print(f"\033[91mNo results found on {site}\033[0m")
                    print("\033[91mLink:\033[0m", url)  # Link merah jika tidak ada hasil
                scanned_urls.add(url)
            except Exception as e:
                print(f"Error: {e}")
            time.sleep(0.5)  # Delay