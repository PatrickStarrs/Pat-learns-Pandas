#311 service requests for NYC

import pandas as pd
import matplotlib.pyplot as plt

complaints = pd.read_csv('311-service-requests.csv')

#summarizes the data in the dataframe
complaints

#selects the column Complaint Type
complaints['Complaint Type']

#shows the top 5 rows
complaints[:5]

#shows multiple columns, in this case Complaint Type and the Borough of the complaints
complaints[['Complaint Type', 'Borough']]

# shows the above, but just the first 10 rows
complaints[['Complaint Type', 'Borough']][:10]


#uses the value_count function to count the number of each Complaint Type
complaints['Complaint Type'].value_counts()

#sets a new variable as the count of the complaints type, and then shows the 10 most common complaints
complaint_counts = complaints['Complaint Type'].value_counts()
complaint_counts[:10]

#uses matplotlib.pyplot to plot the data 
complaint_counts[:10].plot(kind='bar')