# Flask Blog Application

This project is a small blog application built with Flask.  
It demonstrates basic web development concepts such as routing, templates, form handling, JSON-based storage, and simple CRUD operations.

## Features

- Display all blog posts  
- Add new posts through a form  
- Edit existing posts  
- Delete posts  
- Like posts  
- Store data in a JSON file without a database  

## Installation

### Requirements
- Python 3.8 or higher  
- Flask  

Install Flask:

```bash
pip install flask
```

## Project Structure

```
project/
│
├── app.py
├── blog_postes.json
│
├── templates/
│   ├── index.html
│   ├── add.html
│   ├── update.html
│
└── static/
    └── style.css
```

## Purpose of the Project

This project is designed as a simple learning exercise to understand how Flask works.  
It covers:

- Basic routing  
- GET and POST requests  
- Jinja2 templates  
- Handling forms  
- Lightweight data storage using JSON  
- Implementing small CRUD systems  
