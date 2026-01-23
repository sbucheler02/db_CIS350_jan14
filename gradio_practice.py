import gradio as gr
import sqlite3
import pandas as pd

def fetch_points():
    conn = sqlite3.connect('points.db')
    cursor = conn.cursor()
    query = """
        SELECT *
        FROM points;
    """
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    records_df = pd.DataFrame(records, columns = ['id', 'x', 'y'])
    return records_df

iface = gr.Interface(fn = fetch_points, inputs = [], outputs = gr.Dataframe(headers = ['id', 'x', 'y']))

iface.launch()