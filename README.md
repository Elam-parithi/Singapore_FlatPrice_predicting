# Singapore Resale Flat Prices Prediction

![pandas](https://img.shields.io/badge/pandas-2.2.3-blue)
![numpy](https://img.shields.io/badge/numpy-2.2.3-orange)
![matplotlib](https://img.shields.io/badge/matplotlib-3.10.1-green)
![seaborn](https://img.shields.io/badge/seaborn-0.13.2-red)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.6.1-yellow)
![Streamlit](https://img.shields.io/badge/Streamlit-1.15.2-purple)



This project aims to extract and analyze resale price data of flats in Singapore from the 
Housing and Development Board (HDB) and build a prediction model for flat prices. 
Additionally, a user-friendly interface is created using **Streamlit** for an interactive experience.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [License](#license)

---

## Project Overview

Singapore's public housing market (HDB) plays a vital role in the lives of its residents. 
This project focuses on analyzing trends in HDB resale flat pricing and building a machine 
learning model to predict flat prices based on historical data. An interactive **Streamlit** 
application is built as a visualization and prediction tool for users to understand and interact with the outcome.

---

## Project Structure

```plaintext
|-- data/               # Folder for dataset storage
|-- models/             # Saved trained model artifacts
|-- scripts/            # Python scripts for extraction, analysis, and model generation
|-- app.py              # Streamlit application script
|-- requirements.txt    # List of Python dependencies
|-- README.md           # Project documentation
```

---

## Features

- Extraction of open-source HDB resale flat pricing data for analysis.
- Exploration of key trends and correlations within the dataset.
- Development of a machine learning model to predict flat prices.
- Deployment of a **Streamlit-based** user interface for:
    - Data visualization
    - Flat price prediction
    - Easy interaction with prediction results and analysis.

---

## Technologies Used

The project leverages the following tools and technologies:

- **Python**: For data extraction, manipulation, and modeling.
- **Libraries and Frameworks**:
    - **pandas**, **numpy**, **matplotlib**, **seaborn**: For data analysis and visualization.
    - **scikit-learn**,: For building and evaluating the machine learning model.
    - **Streamlit**: To build the interactive user interface.
- **Singapore HDB Open Data**: As the data source for HDB resale flat prices.

---

## Setup Instructions

To run this project locally:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Elam-parithi/Resale_Flat_Price_Prediction.git
   cd Singapore-Resale-Flat-Prices-Predicting
   ```

2. **Set Up a Virtual Environment** (Optional but recommended)
   ```bash
   python -m venv env
   source env/bin/activate 
   # On Windows use 
   # `env\Scripts\activate`
   ```

3. **Install Dependencies**
   Install required Python packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   Start the Streamlit interface by:
   ```bash
   streamlit run app.py
   ```

---

## Usage

### Data Analysis
- Resale flat data is explored and visualized to identify patterns, 
    trends, and outliers.

### Prediction
- Select input variables (location, size, etc.) in the 
    Streamlit interface to predict the HDB resale flat price using the 
    trained machine learning model.


---

## License

This project is licensed under the MIT License. 
See the LICENSE file for details.

---

## Developer

   This application was developed by [Elamparithi](https://www.linkedin.com/in/elamparithi-t/)
    
<a href="https://www.linkedin.com/in/elamparithi-t/"><img src="Documentation/Icons/LI-Logo.png" alt="linkedin.com" width="120" height="38"></a>