# import pandas as pd
# import streamlit as st
# import plotly.express as px

# # Read the CSV file
# df = pd.read_csv('PnL.csv')

# # Plotting histogram of Day's Profit vs Date using Plotly
# fig = px.histogram(df, x='Date', y="Day's Profit", title="Histogram: Day's Profit vs Date")
# fig.update_layout(xaxis_title='Date', yaxis_title="Day's Profit")
# st.plotly_chart(fig)

# import pandas as pd
# import streamlit as st
# import plotly.express as px

# # Read the CSV file
# df = pd.read_csv('PnL.csv')

# # Convert Date column to datetime
# df['Date'] = pd.to_datetime(df['Date'])

# # Create a histogram for Day's Profit vs Date
# fig_day_profit = px.histogram(df, x='Date', y="Day's Profit", histfunc='count', title="Histogram: Day's Profit vs Date")
# fig_day_profit.update_xaxes(title='Date')
# fig_day_profit.update_yaxes(title="Frequency of Day's Profit")



# # Display the histogram for Day's Profit vs Date
# st.plotly_chart(fig_day_profit)

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



# Create line plot with Plotly
fig = go.Figure()

# Add trace for XP Actual Nozzle Sales
fig.add_trace(go.Scatter(x=df['Date'], y=df['XP Actual Nozzle Sales'], mode='lines', name='XP Actual Nozzle Sales'))

# Add trace for HS Actual Nozzle Sales
fig.add_trace(go.Scatter(x=df['Date'], y=df['HS Actual Nozzle Sales'], mode='lines', name='HS Actual Nozzle Sales'))

# Add trace for MS Actual Nozzle Sales
fig.add_trace(go.Scatter(x=df['Date'], y=df['MS Actual Nozzle Sales'], mode='lines', name='MS Actual Nozzle Sales'))

# Update layout
fig.update_layout(title='Actual Nozzle Sales vs Date',
                  xaxis_title='Date',
                  yaxis_title='Actual Nozzle Sales')

# Display Plotly chart using Streamlit
st.plotly_chart(fig)