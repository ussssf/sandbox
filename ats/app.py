import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Sample data
data = {
    "Smartphones": {
        "Electronics": {
            "errors": 15,
            "total": 200,
            "error_rate": 0.075
        },
        "Accessories": {
            "errors": 5,
            "total": 50,
            "error_rate": 0.1
        }
    },
    "Laptops": {
        "Electronics": {
            "errors": 10,
            "total": 100,
            "error_rate": 0.1
        },
        "Accessories": {
            "errors": 3,
            "total": 30,
            "error_rate": 0.1
        }
    },
    "Chairs": {
        "Furniture": {
            "errors": 7,
            "total": 80,
            "error_rate": 0.0875
        },
        "Office Supplies": {
            "errors": 2,
            "total": 20,
            "error_rate": 0.1
        }
    },
    "Tables": {
        "Furniture": {
            "errors": 5,
            "total": 60,
            "error_rate": 0.0833
        },
        "Office Supplies": {
            "errors": 1,
            "total": 15,
            "error_rate": 0.0667
        }
    },
    "Shirts": {
        "Clothing": {
            "errors": 20,
            "total": 150,
            "error_rate": 0.1333
        },
        "Casual": {
            "errors": 6,
            "total": 50,
            "error_rate": 0.12
        }
    },
    "Jeans": {
        "Clothing": {
            "errors": 12,
            "total": 100,
            "error_rate": 0.12
        },
        "Casual": {
            "errors": 4,
            "total": 40,
            "error_rate": 0.1
        }
    }
}

# Prepare data for bar chart and scatter plot
errors_data = []
error_rate_data = []
for variation, product_types in data.items():
    for product_type, metrics in product_types.items():
        errors_data.append({
            "Product Variation": variation,
            "Product Type": product_type,
            "Errors": metrics["errors"]
        })
        error_rate_data.append({
            "Product Variation": variation,
            "Product Type": product_type,
            "Error Rate": metrics["error_rate"]
        })

df_errors = pd.DataFrame(errors_data)
df_error_rate = pd.DataFrame(error_rate_data)

# Create bar chart for errors
fig_errors = px.bar(df_errors, x="Product Variation", y="Errors", color="Product Type", barmode="group")
fig_errors.update_layout(
    title_text="Number of Errors by Product Variation and Product Type",
    paper_bgcolor='black',
    plot_bgcolor='black',
    font=dict(color='white')
)
fig_errors.show()

# Create scatter plot for error rate
fig_error_rate = px.scatter(df_error_rate, x="Product Variation", y="Error Rate", color="Product Type", size="Error Rate")
fig_error_rate.update_layout(
    title_text="Error Rate by Product Variation and Product Type",
    paper_bgcolor='black',
    plot_bgcolor='black',
    font=dict(color='white')
)
fig_error_rate.show()