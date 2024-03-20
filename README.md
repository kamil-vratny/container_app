# Container application CodePipeline Demo

## Files
* Dockerfile - docker image definition
* backend_main.py - FastAPI based application
* buildspec.yml - CodeBuild spec file

## Github Connection
use V2

## CodePipeline
* source - Github
* trigger - no filter
* build provider - AWS CodeBuild
* deployment - AWS CodeDeploy
    * ECS Service - Blue/Green (AWS CodeDeploy)
