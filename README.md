# Simple Task Manager SPA

A lightweight Single Page Application (SPA) task manager built with **Django**, using modern frontend techniques like **HTMX**, **Alpine.js**, **Tailwind CSS**, and **DaisyUI**. This project demonstrates how to create a reactive, dynamic web app with minimal JavaScript while leveraging Django templates.

---

## Features

- **Task CRUD**: Create, Read, Update, and Delete tasks.
- **Search by Name**: Filter tasks dynamically by typing their name.
- **Ordering**: Sort tasks directly in the table by selecting the appropriate column name.
- **Row Details**: Expand a task to see detailed information.
- **Transitions & Animations**: Smooth transitions when adding, updating, or deleting tasks.
- **Throttling**: Efficient input handling to reduce unnecessary requests.
- **Responsive Design**: Fully responsive layout using Tailwind CSS + DaisyUI.
- **SPA-like Experience**: Minimal page reloads thanks to HTMX and Alpine.js.

---

## Tech Stack

- **Backend**: Django
- **Frontend**: 
  - Django templates
  - HTMX (for dynamic HTML updates)
  - Alpine.js (for lightweight interactivity)
  - Tailwind CSS + DaisyUI (for styling and components)
- **Containerization**: Docker for easy setup and deployment

---

## Screenshots

<img width="1919" height="909" alt="image" src="https://github.com/user-attachments/assets/30b43fb4-c336-4ff8-aa85-1122c4a7dd40" />
<img width="1919" height="910" alt="image" src="https://github.com/user-attachments/assets/01875ef4-38a3-409e-aa62-ce136146ea2e" />

---

## Installation

### Using Docker (Recommended)

Build and run the container:

```bash
docker build -t simple-task-manager .
docker run -p 8000:8000 simple-task-manager
