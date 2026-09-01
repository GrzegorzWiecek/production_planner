# 🏭 Production Planning & Execution System

A web application for planning, managing and monitoring production orders.

This project started as a **quick proof-of-concept built with Streamlit** to validate the main business workflow and database structure.

After validating the concept, the project is being redesigned using **Django** as the backend and web application framework, with a focus on multi-user operation, scalability, authentication and a production-ready architecture.

---

## 🎯 Project Goal

The application is designed to support two main groups of users:

### Production Planners

Planners can:

* create production orders
* assign orders to a workplace and workstation
* define planned production dates
* monitor order status
* track production progress

### Production Workers

Workers can:

* filter orders assigned to their workstation
* start a production order
* record the actual start time
* add comments or explanations
* complete production orders
* record the completion time
* track the actual execution time

---

## 🔄 Production Workflow

```text
Production Planner
        │
        ▼
Create Production Order
        │
        ▼
Assign Workplace & Workstation
        │
        ▼
      PLANNED
        │
        │ START
        ▼
   IN PROGRESS
        │
        ├── Completion Note
        │
        │ COMPLETE
        ▼
     COMPLETED
        │
        ▼
Execution Time
```

---

## 🧪 Proof of Concept

The initial version was developed with **Streamlit** as a rapid prototype.

The purpose of this stage was to validate:

* database structure
* production order workflow
* workplace and workstation relationships
* production start/complete logic
* execution time calculation
* basic filtering

The Streamlit version served as a **functional prototype rather than the final architecture**.

---

## 🚀 Current Development

The project is being migrated to **Django** to provide a more suitable foundation for a multi-user production application.

The Django version will introduce:

* multi-user support
* user authentication
* role-based access
* planner and worker views
* database-backed business logic
* production order management
* workstation-specific order queues
* scalable web application architecture
* PostgreSQL support

The goal is to move from a quick prototype to a more realistic production-oriented application.

---

## 🗄️ Database

The application is designed to work with relational databases.

### Development

SQLite is currently used for local development because it requires no separate database server.

### Target Environment

PostgreSQL is planned as the target database for the multi-user Django application.

The database model includes concepts such as:

```text
Users
   │
   ├── Planner
   └── Worker

Workplaces
   │
   └── Workstations
           │
           └── Production Orders
```

---

## 🛠️ Technology Stack

### Prototype

* Python
* Streamlit
* SQLAlchemy
* SQLite
* Alembic

### Target Architecture

* Python
* Django
* Django ORM
* PostgreSQL
* HTML / CSS
* JavaScript

---

## 📌 Project Status

**Prototype completed.**

The initial Streamlit implementation successfully validates the core production workflow.

**Django redevelopment in progress.**

The next stage focuses on transforming the prototype into a multi-user web application with a production-oriented architecture.

---

## 💼 Portfolio Purpose

This project demonstrates practical application of:

* Python development
* relational database design
* ORM
* database migrations
* CRUD operations
* business process modelling
* production workflow design
* web application architecture
* transition from rapid prototyping to production-oriented development

The project is intentionally developed in stages to demonstrate how a business idea can evolve from a quick proof-of-concept into a structured multi-user application.

---

## 📄 License

This project is intended primarily as a portfolio and learning project.
