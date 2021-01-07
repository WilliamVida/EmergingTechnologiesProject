# Emerging Technologies Project
Authored by William Vida.
<br>
Lecturer: Dr Ian McLoughlin.

## About the Project
This repository contains my solutions to my project as part of my final year module Emerging Technologies. The objective was to create a web service that uses machine learning to make power production predictions based on inputted speed data based on data. The `index.html` contains four different machine learning models to calculate power production. The machine learning models include linear regression (inaccurate), polynomial regression (accurate), k-nearest neighbours regression (accurate) and a neural network (accurate).

Open the `Project 2020 assessment.pdf` file to view the project brief.
<br>
Open `Project.ipynb` to view the research, progress and the different models used. Open `powerproduction.csv` to view the dataset.

## Getting Started
### Downloading the Project
1. Clone the repo
   ```sh
   git clone https://github.com/WilliamVida/EmergingTechnologiesProject
   ```
2. Enter the directory.
  
### Run Using Docker
```bash
docker build . -t emerging-technologies-project
docker run --name emerging-technologies-project-container -d -p 5000:5000 emerging-technologies-project
```

Then open http://127.0.0.1:5000/ in a web browser to view the webpage and to make power production predictions.

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

To list the images
```bash
docker image ls
```

Then open http://127.0.0.1:5000/ in a web browser to view the webpage and to make power production predictions.

To kill the Docker container
```bash
docker kill [CONTAINER id]
```

To remove the container
```bash
docker rm [CONTAINER ID]
```

## Acknowledgments
Dr Ian McLoughlin.
<br>
All those whom I have referenced in `Project.ipynb`.
