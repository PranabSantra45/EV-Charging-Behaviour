# EV Charging Behavior Analysis & Prediction System

This repository contains the complete development of an EV charging data analysis
and prediction system. The project evolves from data exploration to building a
machine learning model and deploying it as a web-based application.

---

## Current Status
🚧 Actively developed and functional  

The project has progressed from analysis to a working prediction system with
a trained model, backend API, and frontend interface.

---

## What has been done

### 📊 Data Analysis & Preprocessing
- Data cleaning and handling missing/inconsistent values  
- Feature engineering (date, time, and behavioral features)  
- Hour-wise and weekday-wise charging analysis  
- Visualization using Python and Power BI  

### Machine Learning Model
- Built regression model to predict energy consumption (kWh)  
- Implemented pipeline using:
  - ColumnTransformer  
  - OneHotEncoder  
  - RandomForestRegressor  
- Included domain-based feature engineering:
  - State of Charge (SOC)  
  - Battery capacity  
  - Charging rate  
  - Temperature conditions  
- Created a derived feature (`energy_expected`) based on charging physics  

### Web Application
- Developed a frontend interface for user input  
- Built Flask backend API for real-time prediction  
- Integrated model with API to return predictions dynamically  

---

## Key Features

- ⚡ Predict EV energy consumption (kWh)
- 📅 Considers time-based patterns (hour, day)
- 🔋 Uses battery and charging parameters
- 🌍 Includes environmental and contextual factors
- 🔁 End-to-end system: Data → Model → API → UI

---

## Project Structure 

```
EV_CS/
│
├── Datasets/                # Preprocessed datasets  
├── Visualisation/           # Power BI dashboards  
│
├── main.ipynb               # Data analysis & experiments  
├── app.py                   # Flask backend API
├── data_clean.py
│
├── index.html               # Frontend UI  
├── script.js                # Frontend logic  
│
├── energy_model_v2.pkl      # Trained ML model  (USED)
├── model_energy.pkl         # Previous model versions  
├── model_peak.pkl           # Peak prediction model (experimental)  
```

--- 

## Tools & Technologies

- Python (Pandas, NumPy, Scikit-learn)
- Machine Learning (Random Forest, Pipelines)
- Flask (Backend API)
- HTML, CSS, JavaScript (Frontend)
- Power BI (Visualization)
- Jupyter Notebook

---

## Future Scope

- Improve model accuracy using advanced feature engineering  
- Add peak-hour prediction (classification model)  
- Build an interactive dashboard with charts and analytics  
- Store predictions for historical analysis  
- Deploy the system for real-time usage

---

## Notes

This project reflects a step-by-step development approach from data analysis
to a full-stack machine learning application. The repository includes experiments,
intermediate models, and evolving implementations as part of the learning process.

---

## Author

**Pranab Santra**  

- 2nd Year CSE Student  
- Interested in AI/ML, Quantum Computing, and Data-driven Systems  
- Passionate about building real-world applications from research concepts  

---

## Acknowledgment

This project was developed as part of an ongoing exploration into EV systems,
data analysis, and machine learning applications. It reflects a hands-on approach
to understanding real-world problems and building practical solutions.

---

## License

This project is intended for educational and research purposes.  
You are free to explore, learn from, and build upon this work.
