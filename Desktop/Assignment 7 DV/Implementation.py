import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load dataset
df = pd.read_csv("world_cup_data.csv")

# Dash app setup
app = dash.Dash(__name__)

# Create Choropleth map
fig = px.choropleth(df, locations='Winner', locationmode='country names',
                    title='FIFA World Cup Winners',
                    color_discrete_sequence=['gold'])

# Dash Layout
app.layout = html.Div([
    html.H1('FIFA World Cup Dashboard', style={'textAlign': 'center'}),
    dcc.Graph(figure=fig),
    
    # Dropdown for country selection
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in df['Winner'].unique()],
        placeholder='Select a Country'
    ),
    html.Div(id='country-output'),
    
    # Dropdown for year selection
    dcc.Dropdown(
        id='year-dropdown',
        options=[{'label': year, 'value': year} for year in df['Year']],
        placeholder='Select a Year'
    ),
    html.Div(id='year-output')
])

# Callbacks
@app.callback(
    dash.Output('country-output', 'children'),
    [dash.Input('country-dropdown', 'value')]
)
def update_country_output(country):
    if country:
        count = df[df['Winner'] == country].shape[0]
        return f'{country} has won the World Cup {count} times.'
    return ''

@app.callback(
    dash.Output('year-output', 'children'),
    [dash.Input('year-dropdown', 'value')]
)
def update_year_output(year):
    if year:
        row = df[df['Year'] == year]
        return f'Winner: {row.Winner.values[0]}, Runner-Up: {row["Runner-Up"].values[0]}'
    return ''

# Run the server
if __name__ == '__main__':
    app.run(debug=True)

