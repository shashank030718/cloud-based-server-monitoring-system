# Cloud-Based Server Monitoring System

## Project Overview

A containerized server monitoring system built using Python, FastAPI, psutil, Docker, and Docker Compose.

The system monitors CPU usage, memory utilization, disk usage, uptime, and server health through a web dashboard.

## Features

- Real-time CPU monitoring
- Memory utilization monitoring
- Disk usage monitoring
- Server uptime tracking
- Health status reporting
- Threshold-based alerts
- REST API using FastAPI
- Interactive web dashboard
- Docker containerization
- Multi-container orchestration using Docker Compose

## Architecture

The application consists of two services:

- **Backend:** FastAPI application that collects system metrics using psutil.
- **Frontend:** HTML, CSS, and JavaScript dashboard served by Nginx.

Docker Compose manages both services and provides network connectivity.

## Technologies Used

- Python
- FastAPI
- Uvicorn
- psutil
- HTML
- CSS
- JavaScript
- Docker
- Docker Compose
- Nginx
- Linux (Ubuntu / WSL)

## Project Structure

cloud-monitoring-project/
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── server-monitor.sh
├── README.md
└── frontend/
    ├── Dockerfile
    ├── index.html
    ├── style.css
    └── script.js

## Deployment Using Docker Compose

### Start the application

docker compose up -d --build

### Check container status

docker compose ps

### View backend logs

docker compose logs backend

## Access the Dashboard

Frontend:
http://localhost:5501

Backend API:
http://localhost:8002/health

API Documentation:
http://localhost:8002/docs

## Stop the Application

docker compose down

## Learning Outcomes

- Linux server monitoring
- REST API development
- Docker image creation
- Docker container deployment
- Docker Compose orchestration
- Container networking
- Frontend and backend integration
- Application troubleshooting

## Author

Shashank M P

Cloud and DevOps Engineering Projects
