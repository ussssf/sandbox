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

# Create table using Plotly
fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df.Combination, df.runids],
               fill_color='lavender',
               align='left'))
])

# Show the table
fig.show()