## Desafio backend python 
Esta seção é válida para testes de backend e frontend.
Redux para armazenar dados (quando necessário)
Ganchos em vez de classes
AVISO!
Todos os dados postados ficarão visíveis para outros candidatos.
Observação: devido ao modo como o Django funciona, uma barra final “/” é necessária. A não inclusão disso pode causar problemas relacionados ao CORS.
O URL de back-end base é
https://dev.codeleap.co.uk/careers/
A estrutura de dados do item é a seguinte:
```json
{
    "id": "number",
    "username": "string",
    "created_datetime": "datetime",
    "title": "string",
    "content": "string"
}
```
Para criar uma postagem, envie uma solicitação POST http com a estrutura de dados abaixo. Lembre-se de que ainda não temos um ID:
Postar para
https://dev.codeleap.co.uk/careers/
A estrutura de dados do item é a seguinte:
````json
{
    "username": "string",
    "title": "string",
    "content": "string"
}
````
Para obter a lista de postagens, acesse o servidor com a seguinte solicitação GET. Este é um exemplo do que retornará do servidor:
Chegar ao
https://dev.codeleap.co.uk/careers/
A estrutura de dados do item é a seguinte:
````json
{
    "id":"number",
    "username": "string",
    "created_datetime": "datahora",
    "title": "string",
    "content": "string"
}
````
Para atualizar um item, acesse o servidor com a solicitação PATCH abaixo. Observe que desta vez também devemos enviar o ID na URL. Você não pode alterar as propriedades “id”, “nome de usuário” ou “data_criada”.
PATCH para
https://dev.codeleap.co.uk/careers/{OBJECT_ID}/
A estrutura de dados do item é a seguinte:
````json
{
    "title": "string",
    "content": "string"
}
````
Por último, mas não menos importante, para excluir um item, basta acessar o servidor com uma solicitação DELETE com o ID na URL. Observe que nada retornará do servidor.
EXCLUIR para
https://dev.codeleap.co.uk/careers/{OBJECT_ID}/
A estrutura de dados do item é a seguinte:
````json
{}
````



<h2 id="started">🚀 Getting started</h2>

Here you describe how to run your project locally

<h3>Prerequisites</h3>

Here you list all prerequisites necessary for running your project. For example:

- [Python](https://github.com/)
- [Docker](https://github.com) Optional
- [PDM]()

<h3>Cloning</h3>

How to clone my project branch docker

```bash
git clone https://github.com/PedroGuilhermeSilv/desafio-codeleap
```

<h3>Config .env variables</h2>

Use the `.env-example` as reference to create your configuration file `.env`.
If you use ENV as dev it will run with db.sqlite and if you use ENV as prod it will run in postgres


```yaml
POSTGRES_USER=admin
POSTGRES_PASSWORD=adminpass
POSTGRES_DB=main
PGADMIN_DEFAULT_EMAIL="admin@gmail.com"
PGADMIN_DEFAULT_PASSWORD=admin
ENV=prod
```

<h3>Starting</h3>

How to start project

```bash
cd desafio-codeleap
docker compose up
```