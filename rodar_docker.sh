#!/bin/bash
app="backend.model"
docker build -t ${app} .
docker run -d -p 8000:8000 --name=${app} -v $PWD:/app ${app}

