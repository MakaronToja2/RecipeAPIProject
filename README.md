<h1>"RecipeAPI"</h1></br>
An advanced API that allows users to upload and retrieve recipes to the server through HTTP requests or swagger UI.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Deployment](#deployment)

## Prerequisites
- Docker
- Python 3.8 or higher
- Linux operating system

## Installation
1. Clone the repository:
```
git clone https://github.com/MakaronToja2/RecipeAPIProject
```
2. Change the working directory
```
cd RecipeAPIProject
```
3. Build a new container for the project
```
docker-compose build
```
4. Start a container with a server
```
docker-compose up
```
## Usage

To use RecipeAPIProject we can use HTTPS requests, but go to 127.0.0.1:8000/api/docs. 
There you can find all the endpoints available.

## Examples
Open Terminal and type for example:
```shell
curl -X POST http://127.0.0.1:8000/api/user/create/ \
     -H "Content-Type: application/json" \
     -d '{"email": "user@example.com", "password": "password123", "name": "user"}'
```
Now to retrieve a token for authorization:
```shell
curl -X POST http://127.0.0.1:8000/api/user/token/ \
     -H "Content-Type: application/json" \
     -d '{"email": "user@example.com", "password": "password123", "name": "user"}'
```

Now to authorize we get token from previous command and POST new recipe with it:
```shell
curl -X POST http://127.0.0.1:80/api/recipe/recipes/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Token YOUR_AUTHENTICATION_TOKEN" \
     -d '{
           "title": "string",
           "time_minutes": 2147483647,
           "price": "-4",
           "link": "string",
           "tags": [
             {
               "name": "string"
             }
           ],
           "ingredients": [
             {
               "name": "string"
             }
           ],
           "description": "string"
         }'
```

And now to get all the recipes from this specific user:
```shell
curl -X GET http://127.0.0.1:80/api/recipe/recipes/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Token YOUR_AUTHENTICATION_TOKEN"
```
## Deployment
The code is ready for deployment for AWS it needs to be configured.</br>
Due to the costs of AWS, I was not able to deploy the server.</br>
<h2>I hope you like the project and have fun with it! Cy@</h2>
