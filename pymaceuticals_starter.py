
# coding: utf-8

# In[1]:


# Dependencies and Setup
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Hide warning messages in notebook
import warnings
warnings.filterwarnings('ignore')

# File to Load (Remember to Change These)
mouse_drug_data_to_load = "data/mouse_drug_data.csv"
clinical_trial_data_to_load = "data/clinicaltrial_data.csv"

# Read the Mouse and Drug Data and the Clinical Trial Data
mouse = pd.read_csv(mouse_drug_data_to_load)
clinical = pd.read_csv(clinical_trial_data_to_load)

# Combine the data into a single dataset
data  = pd.merge(mouse,clinical)

# Display the data table for preview
data.head()


# ## Tumor Response to Treatment

# In[2]:


# Store the Mean Tumor Volume Data Grouped by Drug and Timepoint 
tumor_mean = data.groupby(['Drug','Timepoint'])['Tumor Volume (mm3)'].mean()
# Convert to DataFrame
tumor = pd.DataFrame(tumor_mean)
# Preview DataFrame
tumor.head()


# In[3]:


# Store the Standard Error of Tumor Volumes Grouped by Drug and Timepoint# Store 
tumor_sem = data.groupby(['Drug','Timepoint'])['Tumor Volume (mm3)'].sem()
# Convert to DataFrame
tumor_sem = pd.DataFrame(tumor_sem)
# Preview DataFrame
tumor_sem.head()


# In[4]:


# Minor Data Munging to Re-Format the Data Frames
reformat_tumor_mean= tumor_mean.unstack(level=0)
# Preview threformat_tumor_mean['Capomulin']at Reformatting worked
reformat_tumor_mean.head()


# In[5]:


# Generate the Plot (with Error Bars)
x_axis=reformat_tumor_mean.index.values 


plt.errorbar(x_axis,reformat_tumor_mean['Capomulin'],reformat_tumor_sem['Tumor Volume (mm3)']['Capomulin'],color='r',marker='o',linewidth=0.5)
plt.errorbar(x_axis,reformat_tumor_mean['Infubinol'],reformat_tumor_sem['Tumor Volume (mm3)']['Infubinol'],color='b',marker='^',linewidth=0.5)
plt.errorbar(x_axis,reformat_tumor_mean['Ketapril'],reformat_tumor_sem['Tumor Volume (mm3)']['Ketapril'],color='g',marker='s',linewidth=0.5)
plt.errorbar(x_axis,reformat_tumor_mean['Placebo'],reformat_tumor_sem['Tumor Volume (mm3)']['Placebo'],color='k',marker='p',linewidth=0.5)

plt.xlim(min(x_axis)-5, max(x_axis)+5)
plt.xlabel('Time (Days)')
plt.ylabel("Tumor Volume (mm3)")
plt.title('Tumor Response to Treatment')
plt.legend(['Capomulin','Infubinol','Ketapril','Placebo'],loc='upperleft')
plt.grid()

# Save the Figure
plt.savefig("Tumor Response to Treatment.png")
plt.show()


# In[ ]:


# Show the Figure
plt.show()


# ## Metastatic Response to Treatment

# In[ ]:


# Store the Mean Met. Site Data Grouped by Drug and Timepoint 
meta_mean = data.groupby(['Drug','Timepoint'])['Metastatic Sites'].mean()

# Convert to DataFrame
meta_mean= pd.DataFrame(meta_mean)

# Preview DataFrame
meta_mean.head()


# In[ ]:


# Store the Standard Error associated with Met. Sites Grouped by Drug and Timepoint # Store  
meta_sem =data.groupby(['Drug','Timepoint'])['Metastatic Sites'].sem()

# Convert to DataFrame
meta_sem = pd.DataFrame(meta_sem)

# Preview DataFrame
meta_sem.head()


# In[ ]:


# Minor Data Munging to Re-Format the Data Frames
minor_meta_mean = meta_mean.unstack(level=0)

# Preview that Reformatting worked
minor_meta_mean.head()


# In[ ]:


# Generate the Plot (with Error Bars)

# Save the Figure

# Show the Figure


# In[ ]:



# Generate the Plot (with Error Bars)# Genera 
x_axis=minor_meta_mean.index.values 

plt.errorbar(x_axis,minor_meta_mean['Metastatic Sites']['Capomulin'],minor_meta_sem['Metastatic Sites']['Capomulin'],color='r',marker='o',linewidth=0.5)
plt.errorbar(x_axis,minor_meta_mean['Metastatic Sites']['Infubinol'],minor_meta_sem['Metastatic Sites']['Infubinol'],color='b',marker='^',linewidth=0.5)
plt.errorbar(x_axis,minor_meta_mean['Metastatic Sites']['Ketapril'],minor_meta_sem['Metastatic Sites']['Ketapril'],color='g',marker='s',linewidth=0.5)
plt.errorbar(x_axis,minor_meta_mean['Metastatic Sites']['Placebo'],minor_meta_sem['Metastatic Sites']['Placebo'],color='k',marker='p',linewidth=0.5)


plt.xlim(min(x_axis)-5, max(x_axis)+5)
plt.xlabel('Treatment Duration (Days)')
plt.ylabel("Met. Sites")
plt.title('Metastatic Spread During Treatment')
plt.legend(['Capomulin','Infubinol','Ketapril','Placebo'],loc='upperleft')
plt.grid()

# Save the Figure
plt.savefig("Metastatic Spread During Treatment.png")

#Show the figure
plt.show()


# ## Survival Rates

# In[7]:


# Store the Count of Mice Grouped by Drug and Timepoint (W can pass any metric)
mice_count = data.groupby(['Drug','Timepoint'])['Mouse ID'].count()

# Convert to DataFrame
mice_count = pd.DataFrame(mice_count)
mice_count.rename(columns={'Mouse ID': 'Mouse Count'}, inplace=True)
mice_sum = mice_count.sum()

# Preview DataFrame
mice_count.head()


# In[8]:


# Minor Data Munging to Re-Format the Data Frames
minor_mice_count = mice_count.unstack(level=0)

# Preview the Data Frame
minor_mice_count.head()


# In[11]:





# In[12]:


# Generate the Plot (Accounting for percentages)
percentage=(100*mice_count/mice_sum)
percentage = pd.DataFrame(percentage)
percentage = percentage.unstack(level=0)
(percentage['Mouse Count'][['Capomulin','Infubinol','Ketapril','Placebo']]).plot(style=['.-','^-','o-','s-'],linewidth=0.5)

plt.xlim(min(x_axis)-5, max(x_axis)+5)
plt.xlabel('Treatment Duration (Days)')
plt.ylabel("Percentage")
plt.title('Mice percentage vs time')
plt.legend(['Capomulin','Infubinol','Ketapril','Placebo'],loc='upperleft')
plt.grid()

# Save the Figure
plt.savefig('Acconting for Percentage')

# Show the Figure
plt.show()


# ## Summary Bar Graph

# In[13]:


# Calculate the percent changes for each drug
tumor_volume_mean = data.groupby(['Drug','Timepoint'])['Tumor Volume (mm3)'].mean()

# Display the data to confirm
tumor_volume_unstack = tumor_volume_sum.unstack(level=1)
tumor_volume_unstack


# In[14]:


# Store all Relevant Percent Changes into a Tuple
percentage_1 = tuple(percentage)
percentage_list= percentage[['Capomulin','Infubinol','Ketapril','Placebo']].values
# Splice the data between passing and failing drugs
a=[]
for i in percentage_1:
    if i >0:
        a.append('Fail')
    else:
        a.append('Pass')
# Orient widths. Add labels, tick marks, etc. 
x_axis = np.arange(4)
plt.bar(x_axis,percentage_list,color=['g','r','r','r'],width=-1,align="edge")
ticks=['Capomulin','Infubinol','Ketapril','Placebo']
plt.xticks(np.arange(4),ticks)
plt.ylabel("% Tumor Volume Change")
plt.xlim(-1,3.25)
plt.grid()
# Use functions to label the percentages of changes
def percentage_label(label):
    for i in range(len(label)):
        plt.annotate(str(int(label[i]))+'%', xy=(0,0), color='w',xytext=(i-0.65, 5*np.sign(label[i])))


# Call functions to implement the function calls


# Save the Figure

# Show the Figure
# fig.show()


# In[14]:




