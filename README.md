# Emerging Technologies Project
Author: William Vida.
<br>
Lecturer: Dr Ian McLoughlin.

## About the Project
This repository contains my solutions to my project as part of my final year module Emerging Technologies. The objective was to create a web service that uses machine learning to make power production predictions based on inputted speed data based on an existing wind turbine dataset. `index.html` contains four different machine learning models to calculate power production based on speed input. The machine learning models include linear regression (inaccurate most of the time), polynomial regression (accurate most of the time), k-nearest neighbours regression (accurate) and a neural network (accurate).

Open the `Project 2020 assessment.pdf` file to view the project brief.
<br>
Open `powerproduction.csv` to view the wind turbine dataset.
<br>
Open `Project.ipynb` to view the research, progress and the different machine learning models used.

## Getting Started
### Prerequisites
Either or both of Docker and Flask have to be installed.
<br>
Docker download link https://docs.docker.com/docker-for-windows/install/.
<br>
Flask download link https://pypi.org/project/Flask/.

### Downloading the Project
1. Clone the repo
   ```sh
   git clone https://github.com/WilliamVida/EmergingTechnologiesProject
   ```
2. Enter the directory.
  
### Run Using Docker
Enter the following in a command line
```bash
docker build . -t emerging-technologies-project
docker run --name emerging-technologies-project-container -d -p 5000:5000 emerging-technologies-project
```

Then open http://127.0.0.1:5000/ in a web browser to view the webpage and to make power production predictions.

To list the Docker containers
```bash
docker container ls
```	

To list the Docker images
```bash
docker image ls
```

To kill the Docker container
```bash
docker kill [CONTAINER ID]
```

To remove the Docker container
```bash
docker rm [CONTAINER ID]
```

### Run Without Using Docker
#### Windows
```bash
set FLASK_APP=app.py
python -m flask run
```

#### Linux
```bash
export FLASK_APP=app.py
python3 -m flask run
```

Then open http://127.0.0.1:5000/ in a web browser to view the webpage and to make power production predictions.

## Acknowledgments
Dr Ian McLoughlin.
<br>
All those whom I have referenced in `Project.ipynb`.
