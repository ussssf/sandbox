import plotly.express as px

# Sample data
data = {
    "Name1": 10,
    "Name2": 20,
    "Name3": 30,
    "Name4": 40,
    "Name5": 50,
    "Name6": 60,
    "Name7": 70,
    "Name8": 80,
    "Name9": 90,
    "Name10": 100,
    "Name11": 110,
    "Name12": 120
}

# Sort data by value and select top 10
sorted_data = dict(sorted(data.items(), key=lambda item: item[1], reverse=True)[:10])

# Create a horizontal bar chart
fig = px.bar(
    x=list(sorted_data.values()),
    y=list(sorted_data.keys()),
    orientation='h',
    labels={'x': 'Count', 'y': 'Name'},
    title='Top 10 Names by Count'
)

# Show the plot
fig.show()