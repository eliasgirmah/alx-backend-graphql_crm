# alx-backend-graphql_crm

This is a simple Django project demonstrating how to set up a GraphQL endpoint using **graphene-django**.

## Features

- Django backend with a GraphQL endpoint
- Basic GraphQL schema with a `hello` query returning a greeting message
- GraphiQL interface enabled for easy query testing

## Setup Instructions

### Prerequisites

- Python 3.x
- Git

### Installation Steps

1. **Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/alx-backend-graphql_crm.git
cd alx-backend-graphql_crm

Create and activate virtual environment

On Linux/macOS:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
On Windows (PowerShell):

powershell
Copy
Edit
python -m venv venv
.\venv\Scripts\Activate.ps1
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
(If you don't have a requirements.txt yet, run:)

bash
Copy
Edit
pip install django graphene-django django-filter
pip freeze > requirements.txt
Run migrations

bash
Copy
Edit
python manage.py migrate
Run the development server

bash
Copy
Edit
python manage.py runserver
Test GraphQL Endpoint

Open your browser and navigate to:

bash
Copy
Edit
http://localhost:8000/graphql
Try running this query in GraphiQL:

graphql
Copy
Edit
{
  hello
}
You should see:

json
Copy
Edit
{
  "data": {
    "hello": "Hello, GraphQL!"
  }
}
Project Structure
alx_backend_graphql_crm/ — Django project folder

crm/ — Django app folder

alx_backend_graphql_crm/schema.py — GraphQL schema definition