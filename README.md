# Todo App - Microservices Architecture with FastAPI

This repository contains a Todo application built using a microservices architecture. The app consists of four microservices, each handling specific functionality: Authentication, User Management, Todo Management, and Notifications.

## Overview

This project is designed using **FastAPI** with **microservices architecture**, where each service is isolated and handles its own domain logic. This helps in scaling each service independently and allows for better maintainability.

The application has the following core functionalities:

- User registration, authentication, and management.
- Creating and managing todo items.
- Sending notifications (e.g., email) based on specific triggers.
- Token-based authentication and secure communication.

## Services

### Auth Service

- Handles user authentication using JWT tokens.
- Issues access tokens upon successful login.
- Secures endpoints requiring authentication.

### User Service

- Manages user profiles.
- Handles CRUD operations for user-related information.
- Includes password reset functionality.

### Todo Service

- Handles creating, updating, and managing todos.
- Each todo is associated with a specific user.
- Provides endpoints for filtering and retrieving todos.

### Notification Service

- Handles sending notifications (emails or SMS) when triggered by events.
- Can be integrated to send reminders for due tasks or confirmation emails.

## Technologies Used

- **FastAPI**: High-performance web framework for building APIs.
- **SQLAlchemy**: ORM for managing databases.
- **SQlite**:for local development
- **PostgreSQL**: Database for managing persistent data.
- **Docker**: Containerization platform for easy deployment.
- **Redis**: For caching and handling notifications.
- **JWT (JSON Web Tokens)**: For authentication.
- **Nginx**: Used as a reverse proxy.
- **Pydantic**: For data validation.

## Getting Started

To get started with this project, you will need to have Docker and Python 3.9+ installed. Follow the steps below to set up the development environment.

### Prerequisites

- Python 3.9+
- Docker and Docker Compose
- Sqlite for local development
- PostgreSQL for each service’s database
- Redis for notification service

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/todo-microservices.git
   cd todo-microservices
   ```
