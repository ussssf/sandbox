import pandas as pd
import plotly.graph_objects as go

# Example data with 'null' values
data = [
    {
        "Combination": ["ProductA", "Variation1"],
        "runids": ["101", "102", "103"]
    },
    {
        "Combination": ["ProductB", None],
        "runids": ["104", "105", "106"]
    },
    {
        "Combination": [None, "Variation3"],
        "runids": ["107", "108", "109"]
    },
    {
        "Combination": [None, None],
        "runids": ["110", "111"]
    }
]

# Replace None with 'null' to mimic the data structure mentioned
for entry in data:
    entry["Combination"] = [i if i is not None else 'null' for i in entry["Combination"]]

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Replace 'null' values with empty strings
df['Combination'] = df['Combination'].apply(lambda x: [i if i != 'null' else '' for i in x])
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