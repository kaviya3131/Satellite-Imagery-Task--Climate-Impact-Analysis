Instructions for Running the Colab Notebook & Streamlit NDVI Analysis App
- Running the Colab Notebook
Google Earth Engine (GEE) Authentication

Before running the notebook, authenticate your Google Earth Engine (GEE) account:
ee.Authenticate()
ee.Initialize()
	•	Use the following credentials to log in and run the Colab file:
	◦	Email ID: t9561568@gmail.com
	◦	Password: test9876
	•	After running the notebook in Colab, you will see a prompt: “Allow this notebook to access your Google credentials?” → Click Allow to proceed.
- Running the Streamlit NDVI Analysis App
1. Requirements
Before running the application, ensure the following dependencies are installed:
Dependencies:
	•	Python 3.9+
	•	Streamlit
	•	Google Earth Engine (GEE)
	•	GeoPandas
	•	Geemap
	•	NumPy
	•	Matplotlib
	•	Seaborn
	•	Plotly

Install Dependencies:
Run the following commands to install the required Python libraries:
!pip install geemap geopandas matplotlib numpy seaborn streamlit plotly

2. Running the Application Locally
To launch the Streamlit web app, navigate to the directory containing the script and run:
streamlit run project.py

This will start a local server, and you will see an output like:
You can now view your Streamlit app in your browser.
Local URL: http://localhost:8501

Open the Local URL (http://localhost:8501) in your browser to access the interactive NDVI dashboard.

Key Features of the App
NDVI Change Detection Maps → Visualize NDVI trends between 2016 and 2023. Histogram of NDVI Changes → Interactive distribution of vegetation changes. Time-Series Analysis → Line chart of mean NDVI trends. Box Plot Comparison → NDVI differences between both years. Dynamic Interactive Dashboard → Developed using Streamlit & Plotly for an enhanced user experience.
