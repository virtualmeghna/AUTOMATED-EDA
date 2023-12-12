import numpy as np
import pandas as pd
import streamlit as st
from annotated_text import annotated_text
# from pandas_profiling import ProfileReport
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


st.set_page_config(layout="wide")


# Web App Title
st.markdown('''
# **Automated EDA using AutoML**
            
Exploratory Data Analysis, a term so fancy it's almost scary for people who just want to learn about their data.\n
**EDA stands for "Exploratory Data Analysis"**. It's a way to dig into a dataset to understand its main characteristics, patterns, 
and relationships. Think of it like investigating a puzzle before solving it. EDA involves techniques to visualize data, 
summarize its key features, and uncover insights that might help you make better decisions or develop further analyses. Sounds so fancy right? Generally you'd require advanced knowledge of Python, Statistics and several visualization tools to be able to achieve this feat.
But what if could tell you that you conduct your own EDA using your own Dataset, a job apparetnly only reserved for Data analysts, all on your own with just a simple click?
''')
            
st.markdown("**Hereby, I introduce you to AutoML, which stands for 'Automated Machine Learning'. I have created this webapp to make all those special terms like Machine Learning and AI available to everyone. With this app, I hope to motivate people to understand the power of Data and how all you need is simple webapp to conduct it.**")

st.markdown('''This App is created in Streamlit using the **Numpy**, **Pandas** & **pandas-profiling** library.

**Credit:** App built in `Python` + `Streamlit` by :red[**Akash Sharma** ]''')
        
st.write(":arrow_forward: Here's how it works: ")
st.write('1. Upload your CSV file in the sidebar. (Or just to see how it works, you can use the given example Dataset)')
st.write('2. Wait for the app to load the data and generate the report.')
st.write('3. You can then visualize the Report by scrolling down as well as Download the report and use it for your own purposes.')
st.write('---')

# Upload CSV data
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
st.sidebar.subheader("Or Use an Example Dataset :point_down:")
                        
# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache_data
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Analysis Report**')
    st_profile_report(pr)

    export=pr.to_html()
    st.sidebar.write('---')
    st.sidebar.subheader('Download your Report :point_down:')
    st.sidebar.download_button(label="Download here", data=export, file_name='report.html')

else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.sidebar.button('Press to use Example Dataset'):
        # Example data
        @st.cache_data
        def load_data():
            df = pd.read_csv('Top_1000_Companies_Dataset.csv')
            return df
        df = load_data()

        with   st.sidebar.expander("About the example Dataset"):
            st.write("This comprehensive dataset contains informations about 'Top 1000 Companies' and can be used to analyze, visualize, and model the performance and characteristics of the top 1000 companies across various industries.")
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Analysis Report**')
        st_profile_report(pr)

        export=pr.to_html()
        st.sidebar.write('---')
        st.sidebar.subheader('Download your Report :point_down:')
        st.sidebar.download_button(label="Download here", data=export, file_name='report.html')