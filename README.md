# TwitterClone API

Esta é uma API para um clone do Twitter.

## Uso do Docker

Para rodar a API, utilize o Docker:

```bash
docker-compose up --build
```

A API estará disponível em `http://localhost:8000/api/`.

## Variáveis de Ambiente

Antes de executar o projeto, você precisará configurar algumas variáveis de ambiente. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
```

Substitua `your_secret_key` e `your_database_url` pelos valores apropriados.

## Autenticação

A API requer autenticação para realizar requisições. Você deve obter um token de acesso ao fazer login e incluí-lo no cabeçalho de autorização das requisições:

```
Authorization: Bearer <access_token>
```
