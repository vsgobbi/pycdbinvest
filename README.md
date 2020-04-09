## Flask API Project with VueJs Frontend Client

## Description
Project develop using Flask and VueJs in order to deploy at Amazon Web Services, using Lambda environment.
Using serverless framework to deploy on localhost and to AWS as well. NodeJS Axios to route client requests using VueJs
framework. This project is ***GPL v3.0 licensed***.

## Table of Contents


- [Installation](#installation)
- [Running application](#running)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Crate virtualenvironment 'venv' using Python3.7
```
$ virtualenv -p python3.7 venv
$ source venv/bin/activate
```
### Install requirements
```
$ pip install -r requirements
```
### In order to deploy web applications on localhost or on AWS Lambda and AWS API Gateway use Serverless framework:
```
$ npm install -g serverless
```
### Install serverless plugins:
```
$ sls plugin install -n serverless-wsgi
$ sls plugin install -n serverless-python-requirements
```
### Use the 'default' created config in ~/.aws/config
### Create default bucket
### check serverless.yml and deploy: 
```
$ sls wsgi serve
```
### Running app in aws lambda:
```
$ sls deploy
```
### Checking logs from application:
```
$ sls logs -f app
```
### Creating VUEjs front end application:
### first install nodejs and npm
### Install vue cli: 
```
$ npm install -g @vue/cli
```
### Create VUE project 'client' for Single Page Application
```
$ vue create client
```
### Install vuetify and select 'Default' preset:
```
$ cd client && vue add vuetify
```
### Install nodejs Axios on client to consume our API:
```
$ npm install -S axios
```
### Deploy frontend and run client 
```
$ npm run serve
```

## Running
### check serverless.yml and deploy on localhost: 
```
$ sls wsgi serve
```
### Running app in aws lambda:
```
$ sls deploy
```
### Run VUEjs application locally to test client frontend
```
$ npm run serve
```

## Contributing

- **Step 1**
    - 🍴 Fork this repo!

- **Step 2**
    - 🔨🔨 Clone this repo to your local machine using `https://github.com/vsgobbi/pycdbinvest`

- **Step 3**
    - 🔃 Create a new pull request using 
    <a href="https://github.com/vsgobbi/pycdbinvest/compare/" target="_blank">`https://github.com/vsgobbi/pycdbinvest/compare`</a>

### Runnign Tests:

## License

 [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
- **[GPL license](https://www.gnu.org/licenses/gpl-3.0)**
- Copyright 2020 © <a href="https://github.com/vsgobbi" target="_blank">Vitor Gabriel Sgobbi</a>.