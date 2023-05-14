import dash
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

# Load the data
url = 'https://raw.githubusercontent.com/Zixuan-YU/predicting_hotel_cancellation/main/hotel_bookings.csv?token=GHSAT0AAAAAACAVZNMHZCW46ERZ6NMO6OWUZDAGUCA'
df = pd.read_csv(url)

# Calculate the correlation and round it
correlation = df.corr().round(2)

# Create a heatmap with Plotly
heatmap = ff.create_annotated_heatmap(
    z=correlation.values,
    x=list(correlation.columns),
    y=list(correlation.index),
    annotation_text=correlation.values,
    colorscale='YlOrBr',
    hoverinfo='z'
)

# Create a Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Calculate the NA distribution
na_distribution = df.isna().sum().reset_index()
na_distribution.columns = ['Column', 'Missing Values']

# Create a DataTable for the NA distribution
na_table = dash.dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in na_distribution.columns],
    data=na_distribution.to_dict('records'),
)

# Create dropdowns and containers for the count plots
dropdowns = []
containers = []
variables = [
    ('cat', ['no_of_adults', 'no_of_children', 'no_of_weekend_nights', 'no_of_week_nights', 'type_of_meal_plan', 
             'required_car_parking_space', 'room_type_reserved', 'arrival_year']),
    ('mon', ['arrival_month', 'market_segment_type', 'repeated_guest', 'no_of_previous_cancellations', 'no_of_special_requests', 
             'booking_status']),
    ('con', ['lead_time', 'arrival_date', 'avg_price_per_room', 'no_of_previous_bookings_not_canceled'])
]

for prefix, var_list in variables:
    dropdowns.append(dcc.Dropdown(
        id=f'dropdown-{prefix}',
        options=[{'label': i, 'value': i} for i in var_list],
        value=var_list[0]
    ))
    containers.append(dcc.Graph(id=f'countplot-{prefix}'))

# Create a dropdown for the boxplot variables selection
boxplot_vars = ['lead_time', 'avg_price_per_room']

dropdown_boxplot = dcc.Dropdown(
    id='dropdown-boxplot',
    options=[{'label': i, 'value': i} for i in boxplot_vars],
    value=boxplot_vars[0]
)

# Create a container for the boxplot
boxplot_container = dcc.Graph(id='boxplot')

# Create a dropdown for the boxplots
boxplot_den_vars = ['no_of_adults', 'no_of_children', 'no_of_weekend_nights', 'market_segment_type', 'type_of_meal_plan',
                'room_type_reserved', 'no_of_special_requests', 'arrival_month', 'arrival_date',
                'no_of_previous_cancellations', 'no_of_previous_bookings_not_canceled']

dropdown_den_boxplot = dcc.Dropdown(
    id='dropdown-boxplot-density',
    options=[{'label': i, 'value': i} for i in boxplot_den_vars],
    value=boxplot_den_vars[0]
)

# Create a container for the boxplots
boxplot_den_container = dcc.Graph(id='boxplot-density')

# Create a dropdown for the scatter plot hues
scatter_hue = ['booking_status']

dropdown_scatter = dcc.Dropdown(
    id='dropdown-scatter',
    options=[{'label': i, 'value': i} for i in scatter_hue],
    value=scatter_hue[0]
)

# Create a container for the scatter plot
scatter_container = dcc.Graph(id='scatter-plot')

# Arrange the components in the app layout
app.layout = html.Div([
    html.H1("Data Visualization Dashboard"),
    html.H2("NA Distribution"),
    na_table,
    html.H2("Verifying the correlation between our variables"),
    dcc.Graph(id='heatmap', figure=heatmap),
    html.H2("Histograms of Categorical Variables"),
    dropdowns[0],
    containers[0],
    html.H2("Histograms of Bookings by Month"),
    dropdowns[1],
    containers[1],
    html.H2("Histograms of Continous Variables"),
    dropdowns[2],
    containers[2],
    html.H2("Boxplots of Variables"),
    dropdown_boxplot,
    boxplot_container,
    html.H2("Boxplot Density Analysis"),
    dropdown_den_boxplot,
    boxplot_den_container,
    html.H2("Tendency for higher price x higher lead time for cancellations"),
    dropdown_scatter,
    scatter_container
])

# Define callbacks to update the count plots based on the dropdown selections
@app.callback(
    Output('countplot-cat', 'figure'),
    Input('dropdown-cat', 'value')
)
def update_cat_countplot(selected_var):
    fig = px.histogram(df, x=selected_var, nbins=50)
    return fig

@app.callback(
    Output('countplot-mon', 'figure'),
    Input('dropdown-mon', 'value')
)
def update_mon_countplot(selected_var):
    fig = px.histogram(df, x=selected_var, nbins=50)
    return fig

@app.callback(
    Output('countplot-con', 'figure'),
    Input('dropdown-con', 'value')
)
def update_con_countplot(selected_var):
    fig = px.histogram(df, x=selected_var, nbins=50)
    return fig
    
# Define a callback to update the boxplot based on the dropdown selection
@app.callback(
    Output('boxplot', 'figure'),
    Input('dropdown-boxplot', 'value')
)
def update_boxplot(selected_var):
    fig = go.Figure()
    fig.add_trace(go.Box(y=df[selected_var], name=selected_var))
    return fig

# Define a callback to update the boxplots based on the dropdown selection
@app.callback(
    Output('boxplot-density', 'figure'),
    Input('dropdown-boxplot-density', 'value')
)
def update_boxplot(selected_var):
    fig = px.box(df, x=selected_var, y="lead_time")
    return fig

# Define a callback to update the scatter plot based on the dropdown selection
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('dropdown-scatter', 'value')]
)
def update_scatter_plot(selected_hue):
    fig = px.scatter(df, x="lead_time", y="avg_price_per_room", color=selected_hue)
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(host='jupyter.biostat.jhsph.edu', port=1044, debug=False)