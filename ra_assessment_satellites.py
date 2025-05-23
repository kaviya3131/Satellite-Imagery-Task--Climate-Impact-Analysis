# -*- coding: utf-8 -*-
"""RA_Assessment_Satellites.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1d68YumslZk5P3uR986IsB6ONnVfCvmvy

# Assessing Climate Impacts in Saarland in the Past Decade
Local climate impacts can be analyzed using satellite imagery. For this task, you will identify climate impact patterns in Saarland using Google Earth Engine. The analysis should focus on comparing two points in time and deriving insights about climate impact patterns during that time.

### Import necessary libraries
"""

import ee
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import geemap
import seaborn as sns
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

"""### Main script workflow(Takes few minutes to give the result)"""

# Initialize Earth Engine
ee.Authenticate()
ee.Initialize(project='psychic-ruler-363215')


# Define the Area of Interest (AOI) - Saarland, Germany
aoi = ee.Geometry.Polygon([
    [[6.35, 49.1], [7.35, 49.1], [7.35, 49.7], [6.35, 49.7], [6.35, 49.1]]
])

# Function to mask clouds using QA60 band
def mask_clouds(image):
    qa = image.select('QA60')
    cloud_mask = qa.bitwiseAnd(1 << 10).eq(0)
    return image.updateMask(cloud_mask)

# Function to compute NDVI and add it as a band
def add_ndvi(image):
    ndvi = image.normalizedDifference(['B8', 'B4']).rename('NDVI')
    return image.addBands(ndvi)

# Function to prepare Sentinel-2 image collection
def get_sentinel_images(start_date, end_date, dataset="COPERNICUS/S2"):
    collection = (ee.ImageCollection(dataset)
                  .filterBounds(aoi)
                  .filterDate(start_date, end_date)
                  .filterMetadata('CLOUDY_PIXEL_PERCENTAGE', 'less_than', 10)
                  .map(mask_clouds)
                  .map(add_ndvi))
    return collection.median().clip(aoi)

# Load Sentinel-2 images for two time points
image_2016 = get_sentinel_images('2016-06-01', '2016-08-31')
image_2023 = get_sentinel_images('2023-06-01', '2023-08-31')

# Extract NDVI bands
ndvi_2016 = image_2016.select('NDVI')
ndvi_2023 = image_2023.select('NDVI')

# Compute NDVI change (difference: 2023 - 2016)
ndvi_change = ndvi_2023.subtract(ndvi_2016)

# Convert to NumPy for visualization and interactive dashboard
ndvi_array_2016 = geemap.ee_to_numpy(ndvi_2016, region=aoi)
ndvi_array_2023 = geemap.ee_to_numpy(ndvi_2023, region=aoi)
ndvi_change_array = geemap.ee_to_numpy(ndvi_change, region=aoi)

# Compute Change Detection Metrics
loss_area = np.sum(ndvi_change_array < -0.1) / ndvi_change_array.size * 100
gain_area = np.sum(ndvi_change_array > 0.1) / ndvi_change_array.size * 100
stable_area = 100 - (loss_area + gain_area)

# Streamlit Web App
st.title("Saarland Vegetation Change Analysis")

# NDVI Change Visualization
st.subheader("NDVI Change Map")
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(ndvi_array_2016, cmap='RdYlGn', vmin=-1, vmax=1)
axes[0].set_title("NDVI 2016")
axes[1].imshow(ndvi_array_2023, cmap='RdYlGn', vmin=-1, vmax=1)
axes[1].set_title("NDVI 2023")
axes[2].imshow(ndvi_change_array, cmap='bwr', vmin=-0.5, vmax=0.5)
axes[2].set_title("NDVI Change (2023 - 2016)")
st.pyplot(fig)

# Interactive Time Series Visualization
years = list(range(2016, 2024))
ndvi_means = [np.nanmean(ndvi_array_2016) if y == 2016 else np.nanmean(ndvi_array_2023) for y in years]
ndvi_df = {'Year': years, 'Mean_NDVI': ndvi_means}
fig = px.line(ndvi_df, x='Year', y='Mean_NDVI', title='Mean NDVI Over Time')
st.plotly_chart(fig)

# Interactive Histogram of NDVI Changes
st.subheader("Distribution of NDVI Changes")
fig_hist = px.histogram(ndvi_change_array.flatten(), nbins=50, title="NDVI Change Distribution", labels={'value': "NDVI Change"})
st.plotly_chart(fig_hist)

# Box Plot for NDVI Comparison
st.subheader("NDVI Comparison - 2016 vs 2023")
fig_box = go.Figure()
fig_box.add_trace(go.Box(y=ndvi_array_2016.flatten(), name='NDVI 2016', marker_color='green'))
fig_box.add_trace(go.Box(y=ndvi_array_2023.flatten(), name='NDVI 2023', marker_color='blue'))
fig_box.update_layout(title="NDVI Box Plot Comparison")
st.plotly_chart(fig_box)

# Display Change Statistics
st.subheader("Change Detection Metrics")
st.write(f"**Mean NDVI 2016:** {np.nanmean(ndvi_array_2016):.3f}")
st.write(f"**Mean NDVI 2023:** {np.nanmean(ndvi_array_2023):.3f}")
st.write(f"**NDVI Change:** {(np.nanmean(ndvi_array_2023) - np.nanmean(ndvi_array_2016)) / np.nanmean(ndvi_array_2016) * 100:.2f}%")
st.write(f"**Vegetation Loss Area:** {loss_area:.2f}%")
st.write(f"**Vegetation Gain Area:** {gain_area:.2f}%")
st.write(f"**Stable Vegetation Area:** {stable_area:.2f}%")

st.write("Developed by Kaviya Ravichandran")