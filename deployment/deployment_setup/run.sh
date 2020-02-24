#!/bin/bash
cd /deployment

export FLASK_ENV=development
export FLASK_APP=deploy_app

/miniconda/bin/flask run