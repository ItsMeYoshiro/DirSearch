import requests
from urllib.parse import urlparse
dir_found = []
dir_protected = []

def enum(url):
    if not urlparse(url).scheme:
        return "http://" + url
    return url

def dirfounds (dir_found, dir_protected):
    if dir_found or dir_protected:
        print("\nDiretórios encontrados no Scan: ")
        for dir in dir_found:
            print(dir)
        for dirproc in dir_protected:
            print(dirproc)
    else:
        print("\nNenhum diretório encontrado no Scan.")
    return

def brute (base_url, wordlist):
    base_url = enum(base_url)
    if not base_url.endswith("/"):
        base_url += "/"
    
    for word in wordlist:
        url = base_url + word.strip()
        try:
            response = requests.get(url, timeout=1)
            
            if response.status_code == 200:
                print(f"[!!!] Diretório encontrado: {url}")
                dir_found.append(url)
            elif response.status_code == 403:
                print(f"[!!!] Diretório encontrado mas protegido: {url} - Status: {response.status_code}")
                dir_protected.append(url)
            else:
                print(f"[-] Diretório não encontrado: {url} - Status: {response.status_code}")
        except requests.exceptions.Timeout:
            print(f"[-] Timeout: {url}")
        except requests.ConnectionError:
            print(f"[-] Erro de conexão: {url}")
        except KeyboardInterrupt:
            
            print("\n[?] Saída forçada pelo usuário.")
            print("[?] Saindo...")
            break
    return dir_found, dir_protected
  
def main ():          
    base_url = input("Digite a URL alvo (ex: http://example.com): ")
    caminho_wordlist = input("Digite o caminho da wordlist (ex: wordlist.txt): ")
    try:
        with open(caminho_wordlist, 'r') as arquivo:
            wordlist = [linha.strip() for linha in arquivo if linha.strip()]
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_wordlist}' não foi encontrado.")
        exit()
    brute(base_url, wordlist)
    dirfounds(dir_found, dir_protected)
    print("\nMade by")
    print("Twitter:@Yoshirohh")
    print("GitHub:ItsMeYoshiro\n")
    
if __name__ == "__main__":
    main()