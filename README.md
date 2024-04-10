## Projeto de Busca de Diretórios

Este é um projeto Python para um scanner de diretórios em aplicativos web. O scanner utiliza uma lista de palavras-chave (wordlist) para tentar identificar diretórios existentes em uma URL alvo. Funcionalidades

 

 - Gera combinações URL/diretório a partir de uma wordlist.   Envia
 -  solicitações HTTP GET para cada combinação URL/diretório.  
  - Identifica diretórios existentes com base nos códigos de status HTTP retornados.  
  - Permite interromper a execução com segurança ao pressionar Ctrl+C.

## Requisitos
 - Python 3.x instalado.   
 - Biblioteca requests instalada (pip install requests).

## Instalação

1.Clone o repositório para sua máquina local:

    git clone https://github.com/ItsMeYoshiro/DirSearch.git

2.Navegue até o diretório do projeto:
```
cd scanner-de-diretorios 
```
## Uso

1.Execute o script main.py:

```
python scanner.py
```
2.Siga as instruções para inserir a URL alvo e o caminho da wordlist.

3.Aguarde o término do scanner.

4.Os diretórios encontrados serão exibidos no final da execução.

## Exemplo

Suponha que você deseje verificar a presença de diretórios comuns em http://example.com. Você pode usar uma wordlist contendo os caminhos/diretórios a serem testados (por exemplo, wordlist.txt), e executar o script main.py para iniciar o scanner de diretórios.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias, correções ou novas funcionalidades.

## Licença

Este projeto é distribuído sob a Licença MIT.
