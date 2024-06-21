import pandas as pd
import plotly.graph_objects as go

# Example data
data = [
    {
        "Combination": ["ProductA", "Variation1"],
        "runids": ["101", "102", "103"]
    },
    {
        "Combination": ["ProductA", "Variation2"],
        "runids": ["104", "105", "106"]
    },
    {
        "Combination": ["ProductB", "Variation1"],
        "runids": ["107", "108", "109"]
    },
    {
        "Combination": ["ProductB", "Variation3"],
        "runids": ["110", "111", "112"]
    }
]

# Transform data into a hierarchical format
grouped_data = {}
for entry in data:
    product, variation = entry["Combination"]
    runids = ', '.join(entry["runids"])
    if product not in grouped_data:
        grouped_data[product] = []
    grouped_data[product].append((variation, runids))

# Prepare the table rows
table_rows = []
for product, variations in grouped_data.items():
    product_row_span = len(variations)
    for i, (variation, runids) in enumerate(variations):
        if i == 0:
            table_rows.append([product, variation, runids])
        else:
            table_rows.append(["", variation, runids])

# Create a DataFrame
df = pd.DataFrame(table_rows, columns=["Product", "Variation", "Run IDs"])

# Create the table with Plotly
fig = go.Figure(data=[go.Table(
    columnorder=[1, 2, 3],
    columnwidth=[80, 80, 200],
    header=dict(
        values=["Product", "Variation", "Run IDs"],
        fill_color='#1f77b4',
        align='left',
        font=dict(color='white', size=12),
        line_color='darkslategray'
    ),
    cells=dict(
        values=[df.Product, df.Variation, df['Run IDs']],
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