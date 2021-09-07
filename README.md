About project.

This project is built for guessing what brazilian football team a news article is about. The friendly UI says it all: paste an article into the textarea, press the button and get the team name.

Reproducing:

docker-compose up --build
When built: localhost:8000 to access the react app.

Architecture:
This project consists of four containers. Also there is an inital notebook in the repo, but without data. If needed it can be downloaded from kaggle: https://www.kaggle.com/lgmoneda/ge-soccer-clubs-news.

MLFlow server on port 5000 return the ui of MLFlow. It allows serving the model too.

Model on port 5005 serves the production model. Have in mind that this port is not exposed.

API on port 8000 has only one endpoint. It accepts news text, sends it to model and returns model's response. A little project from the data scraping course was taken as a boilerplate for this one, particularly, that's why it uses FastAPI, not Flask. Other than that it was redone completely, removing all templates and turning it into a REST server.

Web App on port 3000 is the web interface of this project. It uses redux + recoil. It is not a production build. On the other hand I doubt, that in real world anyone would deploy front end and backend with a single docker-compose anyway.

Metrics:

Best model is chosen by accuracy, for it is a multiclassification task which does not require any advanced metrics.

Dataset:

https://www.kaggle.com/lgmoneda/ge-soccer-clubs-news - club column was used as class.