import os
import requests
from bs4 import BeautifulSoup

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

def search_on_social_media(query):
    social_media_sites = {
        "USA": ["Twitter", "Facebook", "Instagram", "LinkedIn", "YouTube", "Pinterest", "Reddit", "Tumblr",
                "Snapchat", "WhatsApp", "TikTok", "Twitch", "Flickr", "Quora"],
        "India": ["Twitter", "Facebook", "Instagram", "LinkedIn", "Snapchat", "WhatsApp", "TikTok", "Pinterest"],
        "Indonesia": ["Twitter", "Facebook", "Instagram", "LinkedIn", "Line", "WhatsApp", "TikTok", "Pinterest"],
        # Anda dapat menambahkan negara dan situs media sosial lain di sini
    }

    for country, sites in social_media_sites.items():
        print(f"\033[92mResults from {country}:\033[0m")
        for site in sites:
            url = f"https://{site.lower()}.com/@{query}"  # Tambahkan "@" di depan username
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
            except Exception as e:
                print(f"Error: {e}")

def main_menu():
    clear_screen()
    print_logo()
    print("\n=== Main Menu ===")
    print("1. Search by Username")
    print("2. Search by Email")
    print("3. Search on Social Media")
    print("4. Exit")

def ossint_tool():
    while True:
        main_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            username = input("Enter username: ")
            search_on_social_media(username)
            input("\nPress Enter to continue...")
        elif choice == '2':
            email = input("Enter email address: ")
            search_on_social_media(email)
            input("\nPress Enter to continue...")
        elif choice == '3':
            query = input("Enter search query: ")
            search_on_social_media(query)
            input("\nPress Enter to continue...")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            input("Invalid choice. Press Enter to continue...")

if __name__ == "__main__":
    ossint_tool()