import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

# Read the CSV file
df = pd.read_csv('./data/PnL.csv')

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create a section for Day's Profit vs Date
st.subheader("Day's Profit vs Date")

# Create a line chart for Day's Profit vs Date
fig_day_profit = px.line(df, x='Date', y="Day's Profit", title="Line Chart: Day's Profit vs Date")
fig_day_profit.update_xaxes(title='Date')
fig_day_profit.update_yaxes(title="Day's Profit")

# Display the histogram for Day's Profit vs Date
st.plotly_chart(fig_day_profit)

# Create a bar chart for "Day's Profit" vs Date using Plotly
fig = go.Figure(go.Bar(x=df['Date'], y=df["Day's Profit"]))
fig.update_layout(title="Day's Profit vs Date", xaxis_title='Date', yaxis_title="Day's Profit")

# Display the bar chart
st.plotly_chart(fig)

chart_data = pd.DataFrame(columns=["Date", "Day's Profit"])

st.bar_chart(chart_data)

# Create a section for Revenue vs Date
st.subheader("Revenue vs Date")

# Create line plot with Plotly
fig = go.Figure()

# Add trace for HS Revenue
fig.add_trace(go.Scatter(x=df['Date'], y=df['HS Revenue'], mode='lines', name='HS Revenue'))

# Add trace for MS Revenue
fig.add_trace(go.Scatter(x=df['Date'], y=df['MS Revenue'], mode='lines', name='MS Revenue'))

# Add trace for XP Revenue
fig.add_trace(go.Scatter(x=df['Date'], y=df['XP Revenue'], mode='lines', name='XP Revenue'))

# Update layout
fig.update_layout(title='Revenue vs Date',
                  xaxis_title='Date',
                  yaxis_title='Revenue')



# Display Plotly chart using Streamlit
st.plotly_chart(fig)


## XP SALES
# Create a bar chart for "Day's Profit" vs Date using Plotly
fig_xp_sales = go.Figure(go.Bar(x=df['Date'], y=df["XP Actual Nozzle Sales"]))
fig_xp_sales.update_layout(title="XP Sales vs Date", xaxis_title='Date', yaxis_title="Day's Sales")

# Display the histogram for Day's Profit vs Date
st.plotly_chart(fig_xp_sales)


## HS Sales
# Create a bar chart for "Day's Profit" vs Date using Plotly
fig_hs_sales = go.Figure(go.Bar(x=df['Date'], y=df["HS Actual Nozzle Sales"]))
fig_hs_sales.update_layout(title="HS Sales vs Date", xaxis_title='Date', yaxis_title="Day's Sales")

# Display the histogram for Day's Profit vs Date
st.plotly_chart(fig_hs_sales)


## MS SALES
# Create a bar chart for "Day's Profit" vs Date using Plotly
fig_ms_sales = go.Figure(go.Bar(x=df['Date'], y=df["MS Actual Nozzle Sales"]))
fig_ms_sales.update_layout(title="MS Sales vs Date", xaxis_title='Date', yaxis_title="Day's Sales")

# Display the histogram for Day's Profit vs Date
st.plotly_chart(fig_ms_sales)


##--------------------Expenses Vs. Revnue--------------------------

# # Plot Expenses vs. Revenue by date
# fig = go.Figure()

# # Add trace for Expenses
# fig.add_trace(go.Scatter(x=df['Date'], y=df['Total Expenses'], mode='lines', name='Total Revenue', line=dict(color='red')))

# # Add trace for Revenue
# fig.add_trace(go.Scatter(x=df['Date'], y=df['Total Expenses'], mode='lines', name='Total Revenue', line=dict(color='green')))

# # Update layout
# fig.update_layout(title='Expenses vs. Revenue by Date',
#                   xaxis_title='Date',
#                   yaxis_title='Amount')

# # Show plot
# st.plotly_chart(fig)