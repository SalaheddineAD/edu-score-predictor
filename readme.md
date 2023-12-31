# edu-score-predictor
## Overview
EduScorePredictor is an end-to-end solution designed to harness the power of machine learning to predict student performance. Built with Python and fully deployed on AWS, it encapsulates the essence of MLOps with data ingestion, transformation, and model training pipelines for educational analytics.
![Screenshot of the web-app](https://github.com/SalaheddineAD/edu-score-predictor/assets/93080778/fb4b38e1-638f-432d-8f40-a94ae97727be)
![edu-scrore](https://github.com/SalaheddineAD/edu-score-predictor/assets/93080778/6b75b429-e122-4872-a541-a7ac4155055d)
![edu-scrore3](https://github.com/SalaheddineAD/edu-score-predictor/assets/93080778/8b05a148-925a-4c27-8ec8-0698f06a7bdd)

## Features
- Data Ingestion: Automate the collection of data in a secure and scalable manner.
- Data Transformation: Preprocess and clean data to ensure quality and consistency.
- Model Training: Develop robust machine learning models with CatBoost.
- Prediction Pipeline: Generate predictions on student performance with trained models.
- Training Pipeline: Streamline the training of models with continuous integration.
- Deployment: Deploy the solution on AWS with Docker, ensuring high availability and scalability.
- Logging: Maintain comprehensive logs to track the system's performance and health.
## Installation
To set up the EduScorePredictor on your local machine, follow these steps:

- Clone the repository to your local machine.
- Ensure that you have Python 3.x installed.
- Install the required dependencies with pip install -r requirements.txt.
- Navigate to the src directory and run python application.py to start the application.
## Usage
After installation, execute the following commands to run the prediction and training pipelines:
- python -m src.pipeline.predict_pipeline
- python -m src.pipeline.train_pipeline
## Documentation
For detailed information on the project setup, components, and usage, refer to documentation.txt.
