#!/usr/bin/env python
# coding: utf-8

# In[94]:


import csv
import os


# In[96]:


input_file = open("budget_data.csv")
csv_read = csv.reader(input_file)
next(csv_read)


# In[97]:


count = 0
total = 0


# In[98]:


newL = []


# In[99]:


for row in csv_read:
    if row[0] != 0:
         count = 1 + count
    n = int(row[1])
    total = n + total
    newL.append(row)


# In[100]:


greatest_inc = 0
inc_date = ""
greatest_dec = 0
dec_date = ""


# In[101]:


i = 0
change = 0
total_change = 0
while i < len(newL) - 1:
    change = int(newL[i+1][1]) - int(newL[i][1])
    total_change = change + total_change
    if change < greatest_dec:
         greatest_dec = change
         dec_date = newL[i+1][0]
    if change > greatest_inc:
         greatest_inc = change
         inc_date = newL[i+1][0]
    i = i + 1


# In[102]:


avg_change = total_change/count

print("Financial Analysis")
print("----------------------------")
print("Total Months: {}".format(count))
print("Total: ${}".format(total))
print("Average Change: ${:.2f}".format(avg_change))
print("Greatest Increase in Profits: {} (${})".format(inc_date, greatest_inc))
print("Greatest Decrease in Profits: {} (${})".format(dec_date, greatest_dec))


# In[103]:


with open("budget_data.txt", "w") as new_file:
    new_file.write("Financial Analysis \n")
    new_file.write("---------------------------- \n")
    new_file.write("Total Months: {} \n".format(count))
    new_file.write("Total: ${} \n".format(total))
    new_file.write("Average Change: ${:.2f} \n".format(avg_change))
    new_file.write("Greatest Increase in Profits: {} (${})\n".format(inc_date, greatest_inc))
    new_file.write("Greatest Decrease in Profits: {} (${}) \n".format(dec_date, greatest_dec))

