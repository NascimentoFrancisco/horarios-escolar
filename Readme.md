# Projeto Horários

Este é um guia de como desenvolver com este projeto.

## Primeiros Passos

1. Clone do  repositório
2. Entre na pasta do projeto
3. Crie um virtualenv com Python3
  ```
  $ python3 -m venv venv
  ```
4. Ative o virtualenv

  ```
  $ . venv/bin/activate
  ```
5. Instale as dependências

  ```
  $ pip install -r requirements.txt
  ```

6. Copie o ENV_SAMPLE para um novo arquivo chamado .env que será usado para
armazenar a informações sensivéis da aplicação como senhas, chaves, ids e etc.

7. Execute as migrations
  ```
  $ ./manage.py makemigrations
  $ ./manage.py migrate
  ```
8. Execute a aplicação

  ```
  $ ./manage.py runserver
  ```

# Especificações


### O que posso fazer com este projeto:
  - Professores:
    - Fazer cadastros.
      - Nome, email, senhas, endereço
    - Podem atualizar a senhas
    - Recuperar a senhas
    - Cadastrar disponibilidade
  - Coordenador (Admin ou com permissões):
    - Cadastrar Professores
    - Cadastrar Disciplinas
    - Casdastrar Turmas
    - Organizar Horaios