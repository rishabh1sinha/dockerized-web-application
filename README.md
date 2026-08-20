# Dockerized Web Application

**Intern Name:** Rishabh Kumar Sinha
**Intern ID:** CITS8600
**Internship:** CODTECH DevOps Internship

## Project Description

This project demonstrates how to containerize a Python Flask web application using Docker. The application provides a simple web page and a health-check endpoint. Docker is used to package the application and its dependencies into a portable container.

## Technologies Used

* Python
* Flask
* Docker
* Dockerfile
* GitHub

## Application Features

* Simple web application using Flask
* `/` endpoint for the main application page
* `/health` endpoint for application health status
* Dockerized application using a Python base image
* Application runs on port 5000

## Project Structure

```text
dockerized-web-application/
├── app.py
├── requirements.txt
├── Dockerfile
└── .dockerignore
```

## Docker Configuration

The Dockerfile performs the following steps:

1. Uses Python 3.12 as the base image.
2. Creates `/app` as the working directory.
3. Copies the Python dependencies.
4. Installs Flask.
5. Copies the application code.
6. Exposes port 5000.
7. Starts the Flask application.

## How the Application Works

```text
User
  ↓
Flask Web Application
  ↓
Docker Container
  ↓
Port 5000
```

The application displays a welcome page at the root URL and provides a health endpoint that returns the application's status.

## Docker Commands

Build the Docker image:

```bash
docker build -t dockerized-web-app .
```

Run the container:

```bash
docker run -p 5000:5000 dockerized-web-app
```

The application can then be accessed at:

```text
http://localhost:5000
```

Health check:

```text
http://localhost:5000/health
```

 Expected Result

The main page displays:

> Dockerized Web Application

The health endpoint returns:

```json
{
  "status": "healthy"
}
```

Learning Outcome

This project demonstrates the fundamentals of Docker containerization, including Dockerfiles, Docker images, containers, port mapping, dependency installation, and running a Python web application inside a container.

**CODTECH Intern ID: CITS8600**
