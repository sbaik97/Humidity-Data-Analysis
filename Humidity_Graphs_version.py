#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Imports

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

import pandas as pd

import numpy as np

data_to_load = "Resources/humidity_data.csv"

# Creating data frame from csv file
humidity_data_df = pd.read_csv(data_to_load)
humidity_data_df


# In[4]:


# Graphs for RH% vs. Time 

data_to_load = "Resources/humidity_data.csv"

humidity_data_df = pd.read_csv(data_to_load)
humidity_data_df

humidity_data_df.plot(x = "Elapsed time (s)", y = "RH%")
plt.ylabel("Relative Humidity (%)")
plt.title("RH% change over time")

plt.savefig("Graphs/RH%_change_over_time.png")
plt.show


# In[3]:


# Statistics for relative humidity data for 10,000-80,000 seconds
Elapsed_time_1 = humidity_data_df["Elapsed time (s)"]
Elapsed_time_average_1 = Elapsed_time_1[(Elapsed_time_1 >= 10000) & (Elapsed_time_1 <= 80000)]
new_frame_1 = humidity_data_df.loc[(humidity_data_df["Elapsed time (s)"]>=10000) & (humidity_data_df["Elapsed time (s)"]<=80000)]
RH_average_1 = new_frame_1["RH%"]
RH_average_1.mean()
RH_average_1.describe()


# In[5]:


# Statistics for relative humidity data for 120,000-150,000 seconds
Elapsed_time_2 = humidity_data_df["Elapsed time (s)"]
Elapsed_time_average_2 = Elapsed_time_1[(Elapsed_time_1 >= 120000) & (Elapsed_time_1 <= 150000)]
new_frame_2 = humidity_data_df.loc[(humidity_data_df["Elapsed time (s)"]>=12000) & (humidity_data_df["Elapsed time (s)"]<=150000)]
RH_average_2 = new_frame_2["RH%"]
RH_average_2.mean()
RH_average_2.describe()


# In[5]:


# Graph of RH sensor temperature vs. Time
humidity_data_df.plot(x = "Elapsed time (s)", y = "RH sensor temperature (C)", color = "green")
plt.ylabel("Temperature (C)")
plt.title("RH sensor temperature (C) change over time")
plt.savefig("Graphs/RH_Sensor_Temperature(c)_change_over_time.png")
plt.show


# In[6]:


# Graph for Dew Point vs. Time
RH_percent = np.array(humidity_data_df["RH%"].tolist())
ambient_temp = np.array(humidity_data_df["RH sensor temperature (C)"].tolist())
time = np.array(humidity_data_df["Elapsed time (s)"].tolist())
dewpoint_temp = np.array((243.04 * np.log(RH_percent)+ 17.625 * ambient_temp/(243.04+ambient_temp)) / (17.625 - (np.log(RH_percent)-17.625*ambient_temp/(243.04+ ambient_temp))))
plt.plot(time, dewpoint_temp, label = "Dewpoint Temperature", color = "maroon")
plt.title("Dewpoint temperature (c) change overtime")
plt.xlabel("Elapsed Time (s)")
plt.ylabel("Temperature (c)")
plt.legend()
plt.savefig("Graphs/Dewpoint_temperature_(c)_change_overtime.png")
plt.show()

# series->list(no calculations)->array


# In[84]:


# Statistics of dewpoint temp data from 10,000 to 80,000 seconds
RH_percent_dewpoint = humidity_data_df["RH%"]
ambient_temp_dewpoint = humidity_data_df["RH sensor temperature (C)"]
time = humidity_data_df["Elapsed time (s)"]

dew_point_temp = ((243.04 * np.log(RH_percent_dewpoint)+ 17.625 * ambient_temp_dewpoint/(243.04+ambient_temp_dewpoint)) / (17.625 - (np.log(RH_percent_dewpoint)-17.625*ambient_temp_dewpoint/(243.04+ ambient_temp_dewpoint)))).tolist()
humidity_data_df["dew_point_temp"] = dew_point_temp
new_frames_1 = humidity_data_df.loc[(humidity_data_df["Elapsed time (s)"]>=10000) & (humidity_data_df["Elapsed time (s)"]<=80000)]
dew_point_average1 = new_frames_1["dew_point_temp"]
dew_point_average1.mean()
dew_point_average1.describe()


# In[83]:


# Statistics for dewpoint temp data for 120,000-150,000 seconds

new_frames_2 = humidity_data_df.loc[(humidity_data_df["Elapsed time (s)"]>=120000) & (humidity_data_df["Elapsed time (s)"]<=150000)]
dew_point_average2 = new_frames_2["dew_point_temp"]
dew_point_average2.mean()
dew_point_average2.describe()


# In[22]:


# Graph for Saturated Water Vapor vs. Time
RH_percent = np.array(humidity_data_df["RH%"].tolist())
T = np.array(humidity_data_df["RH sensor temperature (C)"].tolist())
time = np.array(humidity_data_df["Elapsed time (s)"].tolist())
Tc = 647.096
k = np.array(1-(T/Tc))
a1 = -7.85951783
a2 = 1.84408259
a3 = -11.7866497
a4 =  22.6807411
a5 = -15.9618719
a6 = 1.80122502
e = 2.718
Pc = 22.064
saturated_water_pressure = np.array(Pc * (e**((Tc/(T+273))*(a1*k+a2*(k**1.5)+a3*(k**3)+a4*(k**3.5)+a5*(k**4)+a6*(k**7.5)))))
plt.plot(time, saturated_water_pressure, label = "Saturated Water Pressure", color = "magenta")
plt.title("Saturated water pressure change overtime")
plt.xlabel("Elapsed Time (s)")
plt.legend()
plt.savefig("Graphs/Saturated_Water_Pressure_change_overtime.png")
plt.show()


# In[23]:


# Graph for Water Vapor Pressure vs. Time
RH_percent = np.array(humidity_data_df["RH%"].tolist())
T = np.array(humidity_data_df["RH sensor temperature (C)"].tolist())
time = np.array(humidity_data_df["Elapsed time (s)"].tolist())
water_vapor_pressure = np.array(RH_percent * (saturated_water_pressure/100))
plt.plot(time, water_vapor_pressure, label = "Water Vapor Pressure", color = "yellowgreen")
plt.title("Water vapor pressure change overtime")
plt.xlabel("Elapsed Time (s)")
plt.legend()
plt.savefig("Graphs/Water_Vapor_Pressure_change_overtime.png")
plt.show()


# In[24]:


# Graph for Absolute Humidity vs. Time
RH_percent = np.array(humidity_data_df["RH%"].tolist())
T = np.array(humidity_data_df["RH sensor temperature (C)"].tolist())
time = np.array(humidity_data_df["Elapsed time (s)"].tolist())
absolute_humidity = np.array(water_vapor_pressure/(461.5*(T+273)))
plt.plot(time, absolute_humidity, label = "Absolute Humidity", color = "orange")
plt.title("Absolute Humidity change overtime")
plt.xlabel("Elapsed Time (s)")
plt.legend()
plt.savefig("Graphs/Absolute_Humidity_Change_Overtime.png")
plt.show()

