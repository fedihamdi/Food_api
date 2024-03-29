# Membre du groupe
Nom - Prenom - Email

HAMDI - Fedi - fedihamdi@yahoo.com

DOUZI - Ali - a_douzi@hetic.eu

KARA - Redouane - r_kara@hetic.eu

DEBBICHE - Dorra - d_debbiche@hetic.eu

AOUISSAT - Maha Amani - m_aouissat@hetic.eu

ERRAGRAGUI - Ayoub - a_erragragui@hetic.eu


# Les champs interresantes d'OpenFacts

- Le nom : **"product_name"**

- La marque : **"brands"**

- La note nutri-score : **"nutriscore_score"**


# Food Buy API

## Ressources

* Project objectives : 

## Dependencies

* Anaconda or Miniconda: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html

## Setup

1. Create a new conda env named md4-api (if you haven't already) for the project in the Conda application or in the terminal:
```
conda create --name md4-api python=3.7 
```

2. Activate the conda env (you can check your availables env with: conda env list):
```
conda activate md4-api
```

3. Install the project python dependencies :
```
pip install -r requirements.txt
```

4. Install flask in your terminal to be able to launch it:
```
conda install -c conda-forge flask
```

5. Launch the API :
```
flask run --port=3000
```

## Development

To enable automatic re-launch of the API (hot reload) when there is a code update, launch flask like this:
```
FLASK_DEBUG=1 flask run --port=3000
```

## Database

To connect to a database, you must set the environment variable `DATABASE_URL` in the .env file with a valid connection URI.

Example of PostgreSQL uri:
```
DATABASE_URL=postgresql://user:password@database_host:database_port/database_name
```

To apply the database migrations (located in migrations/versions), you can use this command:
```
flask db upgrade
```

To create a new migration, you can use this command and then apply the previous command:
```
flask db migrate -m "Migration message"
```

If your database is empty and you want some random data to start working with your API, you can use this command:
```
flask seed
```
It will fill your database with a test user.

## OpenFoodFacts API



## Docker Setup in the cloud
1. Install docker on the EC2 instance :

```
sudo yum update -y

sudo amazon-linux-extras install docker

sudo service docker start

sudo systemctl enable docker

sudo usermod -a -G docker ec2-user
```

you should make sre that your EC2 can get access to your ECR where you pushed the docker image and to authentificate to get docker run smothely.

2. Run this command

```
aws ecr get-login-password --region eu-west-3 | docker login --username AWS --password-stdin 306429642422.dkr.ecr.eu-west-3.amazonaws.com
```

## Docker run commands in the cloud
```
docker run -p 3000:3000 -e DATABASE_URL=postgresql://postgres:12345678@foodbuy-database.ctdyoxnqbfvo.eu-west-3.rds.amazonaws.com:5432/foodbuy_database -e JWT_SECRET_KEY=xxx -e OPEN_FOOD_FACT_URL=https://world.openfoodfacts.org 306429642422.dkr.ecr.eu-west-3.amazonaws.com/foodbuy-api:latest
```
## docker-compose
1. To start the docker compose 
```
docker compose up 
```

2. To shuttdown the docker compose 

```
docker compose down
```
## Project structure


-- cli : this folder will code to define custom flask commands
    
-- database : this folder will contains all database models
    
----- models.py : contains class definitions for each database model

-- migrations : generated by the Flask CLI (flask db init)
    
----- versions : will contains the list of database migrations

------- xxx.py : "xxx" will be replaced by a migration ID and commit message

-- resources : this folder will contains all the resources of the API
    
----- xxx.py : "xxx" will be replaced by the resource name

-- app.py : the main API file that will list all the available endpoints

-- config.py : this file will contain the configuration of the api

-- requirements.txt : this files will list the dependencies of the project

