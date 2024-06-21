import pandas as pd
import ipywidgets as widgets
from IPython.display import display, clear_output
import matplotlib.pyplot as plt

# Sample data
data = {
    "id1": {"name1": 10, "name2": 15, "name3": 20},
    "id2": {"name1": 5, "name2": 25, "name3": 30},
    "id3": {"name1": 8, "name2": 18, "name3": 28}
}

# Convert dictionary to DataFrame
def dict_to_dataframe(data):
    rows = []
    for id_, values in data.items():
        for name, count in values.items():
            rows.append({"ID": id_, "Name": name, "Count": count})
    return pd.DataFrame(rows)

df = dict_to_dataframe(data)

# Create search input
search_input = widgets.Text(placeholder='Enter ID to search')

# Function to plot counts
def plot_counts(id_):
    if id_ in data:
        names = list(data[id_].keys())
        counts = list(data[id_].values())
        plt.figure(figsize=(10, 6))
        plt.bar(names, counts, color='skyblue')
        plt.xlabel('Names')
        plt.ylabel('Counts')
        plt.title(f'Counts for {id_}')
        plt.show()
    else:
        print(f"No data available for ID: {id_}")

# Function to search and plot
def search_and_plot(change):
    clear_output(wait=True)
    display(search_input)
    search_value = change['new']
    if search_value:
        filtered_df = df[df['ID'].str.contains(search_value)]
        display(filtered_df)
        plot_counts(search_value)
    else:
        display(df)

search_input.observe(search_and_plot, names='value')
display(search_input)

# Display the initial table and plot
display(df)
plot_counts('id1')