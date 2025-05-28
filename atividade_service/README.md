# 🚀 Flask + Docker

> Empacote e execute sua API Flask de forma simples e consistente usando Docker.

---

## 📋 Sumário

* [Pré-requisitos](#-pré-requisitos)
* [Dockerfile](#-dockerfile)
* [Configuração do Flask](#-configuração-do-flask)
* [Build da imagem](#-build-da-imagem)
* [Execução do container](#-execução-do-container)
* [Testando a aplicação](#-testando-a-aplicação)
* [Verificação & Logs](#-verificação--logs)

---

## 🛠️ Pré-requisitos

* Docker instalado (versão 20.x ou superior)
* Projeto Flask com arquivo `requirements.txt`

---

## 🐳 Dockerfile

Crie um arquivo `Dockerfile` na raiz do projeto:

```dockerfile
# 1. Imagem base Python leve
FROM python:3.12-slim

# 2. Define diretório de trabalho
WORKDIR /app

# 3. Instala dependências (usa pip cache-off para otimizar imagem)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copia código-fonte para dentro do container
COPY . ./

# 5. Expõe porta da aplicação
EXPOSE 5002

# 6. Comando padrão para iniciar a API
CMD ["python", "app.py"]
```

---

## ⚙️ Configuração do Flask

No seu script principal (`app.py` ou similar), garanta que o servidor escute em **todas** as interfaces:

```python
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',  # aceita conexões externas ao container
        port=5002,
        debug=True      # opcional em desenvolvimento
    )
```

---

## 🏗️ Build da imagem

Execute este comando no terminal, na pasta raiz do projeto:

```bash
docker build -t minha-api .
```

* `-t minha-api` define o nome da imagem.
* O ponto final (`.`) indica o contexto de build.

---

## ▶️ Execução do container

Suba o container em modo *detached* e mapeie a porta 5002:

```bash
docker run -d -p 5002:5002 minha-api
```

* `-d` → executa em segundo plano.
* `-p 5002:5002` → host\:container = 5002:5002.

---

## 🔍 Testando a aplicação

Após iniciar o container, acesse:

* Pelo navegador: `http://localhost:5002/alunos`
* Pelo `curl`:

  ```bash
  curl http://localhost:5002/alunos
  ```

Se tudo estiver correto, você verá a resposta JSON da sua API.

---

## ⚡ Verificação & Logs

* Para listar containers ativos:

  ```bash
  docker ps
  ```
* Para visualizar logs em tempo real:

  ```bash
  docker logs -f <container_id>
  ```

---

> Agora sua API Flask está pronta para rodar em qualquer ambiente! 🐍 + 🐳
