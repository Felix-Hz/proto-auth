# Auth API App

Welcome to the documentation for the `auth_api` app in my Django project. This app handles user authentication, user information, and related interactions. Below, you'll find details about the functionality, methods, and interactions provided by the `auth_api` app.

## Overview

The `auth_api` app serves as the backbone for user authentication within my Django project. It manages user accounts, authentication processes, and provides endpoints for user-related actions.

## Setup

To integrate the `auth_api` app into my Django project, follow these steps:

1. **Install Dependencies**: Ensure Django is installed in your project environment.
2. **Run Migrations**: Execute database migrations to create the necessary tables for user authentication.

## Endpoints

The `auth_api` app provides the following endpoints for user authentication and management:

- `/auth_api/register`: Register a new user.
- `/auth_api/login`: Log in an existing user.
- `/auth_api/logout`: Log out the current user.
- `/auth_api/publish`: Publish a post.
- `/auth_api/react`: React to a post.

<!--
                    --------------------
                    ~ Work in Progress ~
                    --------------------

- `/api/auth/user/`: Retrieve the details of the current user.
- `/api/auth/user/update/`: Update the details of the current user.
- `/api/auth/user/change-password/`: Change the password of the current user.
- `/api/auth/password-reset/`: Initiate the password reset process.
- `/api/auth/password-reset/confirm/`: Confirm the password reset request.
  -->

## Models

The `auth_api` app defines the following models:

- `User`: Represents a user in the system. It includes fields such as username, email, password, etc.
- `Post`: Represents a post in the system.
- `Comment`: Represents a comment in the system.
- `Reaction`: Represents the interaction between users in the system. It can be positive (like) or negative (dislike).

## Views

The `auth_api` app includes views for handling user authentication, registration, password reset, and user profile management.

## Authentication

The `auth_api` app utilizes token-based authentication for user sessions. Upon successful login, the user receives a token that is used for subsequent authenticated requests.

## Permissions

Permissions are managed to ensure that only authenticated users can access certain endpoints, while others may be accessible to both authenticated and anonymous users.
