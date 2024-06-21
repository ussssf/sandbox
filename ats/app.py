import plotly.express as px
import plotly.graph_objects as go

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
    color=list(sorted_data.values()),
    color_continuous_scale='Magma',
    labels={'x': 'Count', 'y': 'Name'},
    title='Top 10 Names by Count'
)

# Update layout to move names to the left
fig.update_layout(
    yaxis=dict(
        automargin=True,
        tickmode='array',
        tickvals=list(sorted_data.keys()),
        ticktext=['\u2007' + name for name in sorted_data.keys()],  # Adding a small space before the names
    ),
    coloraxis_showscale=False  # Hide the color scale bar
)

# Show the plot
fig.show()