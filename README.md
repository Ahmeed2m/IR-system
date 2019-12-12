# IR System
Course Project Information Storage and retrieval (IS313) 

The project is a simple IR system which indexes N documents in JSON format (DataCollection Folder) using 3 diffrent methods (Inverted Index, Positional Index and TF-IDF) to be able to serve two kinds of queries (Phrase query and Free text query)

The project is divided into two parts frontend and backend. ReactJS communicating with Python Flask server accessing indexed files and matching the query text with the mentioned algorithms.

## 1. Requirements

In order to run this project you need to have python3 preferably 3.5 and later, npm installed and a working 'modern' browser

#### 1.1 Required pacakages installation.

First you have to clone this repo
>git clone https://github.com/Ahmeed2m/IR-system

##### 1.1.1 Python: 
For backend/python part you'd need to install the requirements.txt file
with this command excuted from the repo's root
>pip install -r back/requirements.txt

##### 1.1.2 JavaScript
For the frontend/js part you need to run this command from the repo's root
>npm  --prefix interface install

## 2. Running
The project is currently deployed on Heroku from the heroku branch. You can check that out at [url]

#### 2.1 Running locally
In `package.json` we defined some npm scripts to help running the flask and react servers together.

There are two ways of running either a live reactJS server listening to the flask server. (this way is useful for development only - for live updates).
Or running production build (cached) of the reactJS projcet with the flask running along side. (suitable for deployment and trying the app)

For the production run you'd build the project only one time with 
> npm run --prefix interface build

and the command you'd use afterwards for opening the cached server
> npm run --prefix interface production

with that you'll have the project running at [localhost:5000](http://localhost:5000)

The other way for development purposes to see every live update in react code you'd run
> npm run --prefix interface dev 

with that you'll have the project running at [localhost:3000](http://localhost:3000)
