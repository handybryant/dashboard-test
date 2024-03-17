# Use streamlit to create a web app, with a two buttons
#   "Refresh": read the data from /data/data.xlsx as pandas dataframe, saved into df_data
#   "Plot": using plotly to plot the data from df_data as line chart, "date" as x-asis,
#           "close" as y-axis, "asset" as color

import streamlit as st
import pandas as pd
import plotly.express as px

# create a button to read the data from /data/data.xlsx
@st.cache
def load_data():
    df = pd.read_excel('data/data.xlsx')
    return df


# create a button to plot the data
def plot_data(df):
    fig = px.line(df, x="date", y="close", color="asset")
    st.plotly_chart(fig)


# main function
def main():
    st.title("Stock Data Visualization")
    st.write("This is a simple web app to visualize stock data")

    # create a button to read the data from /data/data.xlsx
    if st.button("Refresh"):
        df_data = load_data()
        st.write(df_data)

    # create a button to plot the data
    if st.button("Plot"):
        df_data = load_data()
        plot_data(df_data)


if __name__ == '__main__':
    main()