import streamlit as st
import pandas as pd
import plotly.express as px
d = pd.read_csv('B1.csv')
df= pd.DataFrame(d)
st.title("Product Sales Dashboard")

# Category selection
categories = df['CATEGORY'].unique()
c = st.multiselect(
    "Select Category:",
    options=categories,
    default=None
)
if c:
    filtered_df = df[df['CATEGORY'].isin(c)]
    fig1 =  px.bar(
        filtered_df,
        x='SUBCATEGORY',
        y='SALES',
        color='SUBCATEGORY',
        title=f'Sales by Subcategory for {c}'
    )
    st.plotly_chart(fig1, use_container_width=True)
    fig2 = px.pie(
        filtered_df,
        names='SUBCATEGORY',
        values='PROFIT',
        title=f'Sales Distribution by Subcategory for {c}'
    )
    st.plotly_chart(fig2, use_container_width=True)
    fig = px.sunburst(
        filtered_df,
        path=['CATEGORY', 'SUBCATEGORY'],
        values='SALES',
        title=f'Sales Hierarchy: {c}'
    )
    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("Please select at least one category to see the charts.")