import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.button')



add_sidebar = st.sidebar.selectbox('Aggregate or Individual', ['Aggregate', 'Individual'])

if add_sidebar == 'Aggregate':

    col1, col2, col3, col4, col5 = st.columns(5)
    columns = [col1, col2, col3, col4, col5]

    count = 0
    for i in range(10):
        with columns[count]:
            st.metric('Metric ' + str(i+1), 100 * count, delta = "{:.2%}".format(0.1))
            count += 1
            if count >= 5:
                count = 0
    df = pd.DataFrame({'Value ' + 'a': [1, 2, 3], 'Value ' + 'b': [4, 5, 6], 'Value ' + 'c': [7, 8, 9], 'Value ' + 'd': [10, 11, 12], 'Value ' + 'e': [13, 14, 15]})
    st.write(df)
    st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

if add_sidebar == 'Individual':
    videos = st.selectbox('Select Video', ['Video 1', 'Video 2', 'Video 3'])

    st.write('Hello, *World!* :sunglasses:')
    st.write(1234)
    
    df2 = pd.DataFrame(
        np.random.randn(200, 3),
        columns=['a', 'b', 'c'])
    c = alt.Chart(df2).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
    st.write(c)
