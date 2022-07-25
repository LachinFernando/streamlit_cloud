# import libraries
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns



# Title 
st.title("Insurance Cost Predictor")

# Reading the image
image = plt.imread("insurance.jpg")
#Setting the image
st.image(image, caption = "Health Matters the most")

# reading the data set
data = pd.read_csv("Insurance.csv")
# header as the data set
st.header("The Dataset")
# setting the dataframe
st.dataframe(data)

#creating plots

#gender distributions
def gender_distribution():
    sns.set_theme()
    fig = plt.figure()
    sns.countplot(x = data['sex'])
    plt.xlabel("Sex")
    plt.ylabel("Frequency")
    plt.title("Gender Distribution of the Applicants")
    st.pyplot(fig)

#population
def region():
    sns.set_theme()
    fig = plt.figure()
    sns.countplot(x = data['region'], palette="Set3")
    plt.xlabel("Region")
    plt.ylabel("Frequency")
    plt.title("Distribution of Regions")
    st.pyplot(fig)

# scatterplot
def scatterplot():
    sns.set_theme()
    fig = plt.figure()
    sns.scatterplot(data = data, x = data['bmi'], y = data['charges'], hue= data['smoker'])
    plt.xlabel("BMI value")
    plt.ylabel("Insurance Cost")
    plt.title("Scatter plot between BMI values and Insurance Cost")
    st.pyplot(fig)

#distribution plot
def age_distribution():
    sns.set_theme()
    fig = plt.figure()
    sns.distplot(x = data['age'], kde= True, rug= True, color = (0.7,0.3,0.2))
    plt.xlabel("Age")
    plt.ylabel("Density")
    plt.title("Distribution of Age")
    st.pyplot(fig)

#Function to visualize graphs
def visulaizations():
    #setting the subheader
    st.header("Data Visualization")
    #radio button
    title = st.radio("Select a variable", ["Gender Distribution","Regions and Frequencies","BMI vs Charges", "Age"])

    if title == "Gender Distribution":
        gender_distribution()
    
    elif title == "Regions and Frequencies":
        region()
    
    elif title == "BMI vs Charges":
        scatterplot()
    
    elif title == "Age":
        age_distribution()


visulaizations()

#more visualizations

#barplot
def children():
    sns.set_theme()
    fig = plt.figure()
    sns.countplot(x = data['children'])
    plt.xlabel("Number of childrens")
    plt.ylabel("Frequency")
    plt.title("Frequency Distribution according to the number of children")
    st.pyplot(fig)

#scatterplot
def scatterplot1():
    sns.set_theme()
    fig = plt.figure()
    sns.scatterplot(data = data, x = data['age'], y = data['charges'], hue= data['smoker'])
    plt.xlabel("Age")
    plt.ylabel("Insurance Cost")
    plt.title("Scatter plot between Age and Insurance Cost")
    st.pyplot(fig)

#creating columns
st.subheader("More Visualizations")
col1, col2 = st.columns(2)
with col1:
    children()
with col2:
    scatterplot1()