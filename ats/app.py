https://typst.app/project/wUlSkeYjNvrvf1KFmzxfcwclnoff


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

# Customize the chart
fig.update_traces(marker_color='rgb(58, 71, 80)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6)

# Add annotations
for i, (name, count) in enumerate(sorted_data.items()):
    fig.add_annotation(x=count, y=name,
                       text=str(count),
                       showarrow=False,
                       font=dict(size=12, color='rgb(8,48,107)'),
                       align='center')

# Update layout for better visuals
fig.update_layout(
    plot_bgcolor='white',
    paper_bgcolor='white',
    title_font=dict(size=24, color='rgb(8,48,107)'),
    xaxis=dict(
        title='Count',
        titlefont_size=16,
        tickfont_size=14,
        gridcolor='lightgrey'
    ),
    yaxis=dict(
        title='Name',
        titlefont_size=16,
        tickfont_size=14
    ),
    margin=dict(l=100, r=20, t=50, b=50)
)

# Show the plot
fig.show()