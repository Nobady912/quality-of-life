import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

# Sample data with updated columns from the screenshot
data = {
    'City': ['Montreal', 'Vancouver', 'Winnipeg', 'Kingston', 'Kitchener', 'Quebec City', 'Ottawa', 'Toronto', 'Edmonton', 'Calgary', 'Hamilton'],
    'Latitude': [45.5, 49.2, 49.9, 44.2, 43.4, 46.8, 45.4, 43.7, 53.5, 51.0, 43.2],
    'Longitude': [-73.6, -123.1, -97.1, -76.5, -80.5, -71.2, -75.7, -79.4, -113.5, -114.1, -79.9],
    'Environment': [32, 100, 0, 60, 0, 16, 69, 49, 36, 52, 42],
    'Society': [100, 22, 0, 32, 0, 16, 19, 49, 10, 27, 68],
    'Access': [2, 52, 40, 2, 0, 3, 31, 39, 36, 60, 5],
    'Prospect': [82, 79, 0, 35, 47, 20, 45, 100, 39, 70, 39],
    'Affordability': [55, 55, 0, 31, 47, 20, 45, 59, 39, 70, 39]
}

df = pd.DataFrame(data)

# Initialize the Dash app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    html.H1("Index Dashboard for Student Quality of Life", style={'textAlign': 'center', 'marginBottom': '20px'}),
    html.Button("SWITCH TO FRENCH", id='language-switch', n_clicks=0, style={'backgroundColor': 'rgb(209, 209, 209)', 'margin': '10px'}),
    
    html.Div([
        html.Div([
            html.H2("City Value", id='city-value-title', style={'textAlign': 'center', 'color': '#333333'}),
            dcc.Dropdown(
                id='city-dropdown',
                options=[{'label': city, 'value': city} for city in df['City']],
                value='Toronto',
                style={'color': '#333333'}
            ),
            html.Div(id='city-value', style={'padding': '10px'})
        ], className='column-left', style={'width': '30%', 'padding': '20px', 'backgroundColor': 'rgb(225, 225, 225)', 'borderRadius': '10px', 'margin': '10px'}),
        
        html.Div([
            dcc.Graph(id='map', style={'width': '70%', 'height': '600px', 'border': 'none', 'borderRadius': '10px', 'padding': '0', 'margin': '10px', 'backgroundColor': 'rgb(161, 161, 161)'})
        ], className='graph-container', style={'width': '70%', 'padding': '20px'})
    ], className='main-container', style={'display': 'flex', 'flexDirection': 'row', 'backgroundColor': 'rgb(209, 209, 209)', 'padding': '20px', 'width': '100%'}),
    
    html.Div([
        html.Div([
            html.H3("City Rank", id='city-rank-title', style={'textAlign': 'center', 'color': '#333333'}),
            html.Div(id='city-rank', style={'padding': '10px'})
        ], className='rounded-box', style={'width': '45%', 'padding': '20px', 'backgroundColor': 'rgb(225, 225, 225)', 'borderRadius': '10px', 'margin': '10px'}),
        
        html.Div([
            html.H3("Weights", id='weights-title', style={'textAlign': 'center', 'color': '#333333'}),
            html.Div([
                html.P("Environment", id='environment-label', style={'color': '#333333'}),
                dcc.Slider(
                    id='slider-1',
                    min=0,
                    max=5,
                    step=1,
                    value=1,
                    marks={i: str(i) for i in range(6)},
                    className='blue-slider'
                )
            ], style={'margin': '10px 0'}),
            html.Div([
                html.P("Society", id='society-label', style={'color': '#333333'}),
                dcc.Slider(
                    id='slider-2',
                    min=0,
                    max=5,
                    step=1,
                    value=1,
                    marks={i: str(i) for i in range(6)},
                    className='blue-slider'
                )
            ], style={'margin': '10px 0'}),
            html.Div([
                html.P("Access", id='access-label', style={'color': '#333333'}),
                dcc.Slider(
                    id='slider-3',
                    min=0,
                    max=5,
                    step=1,
                    value=1,
                    marks={i: str(i) for i in range(6)},
                    className='blue-slider'
                )
            ], style={'margin': '10px 0'}),
            html.Div([
                html.P("Prospects", id='prospects-label', style={'color': '#333333'}),
                dcc.Slider(
                    id='slider-4',
                    min=0,
                    max=5,
                    step=1,
                    value=1,
                    marks={i: str(i) for i in range(6)},
                    className='blue-slider'
                )
            ], style={'margin': '10px 0'}),
            html.Div([
                html.P("Affordability", id='affordability-label', style={'color': '#333333'}),
                dcc.Slider(
                    id='slider-5',
                    min=0,
                    max=5,
                    step=1,
                    value=1,
                    marks={i: str(i) for i in range(6)},
                    className='blue-slider'
                )
            ], style={'margin': '10px 0'})
        ], className='rounded-box', style={'width': '45%', 'padding': '20px', 'backgroundColor': 'rgb(225, 225, 225)', 'borderRadius': '10px', 'margin': '10px'})
    ], className='main-container', style={'display': 'flex', 'flexDirection': 'row', 'justifyContent': 'center', 'width': '100%'}),
    
    html.Div([
        html.H3("City Scores Table", id='city-scores-title', style={'textAlign': 'center', 'color': '#333333'}),
        html.Table(id='city-scores-table', style={'width': '100%', 'textAlign': 'center', 'color': '#333333', 'backgroundColor': '#ffffff', 'border': '1px solid #ccc', 'borderRadius': '5px', 'margin': '10px'})
    ], style={'width': 'calc(100% - 40px)', 'padding': '20px', 'backgroundColor': 'rgb(193, 193, 193)', 'boxSizing': 'border-box', 'borderRadius': '10px', 'margin': '10px'})
], style={'backgroundColor': 'rgb(209, 209, 209)', 'fontFamily': 'Arial, sans-serif', 'boxSizing': 'border-box', 'padding': '0', 'margin': '0', 'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'})

@app.callback(
    Output('map', 'figure'),
    [Input('slider-1', 'value'),
     Input('slider-2', 'value'),
     Input('slider-3', 'value'),
     Input('slider-4', 'value'),
     Input('slider-5', 'value')]
)
def update_map(weight1, weight2, weight3, weight4, weight5):
    df['WeightedAvg'] = (weight1 * df['Environment'] + 
                         weight2 * df['Society'] + 
                         weight3 * df['Access'] + 
                         weight4 * df['Prospect'] + 
                         weight5 * df['Affordability'])

    fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size="WeightedAvg", 
                            hover_name="City", 
                            mapbox_style="carto-positron", 
                            size_max=15, zoom=3,
                            color_discrete_sequence=px.colors.qualitative.Dark2)
    
    fig.update_layout(
        autosize=False,
        width=600,
        height=600
    )

    return fig

@app.callback(
    Output('city-value', 'children'),
    [Input('city-dropdown', 'value')]
)
def update_city_value(selected_city):
    city_data = df[df['City'] == selected_city]
    return html.Div([
        html.H4(f"{selected_city}", style={'color': '#333333'}),
        html.P(f"Environment: {city_data['Environment'].values[0]}", style={'color': '#333333'}),
        html.P(f"Society: {city_data['Society'].values[0]}", style={'color': '#333333'}),
        html.P(f"Access: {city_data['Access'].values[0]}", style={'color': '#333333'}),
        html.P(f"Prospect: {city_data['Prospect'].values[0]}", style={'color': '#333333'}),
        html.P(f"Affordability: {city_data['Affordability'].values[0]}", style={'color': '#333333'})
    ])

@app.callback(
    Output('city-dropdown', 'value'),
    Input('map', 'clickData')
)
def update_city_from_map(clickData):
    if clickData is None:
        return dash.no_update
    return clickData['points'][0]['hovertext']

@app.callback(
    Output('city-rank', 'children'),
    [Input('slider-1', 'value'),
     Input('slider-2', 'value'),
     Input('slider-3', 'value'),
     Input('slider-4', 'value'),
     Input('slider-5', 'value')]
)
def update_city_rank(weight1, weight2, weight3, weight4, weight5):
    df['WeightedAvg'] = (weight1 * df['Environment'] + 
                         weight2 * df['Society'] + 
                         weight3 * df['Access'] + 
                         weight4 * df['Prospect'] + 
                         weight5 * df['Affordability'])
    
    ranked_cities = df.sort_values(by='WeightedAvg', ascending=False)['City']
    return html.Ul([html.Li(f"{i + 1}. {city}", style={'color': '#333333'}) for i, city in enumerate(ranked_cities)])

@app.callback(
    Output('city-scores-table', 'children'),
    [Input('slider-1', 'value'),
     Input('slider-2', 'value'),
     Input('slider-3', 'value'),
     Input('slider-4', 'value'),
     Input('slider-5', 'value'),
     Input('language-switch', 'n_clicks')]
)
def update_city_scores_table(weight1, weight2, weight3, weight4, weight5, n_clicks):
    df['WeightedAvg'] = (weight1 * df['Environment'] + 
                         weight2 * df['Society'] + 
                         weight3 * df['Access'] + 
                         weight4 * df['Prospect'] + 
                         weight5 * df['Affordability'])

    sorted_df = df.sort_values(by='WeightedAvg', ascending=False)

    if n_clicks % 2 == 1:
        headers = ["Ville", "Environnement", "Société", "Accès", "Perspectives", "Abordabilité", "Moyenne Pondérée"]
    else:
        headers = ["City", "Environment", "Society", "Access", "Prospect", "Affordability", "Weighted Avg"]

    header = html.Tr([html.Th(col) for col in headers])

    rows = [html.Tr([
        html.Td(sorted_df.iloc[i]['City']),
        html.Td(sorted_df.iloc[i]['Environment']),
        html.Td(sorted_df.iloc[i]['Society']),
        html.Td(sorted_df.iloc[i]['Access']),
        html.Td(sorted_df.iloc[i]['Prospect']),
        html.Td(sorted_df.iloc[i]['Affordability']),
        html.Td(sorted_df.iloc[i]['WeightedAvg'])
    ]) for i in range(len(sorted_df))]

    table = [header] + rows

    return table

@app.callback(
    [Output('city-value-title', 'children'),
     Output('city-rank-title', 'children'),
     Output('weights-title', 'children'),
     Output('environment-label', 'children'),
     Output('society-label', 'children'),
     Output('access-label', 'children'),
     Output('prospects-label', 'children'),
     Output('affordability-label', 'children'),
     Output('city-scores-title', 'children'),
     Output('language-switch', 'children')],
    [Input('language-switch', 'n_clicks')]
)
def update_language(n_clicks):
    if n_clicks % 2 == 1:
        return ["Valeur de la ville", "Classement des villes", "Poids", "Environnement", "Société", "Accès", "Perspectives", "Abordabilité", "Tableau des scores des villes", "SWITCH TO ENGLISH"]
    else:
        return ["City Value", "City Rank", "Weights", "Environment", "Society", "Access", "Prospects", "Affordability", "City Scores Table", "SWITCH TO FRENCH"]

if __name__ == '__main__':
    app.run_server(debug=True)
