import plotly.express as px
import plotly.graph_objects as go

# Your data dictionary
data = {
    "astrotrue": 0.4,
    "astrofalse": 0.1,
    "qarnottrue": 0.35,
    "qarnotfalse": 0.15
}

# Prepare data for ASTRO chart
astro_labels = ["True", "False"]
astro_values = [data["astrotrue"], data["astrofalse"]]

# Prepare data for Qarnot chart
qarnot_labels = ["True", "False"]
qarnot_values = [data["qarnottrue"], data["qarnotfalse"]]

# Create ASTRO donut chart with Magma theme
fig_astro = go.Figure(data=[go.Pie(labels=astro_labels, values=astro_values, hole=0.3)])
fig_astro.update_traces(marker=dict(colors=px.colors.sequential.Magma))
fig_astro.update_layout(title_text="ASTRO Donut Chart")

# Create Qarnot donut chart with Magma theme
fig_qarnot = go.Figure(data=[go.Pie(labels=qarnot_labels, values=qarnot_values, hole=0.3)])
fig_qarnot.update_traces(marker=dict(colors=px.colors.sequential.Magma))
fig_qarnot.update_layout(title_text="Qarnot Donut Chart")

# Display the charts
fig_astro.show()
fig_qarnot.show()