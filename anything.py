import streamlit as st
import matplotlib.pyplot as plt

def display_pie_chart(data_dict, title="Pie Chart"):
    """
    Display a pie chart in Streamlit.
    
    Parameters:
    - data_dict (dict): A dictionary with labels as keys and values as values.
    - title (str): Title of the pie chart.
    """
    labels = list(data_dict.keys())
    values = list(data_dict.values())
    
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    ax.set_title(title)
    
    st.pyplot(fig)

# Example usage in a Streamlit app
if __name__ == "__main__":
    st.title("Pie Chart Example")
    
    sample_data = {"A": 40, "B": 30, "C": 20, "D": 10}
    display_pie_chart(sample_data, title="Sample Pie Chart")
