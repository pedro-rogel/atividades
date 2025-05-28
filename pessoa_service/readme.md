README

Primeieo, é importante lembrar que a aplicação pega a nossa api school system (*https://school-system-hfwh.onrender.com/doc/*) como base para as entidades
Então, crie um professor, uma turma e um aluno para dar continuidade

Este documento descreve como empacotar e executar sua aplicação Flask dentro de um container Docker.

Pré-requisitos

Docker instalado na sua máquina.

Estrutura do Dockerfile

--

Construir e executar o container

Build da imagem:

docker build -t minha-api .

Executar o container mapeando a porta do host:

docker run -d -p 5001:5001 minha-api

-d: executa em segundo plano (detached).

-p 5001:5001: mapeia a porta 5001 do host → 5001 do container.

Testando a aplicação

Após subir o container, acesse no navegador ou use curl:

curl http://localhost:5001/alunos

Se tudo estiver configurado corretamente, você receberá a resposta JSON da sua API.

Verificação e logs

Para listar containers ativos:

docker ps

Para ver logs do container:

docker logs <container_id>

--

