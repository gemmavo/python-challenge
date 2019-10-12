#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv


# In[2]:


input_file = open("election_data.csv")
csv_read = csv.reader(input_file)
next(csv_read)


# In[3]:


total = 0
all_rows = []
cand = []


# In[4]:


for row in csv_read:
    total = 1 + total
    if row[2] not in cand:
        cand.append(row[2])
    all_rows.append(row)


# In[5]:


newDict = {i : 0 for i in cand} 


# In[6]:


for key in newDict.keys():
    for row in all_rows:
        if row[2] == key:
            newDict[key] += 1


# In[7]:


per_votes = []
for key in newDict.keys():
    p = newDict[key]
    per_votes.append(p/total)


# In[8]:


max_votes = 0
winner = ""
for key in newDict.keys():
    if newDict[key] > max_votes:
        max_votes = newDict[key]
        winner = key 


# In[9]:


print("Election Results")
print("-------------------------")
print("Total Votes: {}".format(total))
print("-------------------------")
print("Khan: {:.3f}% ({})".format(per_votes[0]*100, newDict["Khan"]))
print("Correy: {:.3f}% ({})".format(per_votes[1]*100, newDict["Correy"]))
print("Li: {:.3f}% ({})".format(per_votes[2]*100, newDict["Li"]))
print("O'Tooley: {:.3f}% ({})".format(per_votes[3]*100, newDict["O'Tooley"]))
print("-------------------------")
print("Winner: {}".format(winner))
print("-------------------------")


# In[10]:


with open("election_results2.txt", "w") as out_file:
    out_file.write("Election Results \n")
    out_file.write("------------------------- \n")
    out_file.write("Total Votes: {} \n".format(total))
    out_file.write("------------------------- \n")
    out_file.write("Khan: {:.3f}% ({}) \n".format(per_votes[0]*100, newDict["Khan"]))
    out_file.write("Correy: {:.3f}% ({}) \n".format(per_votes[1]*100, newDict["Correy"]))
    out_file.write("Li: {:.3f}% ({}) \n".format(per_votes[2]*100, newDict["Li"]))
    out_file.write("O'Tooley: {:.3f}% ({}) \n".format(per_votes[3]*100, newDict["O'Tooley"]))
    out_file.write("------------------------- \n")
    out_file.write("Winner: {} \n".format(winner))
    out_file.write("------------------------- \n")

