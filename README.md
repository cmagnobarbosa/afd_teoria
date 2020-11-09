## AFD_Teoria
AFD Teoria de Linguagens

Implementação de um autômato finito determinístico(AFD) na linguagem python.
Esta implementação possui uma interface Web desenvolvida com materialize css e
flask.

Desenvolvido por Carlos Magno, UFSJ 2020.

Licença: MIT

O termo `$`, significa que os presentes comandos devem ser executados no terminal.
Execute os comandos que aparecem após `$`.

Esta implementação é genérica suportando a modificação do arquivo com as
transições em `automatos/afd.txt`.

O processo de instalação também esta disponível no youtube:
 https://youtu.be/6yIw3a9JEPc
## AFD padrao carregado

O AFD padrão carregado foi gerado a partir
da seguinte expressão no regular, no qual
apresenta as palavras da linguagem.

```
C1(09+AL)*3
```
Um conjunto com palavras aceitas e negadas pode ser encontradas nos arquivos
`palavras_aceitas.txt`e `palavras_negadas.txt`

## Estrutura

A principal estrutura utilizada é um dicionario, como apresentado abaixo:

```
{'estado': {'termo_aceito': 'proximo_estado'}}
```

Exemplo:
```
{'q0': {'C': 'q1'}}
```
Lendo `C` no estado `q0` realize uma transição para o estado `q1`.

Cada estado do autômato somente conhece a informações necessário para realizar a transição para o próximo estado.

## Como instalar

Instale o graphviz, utilizado somente para o plot do autômato.

>$ sudo apt-get update

>$ sudo apt-get install graphviz

Recomendamos a instalação
desta aplicação em um ambiente virtual.
O ambiente virtual evita conflitos de dependências.

Crie um ambiente virtual, seguindo o padrao `python3 -m venv <env_name>`, veja o exemplo:

>$ python3 -m venv env_teoria

Agora ative o ambiente virtual:

>$ source env_teoria/bin/activate

Ativando o ambiente virtual, aparecerá no terminal `(env_teoria)$`.

Agora, Instale as dependências no ambiente:

> (env_teoria)$ pip install -r requeriments.txt

## Para Executar

Considerando que você instalou as dependências, siga os passos abaixo:


Ative o ambiente virtual(somente caso já não esteja ativado)

>source env_teoria/bin/activate

Agora execute:

>(env_teoria)$ python main_gui.py

Ocorrendo tudo normal o seu navegador padrão será aberto.
