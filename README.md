# DOCKER

## Instalando no Linux

```BASH
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
Executing docker install script, commit: 7cae5f8b0decc17d6571f9f52eb840fbc13b2737
<...>
```

Verifique se o Docker está corretamente instalado:  \
`sudo docker run hello-world`

Adicione seu usuário ao grupo do Docker para poder executar sem previlégios root
```BASH
sudo groupadd docker
sudo usermod -aG docker $USER
```

Verifique se o Docker está rodando sem sudo:
`docker run hello-world`

## Criando um container

Na pasta do seu projeto crie o arquivo _Dockerfile_:
> Nosso projetinho está dentro da pasta _./application_
```Docker
FROM python:latest
WORKDIR /api

COPY . .

RUN rm -rf venv
RUN python -m pip install -r req.txt

CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]

EXPOSE 8002
```

Cria a imagem e nomeia:tag (-t) da pasta local (.)  \
`docker build -t websocket-test:latest .`

Rodar o container:  \
`docker run -d -p 8002:8002 --name [apelido] websocket-test`
> __-d__ para rodar em background, remova a flag -d para poder visualizar o terminal  \
> __--name [apelido]__ para definir um nome amigável  \
> __-p 8002:8002__ para definir a porta da máquina e a porta do container

Para verificar os containeres rodando:  \
`docker ps`

Parar um container:  \
`docker stop [container ID]`

## Conectando containeres - Network

Para conectar containeres criamos uma rede virtual para eles.  \
`docker network create [nome-da-rede]`

`docker run -p 8002:8002 websocket-test --network [nome-da-rede]`

## Compartilhando dados entre containeres e/ou máquina local - Volume

No arquivo _Dockfile_ adicione `VOLUME /var/www/html`, após isso precisa apagar o container, a imagem e rebuildar.  \
`docker build -t websocket-test:latest .`

E subir um novo container já especificando onde o volume será montado dentro do container:  \
`docker run -p 8002:8002 websocket-test -v [volume-name] /var/www/html`

## Docker Compose
Crie o arquivo: __docker-compose.yml__:  \
```YML
services:
  application:
    # image: python:latest
    container_name: websocket-teste
    build: ./application
    ports:
      - 8002:8002
    volumes:
      - vol-teste:/data/db
    restart: always

  nginx:
    container_name: nginx-exemplo
    build: ./nginx
    restart: always
    volumes:
      - spa-teste:/var/www/html
    ports:
      - 80:80
    depends_on:
      - application
volumes:
  vol-teste:
  spa-teste:

```

docker compose up -d
docker compose down
