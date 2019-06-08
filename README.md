# Simulacao-Fisica-BackEnd

BackEnd da SandBox de Simulação



# Gerenciador de pacotes

	pip
	Para instalar o pip:
		vá ate: https://bootstrap.pypa.io/get-pip.py
		(isso é um aquivo python, salve-o em sua maquina)
		vá até o diretorio onde o salvou e execute a seguinte linha de comando:
		python get-pip.py


# Dependencias

	virtualenv
	instalando venv:
		pip install virtualenv
	_____________________
	flask
	instalando flask:
		pip install Flask
		pip install -U flask-cors

# Iniciando o projeto
	Primeiro instale as dependencias
	inicie o venv com o seguinte comando:
	$ virtualenv .venv
	$ source .venv/bin/activate    - (ou outro diretorio que tiver o arquivo activate, no meu caso foi no scripts)
	instale o flask
	sirva a aplicação com o flask com o seguinte comando:
	$ FLASK_APP=main.py flask run
	estará rodando em http://127.0.0.1:5000/
	
