#  Hospital Coverage Analysis System

##  Overview

This project analyzes hospital accessibility across different areas using population and geographic data. It identifies regions with low healthcare coverage and highlights critical zones using an interactive map-based visualization.

---

## 🚀 Features

*  Relational database design with multiple tables
*  Multi-table JOIN queries for data analysis
*  Interactive map visualization using Leaflet.js
*  Critical zone detection based on population and hospital availability

---

##  Tech Stack

* Backend: Flask (Python)
* Database: SQLite
* Frontend: HTML, JavaScript
* Map Library: Leaflet.js
* Deployment: Render (Backend), Vercel (Frontend)
* Version Control: Git & GitHub

---

## 🗂️ Database Schema

The system uses the following tables:

* Areas
* Hospitals
* Roads
* Area-Hospital Mapping
* Coverage

---
## 📁 Project Structure

```
hospital-coverage-app/
│
├── backend/
│   ├── app.py            # Flask backend with API routes
│   ├── db.py             # Database connection (SQLite)
│   ├── database.db       # SQLite database file
│   └── requirements.txt  # Backend dependencies
│
├── frontend/
│   └── index.html        # Frontend UI with Leaflet map
│
└── README.md             # Project documentation
```

## ⚙️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/yamini749/Hospital-Coverage-App.git
cd Hospital-Coverage-App
```

### 2. Run backend

```bash
cd backend
python app.py
```

### 3. Open frontend

Open the file in your browser:

```
frontend/index.html
```
### Database

This project uses SQLite.

The database file database.db is already included
It contains all tables and sample data 

---

## 🌐 Live Demo

* Backend API: https://hospital-coverage-app.onrender.com/coverage
* Frontend: https://hospital-coverage-app.vercel.app/

---

## 🧠 Logic Used

* Coverage is determined using:

  * Distance to nearest hospital
  * Number of hospitals nearby
  * Population of the area

* Critical zones are identified where:

  * Population is high
  * Hospital availability is low

---

## 📸 Output

* Interactive map with color-coded regions:

  * 🟢 High coverage
  * 🟡 Medium coverage
  * 🔴 Low coverage
  * 🟣 Critical zones

---

## ⚠️ Challenges Faced

* Python environment issues and interpreter mismatches
* Migration from MySQL to SQLite for deployment compatibility
* SQLite empty database issue due to incorrect file paths
* Frontend data rendering issues due to API mismatch
* Deployment challenges (Flask not supported directly on Vercel)

---

## 💡 Future Improvements

* Integration with real-world datasets
* Cloud-based database (AWS / PlanetScale)
* Advanced filtering and search features
* Improved UI/UX and mobile responsiveness

---

## 👩‍💻 Author

Yamini
