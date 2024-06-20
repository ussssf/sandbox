import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Sample data
data = {
    "Electronics": {
        "proportion": 0.4,
        "variations": {
            "Smartphones": 120,
            "Laptops": 80,
            "Tablets": 40
        }
    },
    "Furniture": {
        "proportion": 0.3,
        "variations": {
            "Chairs": 70,
            "Tables": 30,
            "Sofas": 20
        }
    },
    "Clothing": {
        "proportion": 0.2,
        "variations": {
            "Shirts": 150,
            "Jeans": 100,
            "Jackets": 50
        }
    },
    "Toys": {
        "proportion": 0.1,
        "variations": {
            "Action Figures": 60,
            "Board Games": 30,
            "Puzzles": 10
        }
    }
}

# Prepare data for pie chart
labels = list(data.keys())
proportions = [data[product_type]["proportion"] for product_type in data]

# Create pie chart
fig_pie = go.Figure(data=[go.Pie(labels=labels, values=proportions, hole=.3)])
fig_pie.update_layout(
    title_text="Proportion of Each Product Type",
    paper_bgcolor='black',
    plot_bgcolor='black',
    font=dict(color='white')
)
fig_pie.show()

# Prepare data for bar chart
variations_data = []
for product_type, product_info in data.items():
    for variation, count in product_info["variations"].items():
        variations_data.append({
            "Product Type": product_type,
            "Variation": variation,
            "Count": count
        })

df_variations = pd.DataFrame(variations_data)

# Create bar chart
fig_bar = px.bar(df_variations, x="Product Type", y="Count", color="Variation", barmode="group")
fig_bar.update_layout(
    title_text="Product Variations Count by Product Type",
    paper_bgcolor='black',
    plot_bgcolor='black',
    font=dict(color='white')
)
fig_bar.show()