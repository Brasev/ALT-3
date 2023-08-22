import pandas as pd
import openpyxl
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go
import json
from streamlit_lottie import st_lottie
import requests

# Set page configuration
st.set_page_config(
    page_title="Bouncing Ball tracker",
    page_icon="🎱",
    layout="wide"
)

# Read data from CSV
df = pd.read_csv(
    filepath_or_buffer='ballpositions.csv',
    usecols=["X", "Y", "Gravity", "yv", "xv"],
    nrows=1000
)

# Extract columns from DataFrame
x_column = df["X"]
y_column = df["Y"]
gravity = df["Gravity"]
yv = df["yv"]
xv = df["xv"]

# Display title and subheaders
st.title("🎱 Bouncing Ball 🎱")
st.markdown("##")

def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_ball = load_lottieurl("https://lottie.host/50174de1-44c7-41db-ac1e-1e6dc78121da/ngeTUsNkmO.json")    

st.markdown("##")

# Create left and right columns for layout
left_column, right_column = st.columns([3, 7])

with left_column:
    # Display ball path details
    st.subheader(f"Ball path with:")
    st.subheader(f"Gravity: :blue[{gravity[0]}]")
    st.subheader(f"X velocity: :blue[{xv[0]}]")
    st.subheader(f"Y velocity: :blue[{yv[0]}]")
    st.subheader("______________________________")
    st.subheader(f"Highest point: :blue[({max(x_column)} , {max(y_column)})]")

# Create graph of ball path
graph = go.Scatter(x=x_column, y=y_column, mode='lines', name="<b>Ball path</b>")
x_column = x_column.tolist()
y_column = y_column.tolist()
fig = go.Figure()
fig.add_trace(graph)
fig.add_trace(go.Scatter(x=[x_column[0]], y=[y_column[0]], mode='markers+text', marker=dict(size=25, color='green'), name='Starting Point'))
fig.add_trace(go.Scatter(x=[x_column[-1]], y=[y_column[-1]], mode='markers', marker=dict(size=25, color='red'), name='End Point'))

# Configure layout of the graph
fig.update_layout(width=1000, height=600, margin=dict(t=0, l=0, r=100, b=0))

with right_column:
    # Display the graph
    st.plotly_chart(fig)

contact_form = """
<div class="container">
  <h1>Contact me</h1>
  <form target="_blank" action="https://formsubmit.co/your@email.com" method="POST">
    <div class="form-group">
      <div class="form-row">
        <div class="col">
          <input type="text" name="name" class="form-control" placeholder="Full Name" required>
        </div>
        <div class="col">
          <input type="email" name="email" class="form-control" placeholder="Email Address" required>
        </div>
      </div>
    </div>
    <div class="form-group">
      <textarea placeholder="Your Message" class="form-control" name="message" rows="10" required></textarea>
    </div>
    <button type="submit" class="btn btn-lg btn-dark btn-block">Submit Form</button>
  </form>
</div>
"""
st.markdown(contact_form, unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")


