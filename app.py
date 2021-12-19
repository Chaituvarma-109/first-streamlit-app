import datetime
import yfinance as yf
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


def draw_line_chart(data, x, y):
    figure = px.line(data, x=x, y=y)
    st.plotly_chart(figure, use_container_width=True)


st.title("**Stock Price Analysis**")

ticker_name = st.sidebar.text_input(label="Enter ticker name you want to see...", value="GOOG")
start_date = st.sidebar.date_input(label="Select the starting date", value=datetime.date(2021, 12, 1))
end_date = st.sidebar.date_input(label="Select the ending date")

df = yf.download(ticker_name, start=start_date, end=end_date)

st.header(f"Stock Name: {ticker_name}")

st.subheader("Candlestick")
fig = go.Figure(data=[go.Candlestick(
    x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close']
)])
fig.update_layout(xaxis_rangeslider_visible=False)
st.plotly_chart(fig, use_container_width=False)

st.subheader("Close Price")
draw_line_chart(df, df.index, 'Close')

st.subheader("Volume")
draw_line_chart(df, df.index, 'Volume')
