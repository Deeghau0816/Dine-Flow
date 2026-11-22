# 🍽️ DineFlow — Restaurant Management & Reservation System

### A Modern Full-Stack Restaurant Website with Digital Menu Management, Online Reservations & Administrative Control

**DineFlow** is a modern, full-stack restaurant management web application designed to streamline restaurant operations and enhance the digital dining experience.

The platform combines an interactive restaurant website with a scalable backend architecture, enabling customers to explore menus and restaurant information while providing administrators with tools to manage menu categories, food items, and reservations.

Built using **React, TypeScript, FastAPI, and PostgreSQL**, DineFlow demonstrates modern full-stack development practices, RESTful API design, relational database modeling, authentication, and cloud-based media management.

**Project Type:** Personal Full-Stack Development Project  
**Architecture:** RESTful Client–Server Architecture  
**Frontend:** React + TypeScript  
**Backend:** Python + FastAPI  
**Database:** PostgreSQL

**GitHub Repository:** [DineFlow](https://github.com/Deeghau0816/Dine-Flow)

---

## 📖 Project Overview

Restaurants increasingly rely on digital platforms to showcase their menus, communicate with customers, and manage reservations efficiently.

However, many restaurant websites lack centralized management capabilities or require manual updates to menus and booking information.

DineFlow is designed to address these challenges by providing a unified platform for customer-facing restaurant services and administrative operations.

The project focuses on building a maintainable full-stack system with a responsive user interface, structured backend services, secure authentication, and reliable database operations.

### 🎯 Project Objectives

- Develop a responsive and user-friendly restaurant website.
- Provide a digital platform for browsing restaurant menus.
- Enable online table reservation workflows.
- Centralize menu and reservation management.
- Implement secure administrative authentication.
- Build scalable RESTful APIs using FastAPI.
- Maintain structured relational data using PostgreSQL.
- Support cloud-based image storage for restaurant content.

---

## 🚀 Key Features

### 🍕 1. Digital Restaurant Menu

- Organized food and beverage categories.
- Menu item listings with descriptions and pricing.
- Category-based menu browsing.
- Food item images.
- Dynamic content delivery through backend APIs.

### 📅 2. Online Reservation System

- Customer table reservation interface.
- Reservation date and time selection.
- Guest count management.
- Customer contact information collection.
- Reservation records stored in PostgreSQL.
- Administrative reservation management.

### 🛠️ 3. Restaurant Administration

- Centralized administrative functionality.
- Create, update, and delete menu categories.
- Manage food and beverage items.
- Organize restaurant menu information.
- Review and manage table reservations.
- Protected administrative endpoints.

### 🔐 4. Authentication & Authorization

- JWT-based authentication design.
- Cookie-based session handling.
- Protected backend routes.
- Administrative access controls.
- API authorization mechanisms.

### 🖼️ 5. Cloud-Based Image Management

- Cloudinary integration.
- Cloud-based storage for menu item images.
- Image URL management.
- Media delivery for restaurant content.

### 📱 6. Responsive User Interface

- Modern and clean restaurant website design.
- Mobile-friendly navigation.
- Responsive layouts.
- Reusable React components.
- Tailwind CSS-based styling.

**Development status:** DineFlow is under active development. Category CRUD and the initial backend infrastructure have been implemented. Menu-item CRUD, reservation CRUD, and admin authentication are part of the development roadmap; features described above are not all completed.

---

## 🛠️ Technology Stack

| Layer | Technologies |
|---|---|
| Frontend | React.js, TypeScript |
| Frontend Build Tool | Vite |
| Styling | Tailwind CSS |
| Backend | Python, FastAPI |
| ORM | SQLAlchemy |
| Database | PostgreSQL 17 |
| Database Migrations | Alembic |
| Authentication | JWT, HTTP Cookies (planned) |
| Media Management | Cloudinary (planned integration) |
| API Architecture | RESTful APIs |
| Backend Validation | Pydantic |
| Development & Deployment | Git, GitHub, Docker |

---

## 🏗️ System Architecture

DineFlow follows a modular client-server architecture, separating the user interface, business logic, and database operations.

```text
                     ┌──────────────────────────┐
                     │       DineFlow           │
                     │    Restaurant Website    │
                     │                          │
                     │   React + TypeScript     │
                     │   Vite + Tailwind CSS    │
                     └────────────┬─────────────┘
                                  │
                             HTTP / REST
                                  │
                     ┌────────────▼─────────────┐
                     │       FastAPI            │
                     │     Python Backend       │
                     │                          │
                     │  API Routers             │
                     │  Request Validation      │
                     │  Business Logic          │
                     │  Authentication          │
                     └────────────┬─────────────┘
                                  │
                             SQLAlchemy
                                  │
                     ┌────────────▼─────────────┐
                     │       PostgreSQL         │
                     │                          │
                     │  Menu Categories         │
                     │  Menu Items              │
                     │  Reservations            │
                     │  Admin Users             │
                     └──────────────────────────┘

                     External Integration
                     ┌──────────────────────────┐
                     │        Cloudinary        │
                     │     Image Management     │
                     └──────────────────────────┘
```

*The architecture includes planned components as well as implemented infrastructure.*

### Architecture Components

**Frontend — React + TypeScript**

Provides responsive restaurant interfaces and reusable components for displaying menu items, restaurant information, and reservation workflows.

**Backend — FastAPI**

Handles API requests, data validation, business logic, database operations, and planned authentication mechanisms.

**Database — PostgreSQL**

Stores relational application data, including menu categories and planned menu-item, reservation, and administrator records.

**ORM — SQLAlchemy**

Provides database models and structured interaction with PostgreSQL.

**Database Migrations — Alembic**

Manages schema evolution through version-controlled migrations.

**Media Storage — Cloudinary**

Planned for storing and delivering restaurant images and menu-related media.

---

## 📂 Project Structure

An illustrative organization of the full-stack application:

```text
Dine-Flow/
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── assets/
│   │   ├── App.tsx
│   │   └── main.tsx
│   │
│   ├── package.json
│   └── vite.config.ts
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── core/
│   │   ├── db/
│   │   └── main.py
│   │
│   ├── alembic/
│   ├── alembic.ini
│   └── requirements.txt
│
├── docker-compose.yml
└── README.md
```

*Note: This is a reference structure and should be adjusted to match the actual repository.*

---

## ⚙️ Installation & Setup

### Prerequisites

- Node.js and npm
- Python 3.10+
- PostgreSQL
- Git
- Docker (optional)

### 1. Clone the Repository

```bash
git clone https://github.com/Deeghau0816/Dine-Flow.git
cd Dine-Flow
```

### 2. Configure the Backend

Navigate to the backend directory:

```bash
cd backend
```

Create a Python virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file for application configuration.

Example:

```env
DATABASE_URL=postgresql+psycopg://username:password@localhost:5432/dineflow
SECRET_KEY=replace_with_secure_random_secret
```

Environment variable names and database driver requirements should match the actual backend configuration.

Never commit production credentials or secret keys.

### 4. Run Database Migrations

Once PostgreSQL is running and the database connection is configured:

```bash
alembic upgrade head
```

### 5. Start the FastAPI Backend

For a backend exposing `app/main.py`:

```bash
uvicorn app.main:app --reload
```

Default local API URL:

`http://127.0.0.1:8000`

Interactive API documentation:

`http://127.0.0.1:8000/docs`

### 6. Configure the Frontend

Open another terminal and navigate to the frontend directory:

```bash
cd frontend
npm install
```

Start the development server:

```bash
npm run dev
```

Default Vite development URL:

`http://localhost:5173`

*These commands describe a conventional FastAPI/Vite setup. Verify the actual folders, environment variables, scripts, and ports in the repository before use.*

---

## 🔌 API Development

DineFlow uses RESTful APIs to support communication between its frontend and backend.

### Example API Modules

| Module | Operations | Status |
|---|---|---|
| Health | Backend health check | Implemented |
| Categories | Create, Read, Update, Delete | Implemented |
| Menu Items | Create, Read, Update, Delete | Planned |
| Reservations | Create, Read, Update, Delete | Planned |
| Authentication | Login, Logout, Access Control | Planned |
| Media | Image upload and management | Planned integration |

FastAPI provides interactive documentation for testing and inspecting registered endpoints through Swagger UI.

---

## 🗄️ Database Design

The database architecture is organized around key restaurant management entities.

### Core Entities

**Category**
- Category identifier
- Category name
- Description
- Associated menu items

**Menu Item (Planned)**
- Menu item identifier
- Item name
- Description
- Price
- Category reference
- Image URL
- Availability status

**Reservation (Planned)**
- Reservation identifier
- Customer details
- Reservation date and time
- Number of guests
- Reservation status

**Admin User (Planned)**
- Administrator identifier
- Authentication credentials
- Administrative access permissions

The implemented category model and the planned entities should be validated against the actual database schema.

---

## 🔐 Security Considerations

The application architecture includes provisions for:

- JWT-based authentication.
- Secure HTTP cookie handling.
- Password hashing.
- Protected administrative API routes.
- Request validation through Pydantic.
- Environment-based secrets management.
- Database access through SQLAlchemy.

Authentication and authorization are planned components and should not be considered production-ready until implemented and tested.

---

## 📈 Development Progress

| Development Component | Status |
|---|---|
| React + TypeScript + Vite Setup | Completed |
| Tailwind CSS Integration | Completed |
| FastAPI Backend Setup | Completed |
| PostgreSQL 17 Integration | Completed |
| SQLAlchemy Configuration | Completed |
| Alembic Database Migrations | Completed |
| Backend Health API | Completed |
| Category CRUD Operations | Completed |
| Menu Item CRUD | Next |
| Reservation CRUD | Planned |
| Admin Authentication | Planned |
| Cloudinary Image Integration | Planned |
| Full-System Testing | Planned |

---

## 🔮 Future Enhancements

- Real-time table availability.
- Reservation confirmation emails.
- Reservation conflict prevention and capacity management.
- Automated booking reminders.
- QR-code-based digital menus.
- Restaurant analytics dashboards.
- Order management integration.
- Customer reviews and ratings.
- Cloud hosting and production deployment.
- Comprehensive unit and integration testing.

---

## 👨‍💻 Developer

**Deeghau Vidarshana Premasiri**

Data Science Undergraduate  
Sri Lanka Institute of Information Technology (SLIIT)

Interests: Full-Stack Development, Artificial Intelligence, Machine Learning, Data Engineering, and Intelligent Software Systems.

**GitHub:** [Deeghau0816](https://github.com/Deeghau0816)

---

## 📄 License

No license is specified in this README. Refer to the repository for any applicable licensing terms.

---

### 🍽️ DineFlow — Bringing Restaurant Experiences Online

*Designed to connect modern restaurant experiences with scalable digital management.*
