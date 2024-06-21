import pandas as pd
import plotly.graph_objects as go

# Example data
data = [
    {
        "Combination": ["ProductA", "Variation1"],
        "runids": ["101", "102", "103"]
    },
    {
        "Combination": ["ProductB", "Variation2"],
        "runids": ["104", "105", "106"]
    },
    {
        "Combination": ["ProductC", "Variation3"],
        "runids": ["107", "108", "109"]
    }
]

# Convert data to a DataFrame
df = pd.DataFrame(data)
df['Combination'] = df['Combination'].apply(lambda x: ' - '.join(x))
df['runids'] = df['runids'].apply(lambda x: ', '.join(x))

# Create table using Plotly with enhanced styling
fig = go.Figure(data=[go.Table(
    header=dict(
        values=list(df.columns),
        fill_color='#1f77b4',
        align='left',
        font=dict(color='white', size=12),
        line_color='darkslategray'
    ),
    cells=dict(
        values=[df.Combination, df.runids],
        fill_color=['#f2f2f2', '#fafafa'],
        align='left',
        font=dict(color='darkslategray', size=11),
        line_color='darkslategray',
        height=30
    )
)])

# Update layout for better appearance
fig.update_layout(
    title='Product Variations and Run IDs',
    title_x=0.5,
    margin=dict(l=0, r=0, t=40, b=0)
)

# Show the table
fig.show()