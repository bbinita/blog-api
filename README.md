# Blog API

A REST API for managing blog posts, comments, and categories, built with Django and Django REST Framework. Supports full CRUD operations, category-based filtering, and nested serialization.

## Tech Stack
- Python
- Django
- Django REST Framework

## Setup

```bash
git clone https://github.com/bbinita/blog-api.git
cd blog-api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Endpoints

### Posts
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/post/` | List all posts |
| POST | `/api/post/` | Create a post |
| GET | `/api/post/<id>/` | Retrieve a post |
| PUT | `/api/post/<id>/` | Update a post |
| DELETE | `/api/post/<id>/` | Delete a post |
| GET | `/api/post/?category=1` | Filter posts by category |

### Categories
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/category/` | List all categories |
| POST | `/api/category/` | Create a category |
| GET | `/api/category/<id>/` | Retrieve a category |
| PUT | `/api/category/<id>/` | Update a category |
| DELETE | `/api/category/<id>/` | Delete a category |

### Comments
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/comment/` | List all comments |
| POST | `/api/comment/` | Create a comment |
| GET | `/api/comment/<id>/` | Retrieve a comment |
| PUT | `/api/comment/<id>/` | Update a comment |
| DELETE | `/api/comment/<id>/` | Delete a comment |
