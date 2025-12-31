# Foundation & Auth System

A scalable full-stack web application featuring a robust authentication system and a role-based dashboard. Built with **Next.js** for the frontend and **Django REST Framework** for the backend.

## 🚀 Features

- **JWT Authentication**: Secure login and registration using JSON Web Tokens.
- **Role-Based Access Control (RBAC)**: 
  - `GENERAL_USER`: Standard access.
  - `TEAM_MEMBER`: Access to team-specific actions.
  - `SYSTEM_ADMINISTRATOR`: Full system access and admin panel.
- **Modern Frontend**: Built with Next.js 15+, Tailwind CSS, and React Context for state management.
- **Robust Backend**: Python-based Django API with a clean architecture and SQLite database.
- **Responsive Design**: Fully responsive UI that works across desktop and mobile.

## 📁 Project Structure

- `backend/`: Django project containing the API logic and user models.
- `frontend/`: Next.js application for the user interface.
- `conductor/`: Project documentation and architecture specs.

## 🛠️ Tech Stack

- **Frontend**: Next.js, React, Tailwind CSS.
- **Backend**: Python, Django, Django REST Framework, SimpleJWT.
- **Database**: SQLite (Development).

## 🚦 Getting Started

### Prerequisites

- Node.js (v18+)
- Python (v3.10+)

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```

## 🧪 Testing

- **Backend**: Run `python manage.py test`
- **Frontend**: Run `npm test`

## 🔐 Security Features

- Password hashing with Bcrypt (via Django defaults).
- JWT token blacklisting for secure logout.
- Protected API endpoints using `IsAuthenticated` permissions.
- Frontend `RoleGuard` to prevent unauthorized UI access.
