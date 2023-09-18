#!/bin/bash

# Change directory to the desired location
cd technohub/main/static/main/src/styles

# Compile Sass files to CSS
sassc electricity_style.scss electricity_style.css
sassc plumbing_style.scss plumbing_style.css

# Navigate back to the original directory
cd ../../../../../..

# Stop and remove Docker containers defined in docker-compose.yml
docker-compose -f docker-compose.yml down

# Build Docker containers defined in docker-compose.yml
docker-compose -f docker-compose.yml build

# Start Docker containers in detached mode
docker-compose -f docker-compose.yml up -d
