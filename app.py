# import libraries
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import pickle



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


#user input

# function to find BMI value
def bmi(height,weight):
    h=height/100
    bmi_value = weight/(h**2)
    return bmi_value

#Getting user input
def user_inputs():

    #header
    st.header("User Dashboard")

    #Dashboard elements
    age = st.slider('Your Age',1,100,30)
    sex = st.selectbox('Select Your Gender',['male','female'])
    height = st.slider('Your Height in (cm)',50,250,150)
    weight = st.slider('Your Weight in (Kg)',10,150,50)
    children = st.selectbox('Number of Childrens in Your Family',[0,1,2,3,4,5])
    smoker = st.radio('Smoker', ['yes','no'])
    region = st.radio('Select Your Region',['northeast','northwest','southeast','southwest'])
    
    #reading user data as a dictionary
    bmi1 = bmi(height, weight)
    input_data={
        'age':age,
        'sex':sex,
        'bmi':bmi1,
        'children':children,
        'smoker':smoker,
        'region':region
    }
    
    #getting the copy of original data
    df = data.copy()
    #drop the predicting colmn
    df.drop('charges', axis=1, inplace=True)
    #input data as dataframe
    user_data = pd.DataFrame(input_data, index=[0])
    #concatenate original dataframe and user input dataframe
    user_df = pd.concat([df,user_data],ignore_index=True, axis=0)
    #getting dummies(categorical varaibles encoding)
    user_dum_data = pd.get_dummies(user_df, columns=['sex','children','smoker','region'], drop_first=True)
    #selecting the last row which is the user inputs
    user_input_data = user_dum_data.iloc[-1,:]
    #reading the user input data as a dataframe
    final_user_data = pd.DataFrame([user_input_data.array], columns=user_dum_data.columns)
    #user data
    st.subheader("User Data")
    st.dataframe(final_user_data)
    #returning data
    return final_user_data

user_results = user_inputs()

#Cost predictions

#loading the model
model = pickle.load(open("insurance_predict.pkl",'rb'))
#predicting the results
results = list(model.predict(user_results))

#setting the accuarcies, predictions
st.subheader("Predictions and Accuracies")
col3,col4 = st.columns(2)
with col3:
    st.metric("Insurance cost", str(results[0]))
with col4:
    st.metric("RMSE of the model", 4674.719889567355)