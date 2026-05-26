# Healthcare Patient Risk Prioritization System
Overview:

The Healthcare Patient Risk Prioritization System is a Python-based data analysis tool designed to assist healthcare providers in identifying critical patients and prioritizing medical attention based on vital signs, lab results, and admission severity.

This system automates the process of:

Detecting abnormal clinical test values

Assigning priority scores to patients

Ranking patients based on medical urgency

Generating summaries for healthcare staff

This project demonstrates real-world healthcare analytics using data processing and risk scoring algorithms.

# Features
1. Critical Test Value Detection

The system flags abnormal values for key clinical indicators:

Potassium

Glucose

Heart Rate

Lactate

Each value is compared against medically defined normal ranges.

2. Patient Priority Scoring

Each patient receives a Priority Score based on:

Admission type (Emergency, Urgent, Elective)

Presence of Sepsis

Abnormal vital signs

Abnormal lab test results

Higher scores indicate higher urgency.

3. Patient Ranking System

Patients are automatically sorted from highest to lowest priority, allowing healthcare providers to focus on the most critical cases first.

4. Automated Summary Generation

The system generates easy-to-read summaries of critical findings to support faster clinical decision-making.

# Technologies Used

Python 3

Pandas

Excel Data Processing

Data Analysis

Risk Scoring Algorithms

# Project Structure
Healthcare-Priority-System/
│
├── dummy_updated_with_values.xlsx
├── healthcare_priority_system.py
├── README.md
└── requirements.txt
# How It Works

Step 1: Load patient dataset from Excel

Step 2: Analyze vital signs and lab results

Step 3: Flag abnormal test values

Step 4: Calculate priority score using risk factors

Step 5: Sort patients by urgency

Step 6: Generate summary report

# Priority Score Logic
Condition	Score
Emergency Admission	+30
Urgent Admission	+20
Elective Admission	+10
Sepsis Present	+15
Abnormal Heart Rate	+5
Abnormal Glucose	+5
Abnormal Potassium	+5
High Lactate	+5

# Applications

This system can be used in:

Hospitals

Emergency departments

ICU triage systems

Clinical decision support systems

Healthcare analytics platforms

# Future Improvements

Integration with live hospital databases

Real-time monitoring system

Machine Learning-based risk prediction

Dashboard visualization

Integration with Electronic Health Records (EHR)
