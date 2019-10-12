#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import csv


# In[5]:


us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


# In[6]:


input_file = open("employee_data.csv")
csv_input = csv.reader(input_file)
next(csv_input)
with open("employee_data2.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB","SSN", "State"])
    for row in csv_input:
        emp_id = row[0]
        first_name = row[1].split()[0]
        last_name = row[1].split()[1]
        DOB = row[2].split("-")
        new_DOB = DOB[1] + "/" + DOB[2] + "/" + DOB[0]
        SSN = "***-**-" + row[3].split("-")[2]
        state = us_state_abbrev[row[4]]
        writer.writerow([emp_id, first_name, last_name, new_DOB, SSN, state])
        

