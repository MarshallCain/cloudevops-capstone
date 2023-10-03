[![CircleCI](https://dl.circleci.com/status-badge/img/gh/MarshallCain/cloudevops-capstone/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/MarshallCain/cloudevops-capstone/tree/main)

## Project Overview

This project represents is my capstone submission for Udacity Cloud DevOPs Engineer Nanodegree Program.

In this project I have taken a simple website. Then using the flask framework library in python I have created a web app out of it. Then using Docker I have containerised it i.e. created Docker images and I am storing them on Amazon ECR container repository. After that I am using an Amazon EKS cluster to host and run the images. All of this is done via Circle CI pipeline. A little bit of Anisble has also been used for deployment in Circle CI pipelines.

### What I learnt

- Using Circle CI to implement Continuous Integration and Continuous Deployment
- Cloud Native approach to CI and CD
- Using AWS to host my applications
- Containerising images using Docker Engine
- Building Kubernetes clusters
- Working with Ansible

### Project Pre-requisites

- An AWS EKS named "kush-capstone-cluster" needs to be created beforehand in order for this project to work with help of eksctl.
- Python 3.10.12
- Linux OS only

---

## PipeLine Overview

The pipeline buids a docker image out of the source code, uploads the image to ECR and then deploys to AWS EKS cluster ina rolling update fashion. 

### Steps

1. Whenver a new commit arrives, automcatically kick off and build the python flask app in a Vitual env.
2. Lint the app
3. Unit Test the app
4. Create a Docker image with help of Docker file.
5. Upload the Docker image with both a unique and latest tag for supporting rolling deployments.
6. Push the image to Amazon ECR private container repo.
7. Next Configure the AWS EKS cluster with kubectl using Ansible.
8. Apply the Deployment and Service using Ansible. 
9. Depploy the latest app thats has been built in pipeline.

---

## Directory Structure

| Directory/File | Description |
| ---- | ----------- |
| `.circleci/config.yml` | CircleCI configuration |
| `ansible` | Ansible for configuring and deploying to EKS cluster |
| `Screenshots_and_links` | Contains Screenhots and Links for the app succesful run |
| `static` | Contains website static code |
| `templates` | Contains the HTML file which is rendered by Flask library |
| `app.py` | The main application file |
| `Dockerfile` | Dockerfile containing the application and its dependencies for building images |
| `Makefile` | Build file of the project |
| `requirements.txt` | Python requirements file |
| `run_docker.sh` | Shell script for building and running docker image |
| `testflask.py` | Sample Unit test file for python app |
| `upload_docker_image_to_dockerhub.sh` | Shell script for uploading local docker image to dockerhub repository. Not required in pipeline. |
