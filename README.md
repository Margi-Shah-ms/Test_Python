# 🏋️‍♂️ Personal Fitness Tracker & Analytics Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)

A comprehensive Python-based **Personal Fitness Tracker** that allows users to log their daily physical activities, calculate key health metrics, filter workout records, and analyze fitness trends using interactive charts. It supports both a command-line interface (CLI) and an interactive **Streamlit Web Application**.

---

## 📹 Video Demo & Walkthrough

🎥 **Watch the project explanation video here:**  
[Google Drive Video Link](https://drive.google.com/file/d/167kdc98No4gaxV-qlmISPX6nh4fRhLd0/view?usp=sharing)

---

## 📌 Project Overview & Features

This project demonstrates the practical application of Object-Oriented Programming (OOP), Data Analytics, and Web UI development in Python.

### 🌟 Key Features
- **➕ Log Daily Activities:** Easily record workout types (e.g., Running, Gym, Cycling), duration in minutes, calories burned, and date.
- **💾 CSV Data Persistence:** Automatically reads and writes all workout data to `fitness_activities.csv`.
- **🔥 Automated Metric Calculation:**
  - Total Calories Burned
  - Average Workout Duration
  - Calorie Burn Rate per Minute (`Calories / Duration`)
- **🔍 Smart Filtering:** Filter fitness records dynamically based on activity type.
- **📊 Interactive Visualizations & Analytics:**
  - **Bar Chart:** Time spent per activity type.
  - **Line Chart:** Calorie burn trends over time.
  - **Pie Chart:** Overall distribution of workout types.
  - **Heatmap:** Correlation analysis between duration and calories.
- **🛑 Robust Input Validation:** Validates duration and calories to prevent negative or zero inputs.
- **🌐 Dual Interface:** Interactive CLI menu and a modern Streamlit Web Dashboard.

---

## 🛠️ Technologies Used

| Technology | Purpose |
| :--- | :--- |
| **Python** | Core Programming Language |
| **Streamlit** | Interactive Web Dashboard Framework |
| **Pandas** | Data Handling, CSV I/O, & Manipulation |
| **NumPy** | Numerical Calculations & Array Operations |
| **Matplotlib** | Static & Line Plotting |
| **Seaborn** | Advanced Statistical Data Visualization & Heatmaps |

---

## OUTPUT: 
<img width="992" height="700" alt="Figure_1" src="https://github.com/user-attachments/assets/a1ac60bf-c630-494a-86dc-731a4226ab81" />


## 📂 Repository Structure

```text
Test_Python/
├── app.py                   # Streamlit Web Application
├── fitness_tracker.py       # Object-Oriented CLI Application
├── fitness_activities.csv   # Workout Dataset
├── requirements.txt         # Project Dependencies
├── Figure_1.png             # Visualization Output Screenshot
└── README.md                # Project Documentation
