# flask-rest-api 
Padrão de desenvolvimento restful API - Flask 


## Tecnologias utilizadas
* **[Python3](https://www.python.org/downloads/)** - Uma linguagem de programação que permite trabalhar mais rapidamente.
* **[Flask](flask.pocoo.org/)** - Um microframework para Python baseado em Werkzeug, Jinja 2.
* **[Virtualenv](https://virtualenv.pypa.io/en/stable/)** - Uma ferramenta para criar ambientes virtuais isolados.
* **[PostgreSQL](https://www.postgresql.org/download/)** – Banco de dados do Postgres oferece muitas [vantagens](https://www.postgresql.org/about/advantages/) aqui.
* Pequenas dependências podem ser encontradas no arquivo requirements.txt na pasta raiz.


## Instalação / Uso
* Se você deseja executar sua própria compilação, primeiro certifique-se de ter o python3 globalmente instalado em seu computador. Se não, você pode obter python3 [aqui] (https://www.python.org).
* Depois disso, certifique-se de ter instalado o virtualenv globalmente também. Caso contrário, execute isto:
    ```
        $ pip install virtualenv
    ```
* Clone esse repositorio para o seu PC
    ```
        $ git clone https://github.com/EduBrQ/Flask-Rest-Api---Demo.git
    ```


* #### Dependencias
    1. Cd em seu repositorio clonado, como tal:
        ```
        $ cd flask-rest-api
        ```

    2. Crie e ative o seu ambiente virtual em python3:
        ```
        $ virtualenv -p python3 venv
        $ pip install autoenv
        ```

* #### Variáveis de ​​Ambiente
    Crie um arquivo .env e adicione o que segue abaixo:
    ```
    source venv/bin/activate
    export SECRET="alguns-caracteres-muito-longos-e-aleatórios - MUDE AO SEU GOSTO"
    export APP_SETTINGS="development"
    export DATABASE_URL="postgresql://localhost/flask_api"
    ```

    Salve o arquivo. Dê um CD para fora do diretório e então o `Autoenv` irá configurar automaticamente as variáveis.
    Nós agora mantivemos informações confidenciais do mundo exterior! 😄

* #### Instale seus requisitos
    ```
    (venv)$ pip install -r requirements.txt
    ```

* #### Migrações
    No seu console do psql, crie seu database:
    ```
    > CREATE DATABASE flask_api;
    ```
    Então, aplique as suas migrações
    ```
    (venv)$ python manage.py db init

    (venv)$ python manage.py db migrate
    ```

    E finalmente, migre as suas migrações para persistirem no banco de dados
    ```
    (venv)$ python manage.py db upgrade
    ```

* #### Iniciando
    No prompt entre na pasta rest_api_demo e execute o comando:
    ```
    (venv)$ python server.py
    ```
    Agora você pode acessar o aplicativo em seu navegador local usando
    ```
    http://localhost:8000/home/
    ```
    Ou teste as rotas /diabetes e /pressao usando o Postman
	
* #### Testando
    No prompt entre na pasta rest_api_demo e depois na pasta Testes, escolha entre a pasta de testes de integração ou unitarios e execute o comando:
    ```
    (venv)$ python nomeTeste.py
    ```
