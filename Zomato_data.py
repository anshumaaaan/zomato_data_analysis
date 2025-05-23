import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Zomato Data Analysis Dashboard")

# Load the data
dataframe = pd.read_csv("Zomato-data-.csv")

# Clean the rating column
def handleRate(value):
    value = str(value).split('/')
    return float(value[0])

dataframe['rate'] = dataframe['rate'].apply(handleRate)

st.subheader("📊 Raw Data")
st.write(dataframe.head())

# Countplot for restaurant types
st.subheader("🍽️ Type of Restaurant Count")
fig1, ax1 = plt.subplots()
sns.countplot(x=dataframe['listed_in(type)'], ax=ax1)
plt.xticks(rotation=45)
st.pyplot(fig1)

# Votes per restaurant type
st.subheader("💬 Total Votes by Type of Restaurant")
grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
fig2, ax2 = plt.subplots()
grouped_data.plot(kind='line', marker='o', color='green', ax=ax2)
plt.xlabel("Type of restaurant")
plt.ylabel("Total votes")
st.pyplot(fig2)

# Restaurant(s) with max votes
max_votes = dataframe['votes'].max()
restaurant_with_max_votes = dataframe.loc[dataframe['votes'] == max_votes, 'name']
st.subheader("🏆 Restaurant(s) with Maximum Votes")
st.write(restaurant_with_max_votes.tolist())

# Online Order preference
st.subheader("📦 Online Order Distribution")
fig3, ax3 = plt.subplots()
sns.countplot(x=dataframe['online_order'], ax=ax3)
st.pyplot(fig3)

# Ratings Distribution
st.subheader("⭐ Ratings Distribution")
fig4, ax4 = plt.subplots()
plt.hist(dataframe['rate'], bins=5)
plt.title("Ratings Distribution")
st.pyplot(fig4)

# Approximate cost for two people
st.subheader("💰 Most Preferred Cost for Two People")
fig5, ax5 = plt.subplots()
sns.countplot(x=dataframe['approx_cost(for two people)'], ax=ax5)
plt.xticks(rotation=45)
st.pyplot(fig5)

most_common_cost = dataframe['approx_cost(for two people)'].mode()[0]
st.write("Most preferred cost:", most_common_cost)

# Boxplot: Online order vs rating
st.subheader("📉 Rating Distribution by Online Order Availability")
fig6, ax6 = plt.subplots()
sns.boxplot(x='online_order', y='rate', data=dataframe, ax=ax6)
st.pyplot(fig6)

# Heatmap
st.subheader("🗺️ Heatmap: Online Order by Restaurant Type")
pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
fig7, ax7 = plt.subplots()
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='d', ax=ax7)
plt.title("Heatmap")
plt.xlabel("Online Order")
plt.ylabel("Type")
st.pyplot(fig7)

# Insight
st.info("💡 Dining restaurants primarily accept offline orders whereas cafes primarily receive online orders. Clients prefer to place orders in person at restaurants, but prefer online ordering at cafes.")
