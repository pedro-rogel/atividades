README

Este documento descreve como empacotar e executar sua aplicação Flask dentro de um container Docker.

Pré-requisitos

Docker instalado na sua máquina.

Estrutura do Dockerfile

--

Construir e executar o container

Build da imagem:

docker build -t minha-api .

Executar o container mapeando a porta do host:

docker run -d -p 5002:5002 minha-api

-d: executa em segundo plano (detached).

-p 5002:5002: mapeia a porta 5002 do host → 5002 do container.

Testando a aplicação

Após subir o container, acesse no navegador ou use curl:

curl http://localhost:5002/alunos

Se tudo estiver configurado corretamente, você receberá a resposta JSON da sua API.

Verificação e logs

Para listar containers ativos:

docker ps

Para ver logs do container:

docker logs <container_id>