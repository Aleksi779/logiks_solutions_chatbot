# logiks_solutions_chatbot


# How to run?
### Steps:


Clone the repository


```bash 
Project repo: https://github.com
```

### Step 01 - Create a conda environment after opening the repository

```bash
conda create -n llmapp python=3.13 -y
```

```bash
conda activate llmapp
```

### Step 02 - Install the requirements
```bash
pip install -r requirements.txt
```

### Step 03 - Create a .env file in the root directory and add your Pinecone & openai api keys as follows:

```ini
PINECONE_API_KEY="xxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY="xxxxxxxxxxxxxxxxxxxxxx"
```

```bash
# Run following command to store embeddings to pinecone
python store_index.py
```

```bash
# Run the following command to start the application
python app.py
```

Now,
```bash
open up localhost:
```

### Tech stack used:

- Python
- Langchain
- Flask
- GPT
- Pinecone


# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.
## 2. Create IAM user for deployment

#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess


## 3. Create ECR repo to store/save docker image

```bash
- Save the URI: 173813370223.dkr.ecr.eu-north-1.amazonaws.com/companychatbot
```

## 4. Create EC2 machine (Ubuntu)

## 5. Open EC2 and Install docker in EC2 Machine:

#optional

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker


## 6. Configure EC2 as self-hosted runner:

```bash
setting>actions>runner>new self hosted runner> choose os> then run command one by one
```

## 7. Setup github secrets:

* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY
* AWS_DEFAULT_REGION
* ECR_REPO
* PINECONE_API_KEY
* OPENAI_API_KEY