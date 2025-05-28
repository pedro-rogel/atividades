# 🚀 Flask + Docker

> Esta aplicação utiliza a API School System como base para as entidades.
>
> **Base API**: [https://school-system-hfwh.onrender.com/doc/](https://school-system-hfwh.onrender.com/doc/)
>
> Antes de iniciar, certifique-se de criar **pelo menos** um professor, uma turma e um aluno na API base.

---

## 📋 Sumário

1. [Pré-requisitos](#-pré-requisitos)
2. [Dockerfile](#-dockerfile)
3. [Configuração do Flask](#-configuração-do-flask)
4. [Build da imagem](#-build-da-imagem)
5. [Execução do container](#-execução-do-container)
6. [Testando a aplicação](#-testando-a-aplicação)
7. [Verificação & Logs](#-verificação--logs)

---

## 🛠️ Pré-requisitos

* Docker instalado (versão 20.x ou superior)
* Arquivo `requirements.txt` com as dependências do Flask

---

## 🐳 Dockerfile

Crie um arquivo `Dockerfile` na raiz do projeto:

```dockerfile
# 1. Imagem base Python leve
FROM python:3.12-slim

# 2. Define diretório de trabalho
WORKDIR /app

# 3. Instala dependências sem cache
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copia código-fonte
COPY . ./

# 5. Expõe porta da aplicação
EXPOSE 5001

# 6. Comando padrão para iniciar a API
CMD ["python", "app.py"]
```

---

## ⚙️ Configuração do Flask

No script principal (`app.py`), garanta que o Flask escute externamente:

```python
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',  # aceita conexões externas
        port=5001,
        debug=True      # modo de desenvolvimento
    )
```

---

## 🏗️ Build da imagem

No terminal, dentro da pasta do projeto:

```bash
docker build -t minha-api .
```

* `-t minha-api` define o nome da imagem
* `.` indica o contexto de build (diretório atual)

---

## ▶️ Execução do container

Inicie em segundo plano e mapeie a porta 5001:

```bash
docker run -d -p 5001:5001 minha-api
```

* `-d`: detached (segundo plano)
* `-p 5001:5001`: host\:container = 5001:5001

---

## 🔍 Testando a aplicação

1. Pelo navegador: `http://localhost:5001/alunos`
2. Via `curl`:

   ```bash
   curl http://localhost:5001/alunos
   ```

> Certifique-se de ter criado professor, turma e aluno na API base antes de testar.

---

## ⚡ Verificação & Logs

* Listar containers ativos:

  ```bash
  ```

docker ps

````
- Ver logs em tempo real:
```bash
docker logs -f <container_id>
````

---

> Pronto! Sua API Flask está empacotada e rodando em Docker. Boa codificação! 🐍 + 🐳
