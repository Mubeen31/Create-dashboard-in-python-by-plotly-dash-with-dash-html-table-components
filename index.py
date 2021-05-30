import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import dash_table as dt
import pathlib


PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("./data").resolve()

data2 = pd.read_csv(DATA_PATH.joinpath('update.csv'))

year_list = list(data2['year'].unique())

font_awesome = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
meta_tags = [{"name": "viewport", "content": "width=device-width"}]
external_stylesheets = [meta_tags, font_awesome]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

app.layout = html.Div([
html.Div([
        html.Div([
            html.Div([
                html.H5('Movies Data Analyzer', className = 'title_text'),
            ])
        ], className = "title_container twelve columns")
    ], className = "row flex-display"),

html.Div([
        html.Div([
            html.Div([
                html.P(dcc.Markdown(
                    '''
                     **Below table** shows gross sales **values** for each genre category and **percentage** of share 
                     for each genre category in **each year**.
                    '''),
                       style = {'line-height': '1', 'text-align': 'justify', 'font-size': '17px',
                                'margin-bottom': '20px'}),
                html.Div(id = 'calculations'),
            ], className = 'container_no_border'),
            html.Div([
                dcc.Graph(id = 'bar_chart',
                          config = {'displayModeBar': 'hover'}),
            ], className = 'container_with_border')

        ], className = "create_container2 six columns", style = {'margin-bottom': '10px', "margin-top": "10px"}),


    html.Div([
            html.Div([
             html.P('Year:', className = 'fix_label', style = {'color': 'black', 'margin-top': '15px'}),
             dcc.Slider(id = 'select_years',
                        included = False,
                        tooltip = {'always_visible': True},
                        min = year_list[0],
                        max = year_list[-1],
                        step = 1,
                        updatemode='drag',
                        value = year_list[6],
                        marks = {str(yr): str(yr) for yr in range(year_list[0], year_list[-1], 2)},
                        className = 'slider_compon'),

             ], className = 'container_slider'),
            html.Div([
             dcc.Graph(id = 'pie_chart',
                       config = {'displayModeBar': 'hover'}),

             ], className = 'container_pie_chart'),

            html.P(dcc.Markdown(
                    '''
                     Percentage **share** of each **rated category** in each **year**.
                    '''), style = {'line-height': '1', 'text-align': 'justify', 'font-size': '17px',
                                   'margin-top': '30px'}),


html.Div([
            html.Div([
              html.Div(id = 'text1'),
                     ], className = 'container_no_border_text1'),

            html.Div([
              html.Div(id = 'text2'),
                     ], className = 'container_no_border_text2'),
            html.Div([
              html.Div(id = 'text3'),
                     ], className = 'container_no_border_text3'),
            html.Div([
              html.Div(id = 'text4'),
                     ], className = 'container_no_border_text4'),
            html.Div([
              html.Div(id = 'text5'),
                     ], className = 'container_no_border_text5')
], className = 'container_text_with_border')

        ], className = "create_container2 six columns", style = {'margin-bottom': '10px', "margin-top": "10px"}),

    ], className = "row flex-display")

], id= "mainContainer", style={"display": "flex", "flex-direction": "column"})

@app.callback(Output('calculations', 'children'),
             [Input('select_years', 'value')])

def update_table(select_years):
    data3 = data2.groupby(['genre', 'year'])['total_gross'].sum().reset_index()
    data4 = data3[(data3['genre'] == 'Musical') & (data3['year'] == select_years)]['total_gross'].sum()
    data5 = data3['total_gross'].sum()
    data6 = (data4 / data5) * 100

    data7 = data3[(data3['genre'] == 'Comedy') & (data3['year'] == select_years)]['total_gross'].sum()
    data8 = data3['total_gross'].sum()
    data9 = (data7 / data8) * 100

    data10 = data3[(data3['genre'] == 'Adventure') & (data3['year'] == select_years)]['total_gross'].sum()
    data11 = data3['total_gross'].sum()
    data12 = (data10 / data11) * 100

    data13 = data3[(data3['genre'] == 'Romantic Comedy') & (data3['year'] == select_years)]['total_gross'].sum()
    data14 = data3['total_gross'].sum()
    data15 = (data13 / data14) * 100

    data16 = data3[(data3['genre'] == 'Western') & (data3['year'] == select_years)]['total_gross'].sum()
    data17 = data3['total_gross'].sum()
    data18 = (data16 / data17) * 100

    data19 = data3[(data3['genre'] == 'Action') & (data3['year'] == select_years)]['total_gross'].sum()
    data20 = data3['total_gross'].sum()
    data21 = (data19 / data20) * 100

    data22 = data3[(data3['genre'] == 'Drama') & (data3['year'] == select_years)]['total_gross'].sum()
    data23 = data3['total_gross'].sum()
    data24 = (data22 / data23) * 100

    data25 = data3[(data3['genre'] == 'Thriller/Suspense') & (data3['year'] == select_years)]['total_gross'].sum()
    data26 = data3['total_gross'].sum()
    data27 = (data25 / data26) * 100

    data28 = data3[(data3['genre'] == 'Black Comedy') & (data3['year'] == select_years)]['total_gross'].sum()
    data29 = data3['total_gross'].sum()
    data30 = (data28 / data29) * 100

    data31 = data3[(data3['genre'] == 'Documentary') & (data3['year'] == select_years)]['total_gross'].sum()
    data32 = data3['total_gross'].sum()
    data33 = (data31 / data32) * 100

    data34 = data3[(data3['genre'] == 'Horror') & (data3['year'] == select_years)]['total_gross'].sum()
    data35 = data3['total_gross'].sum()
    data36 = (data34 / data35) * 100

    data37 = data3[(data3['genre'] == 'Concert/Performance') & (data3['year'] == select_years)]['total_gross'].sum()
    data38 = data3['total_gross'].sum()
    data39 = (data37 / data38) * 100


    return [

               html.Table([
                   html.Thead(
                       html.Tr([
                           html.Th('Genre'),
                           html.Th('Symbol'),
                           html.Th('Gross Sales ($):' + '  ' + '{0:.0f}'.format(select_years)),
                           html.Th('% Share:' + '  ' + '{0:.0f}'.format(select_years))
                       ], className = 'header_hover')
                   ),
                   html.Tbody([
                       html.Tr([
                           html.Td('Musical'),
                           html.Td(html.I(className = "fa fa-music", style = {"font-size": "150%"})),
                           html.Td('{0:,.0f}'.format(data4)),
                           html.Td('{0:,.2f}%'.format(data6)),
                       ], className = 'hover_only_row'),
                       html.Tr([
                           html.Td('Comedy'),
                           html.Td(html.I(className = "fa fa-theater-masks", style = {"font-size": "150%"})),
                           html.Td('{0:,.0f}'.format(data7)),
                           html.Td('{0:,.2f}%'.format(data9)),
                       ], className = 'hover_only_row'),
                       html.Tr([
                           html.Td('Adventure'),
                           html.Td(html.I(className = "fa fa-tree", style = {"font-size": "150%"})),
                           html.Td('{0:,.0f}'.format(data10)),
                           html.Td('{0:,.2f}%'.format(data12)),
                       ], className = 'hover_only_row'),
                       html.Tr([
                           html.Td('Romantic Comedy'),
                           html.Td(html.I(className = "fa fa-theater-masks", style = {"font-size": "150%"})),
                           html.Td('{0:,.0f}'.format(data13)),
                           html.Td('{0:,.2f}%'.format(data15)),
                       ], className = 'hover_only_row'),
                       html.Tr([
                           html.Td('Western'),
                           html.Td(html.I(className = "fa fa-child", style = {"font-size": "150%"})),
                           html.Td('{0:,.0f}'.format(data16)),
                           html.Td('{0:,.2f}%'.format(data18)),
                       ], className = 'hover_only_row'),
                       html.Tr([
                           html.Td('Action'),
                           html.Td(html.I(className = "fa fa-air-freshener", style = {"font-size": "150%"})),
                           html.Td('{0:,.0f}'.format(data19)),
                           html.Td('{0:,.2f}%'.format(data21)),
                       ], className = 'hover_only_row'),
                       html.Tr([
                           html.Td('Drama'),
                           html.Td(html.I(className = "fa fa-house-damage", style = {"font-size": "150%"})),
                           html.Td('{0:,.0f}'.format(data22)),
                           html.Td('{0:,.2f}%'.format(data24)),
                       ], className = 'hover_only_row'),
                       html.Tr([
                           html.Td('Thriller/Suspense'),
                           html.Td(html.I(className = "fa fa-skull", style = {"font-size": "150%"})),
                           html.Td('{0:,.0f}'.format(data25)),
                           html.Td('{0:,.2f}%'.format(data27)),
                       ], className = 'hover_only_row'),
                       html.Tr([
                           html.Td('Black Comedy'),
                           html.Td(html.I(className = "fa fa-theater-masks", style = {"font-size": "150%"})),
                           html.Td('{0:,.0f}'.format(data28)),
                           html.Td('{0:,.2f}%'.format(data30)),
                       ], className = 'hover_only_row'),
                       html.Tr([
                           html.Td('Documentary'),
                           html.Td(html.I(className = "fa fa-book", style = {"font-size": "150%"})),
                           html.Td('{0:,.0f}'.format(data31)),
                           html.Td('{0:,.2f}%'.format(data33)),
                       ], className = 'hover_only_row'),
                       html.Tr([
                           html.Td('Horror'),
                           html.Td(html.I(className = "fa fa-skull-crossbones", style = {"font-size": "150%"})),
                           html.Td('{0:,.0f}'.format(data34)),
                           html.Td('{0:,.2f}%'.format(data36)),
                       ], className = 'hover_only_row'),
                       html.Tr([
                           html.Td('Concert/Performance'),
                           html.Td(html.I(className = "fa fa-user-ninja", style = {"font-size": "150%"})),
                           html.Td('{0:,.0f}'.format(data37)),
                           html.Td('{0:,.2f}%'.format(data39)),
                       ], className = 'hover_only_row'),
                   ])
               ], className = 'table_style')

    ]

@app.callback(Output('bar_chart', 'figure'),
              [Input('select_years', 'value')])

def update_graph(select_years):
    data3 = data2.groupby(['genre', 'year'])['total_gross'].sum().reset_index()
    data4 = data3[data3['year'] == select_years]

    return {
        'data':[
            go.Bar(
                x = data4['genre'],
                y = data4['total_gross'],
                text = data4['total_gross'],
                texttemplate = '%{text:,.2s}',
                textposition = 'outside',
                marker = dict(color = '#38D56F'),
                textfont = dict(
                    family = "sans-serif",
                    size = 12,
                    color = 'black'),

                hoverinfo = 'text',
                hovertext =
                '<b>Year</b>: ' + data4['year'].astype(str) + '<br>' +
                '<b>Gross Sales</b>: $' + [f'{x:,.0f}' for x in data4['total_gross']] + '<br>'

            )],


        'layout': go.Layout(
             plot_bgcolor='white',
             paper_bgcolor='white',
             title={
                'text': '<b>Gross Sales ($) in' + ' ' + str((select_years)),

                'y': 0.98,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
             titlefont={
                        'color': 'black',
                        'size': 17},

             hovermode='closest',
             margin = dict(t = 30, r = 0),

             xaxis = dict(title = '<b></b>',
                          visible = True,
                          color = 'black',
                          showline = True,
                          showgrid = False,
                          showticklabels = True,
                          linecolor = 'black',
                          linewidth = 1,
                          ticks = 'outside',
                          tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'black')

                          ),

             yaxis = dict(title = '<b>Gross Sales ($)</b>',
                          visible = True,
                          color = 'black',
                          showline = False,
                          showgrid = True,
                          showticklabels = True,
                          linecolor = 'black',
                          linewidth = 1,
                          ticks = '',
                          tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'black')

                         ),

             legend = {
                'orientation': 'h',
                'bgcolor': '#1f2c56',
                'x': 0.5,
                'y': 1.25,
                'xanchor': 'center',
                'yanchor': 'top'},

             font = dict(
                family = "sans-serif",
                size = 12,
                color = 'white'),

        )

    }

@app.callback(Output('pie_chart', 'figure'),
              [Input('select_years', 'value')])
def update_graph(select_years):
    data3 = data2.groupby(['mpaa_rating', 'year'])['total_gross'].sum().reset_index()
    data4 = data3[data3['year'] == select_years]

    return {
        'data': [go.Pie(labels = data4['mpaa_rating'],
                        values = data4['total_gross'],
                        hoverinfo = 'label+value+percent',
                        textinfo = 'label+value',
                        textfont = dict(size = 13),
                        texttemplate = '%{label}: %{value:,f} <br>(%{percent})',
                        textposition = 'auto',
                        rotation = 160
                        )],

        'layout': go.Layout(
            plot_bgcolor = 'white',
            paper_bgcolor = 'white',
            hovermode = 'x',
            title = {
                'text': '<b>Sales by rating category in' + ' ' + str((select_years)),
                'y': 0.97,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            titlefont = {
                'color': 'rgb(50, 50, 50)',
                'size': 15},
            legend = {
                'orientation': 'h',
                'bgcolor': '#F2F2F2',
                'xanchor': 'center', 'x': 0.5, 'y': -0.09},

            font = dict(
                family = "sans-serif",
                size = 12,
                color = 'rgb(50, 50, 50)')
        ),

    }

@app.callback(Output('text1', 'children'),
             [Input('select_years', 'value')])

def update_table(select_years):
    g = data2[(data2['mpaa_rating'] == 'G') & (data2['year'] == select_years)]['mpaa_rating'].count()
    r = data2[(data2['mpaa_rating'] == 'R') & (data2['year'] == select_years)]['mpaa_rating'].count()
    pg = data2[(data2['mpaa_rating'] == 'PG') & (data2['year'] == select_years)]['mpaa_rating'].count()
    pg_13 = data2[(data2['mpaa_rating'] == 'PG-13') & (data2['year'] == select_years)]['mpaa_rating'].count()
    not_rated = data2[(data2['mpaa_rating'] == 'Not Rated') & (data2['year'] == select_years)]['mpaa_rating'].count()
    total_rated = g + r + pg + pg_13 + not_rated
    g_per = (g / total_rated) * 100


    return [

               html.Table([
                   html.Tbody([
                       html.Tr([
                           html.Td('G:', className = 'style1'),
                           html.Td('{0:,.2f}%'.format(g_per) + ' ' + 'share in' + ' ' + str(select_years),
                                   className = 'style2'),
                       ]),
                   ])
               ], className = 'box_style')

    ]

@app.callback(Output('text2', 'children'),
             [Input('select_years', 'value')])

def update_table(select_years):
    g = data2[(data2['mpaa_rating'] == 'G') & (data2['year'] == select_years)]['mpaa_rating'].count()
    r = data2[(data2['mpaa_rating'] == 'R') & (data2['year'] == select_years)]['mpaa_rating'].count()
    pg = data2[(data2['mpaa_rating'] == 'PG') & (data2['year'] == select_years)]['mpaa_rating'].count()
    pg_13 = data2[(data2['mpaa_rating'] == 'PG-13') & (data2['year'] == select_years)]['mpaa_rating'].count()
    not_rated = data2[(data2['mpaa_rating'] == 'Not Rated') & (data2['year'] == select_years)]['mpaa_rating'].count()
    total_rated = g + r + pg + pg_13 + not_rated
    r_per = (r / total_rated) * 100


    return [

               html.Table([
                   html.Tbody([
                       html.Tr([
                           html.Td('R:', className = 'style1'),
                           html.Td('{0:,.2f}%'.format(r_per) + ' ' + 'share in' + ' ' + str(select_years),
                                   className = 'style2'),
                       ]),
                   ])
               ], className = 'box_style')

    ]

@app.callback(Output('text3', 'children'),
             [Input('select_years', 'value')])

def update_table(select_years):
    g = data2[(data2['mpaa_rating'] == 'G') & (data2['year'] == select_years)]['mpaa_rating'].count()
    r = data2[(data2['mpaa_rating'] == 'R') & (data2['year'] == select_years)]['mpaa_rating'].count()
    pg = data2[(data2['mpaa_rating'] == 'PG') & (data2['year'] == select_years)]['mpaa_rating'].count()
    pg_13 = data2[(data2['mpaa_rating'] == 'PG-13') & (data2['year'] == select_years)]['mpaa_rating'].count()
    not_rated = data2[(data2['mpaa_rating'] == 'Not Rated') & (data2['year'] == select_years)]['mpaa_rating'].count()
    total_rated = g + r + pg + pg_13 + not_rated
    p_g_per = (pg / total_rated) * 100


    return [

               html.Table([
                   html.Tbody([
                       html.Tr([
                           html.Td('PG:', className = 'style1'),
                           html.Td('{0:,.2f}%'.format(p_g_per) + ' ' + 'share in' + ' ' + str(select_years),
                                   className = 'style2'),
                       ]),
                   ])
               ], className = 'box_style')

    ]

@app.callback(Output('text4', 'children'),
             [Input('select_years', 'value')])

def update_table(select_years):
    g = data2[(data2['mpaa_rating'] == 'G') & (data2['year'] == select_years)]['mpaa_rating'].count()
    r = data2[(data2['mpaa_rating'] == 'R') & (data2['year'] == select_years)]['mpaa_rating'].count()
    pg = data2[(data2['mpaa_rating'] == 'PG') & (data2['year'] == select_years)]['mpaa_rating'].count()
    pg_13 = data2[(data2['mpaa_rating'] == 'PG-13') & (data2['year'] == select_years)]['mpaa_rating'].count()
    not_rated = data2[(data2['mpaa_rating'] == 'Not Rated') & (data2['year'] == select_years)]['mpaa_rating'].count()
    total_rated = g + r + pg + pg_13 + not_rated
    pg_13_per = (pg_13 / total_rated) * 100


    return [

               html.Table([
                   html.Tbody([
                       html.Tr([
                           html.Td('PG-13:', className = 'style1'),
                           html.Td('{0:,.2f}%'.format(pg_13_per) + ' ' + 'share in' + ' ' + str(select_years),
                                   className = 'style2'),
                       ]),
                   ])
               ], className = 'box_style')

    ]

@app.callback(Output('text5', 'children'),
             [Input('select_years', 'value')])

def update_table(select_years):
    g = data2[(data2['mpaa_rating'] == 'G') & (data2['year'] == select_years)]['mpaa_rating'].count()
    r = data2[(data2['mpaa_rating'] == 'R') & (data2['year'] == select_years)]['mpaa_rating'].count()
    pg = data2[(data2['mpaa_rating'] == 'PG') & (data2['year'] == select_years)]['mpaa_rating'].count()
    pg_13 = data2[(data2['mpaa_rating'] == 'PG-13') & (data2['year'] == select_years)]['mpaa_rating'].count()
    not_rated = data2[(data2['mpaa_rating'] == 'Not Rated') & (data2['year'] == select_years)]['mpaa_rating'].count()
    total_rated = g + r + pg + pg_13 + not_rated
    not_rated_per = (not_rated / total_rated) * 100


    return [

               html.Table([
                   html.Tbody([
                       html.Tr([
                           html.Td('Not Rated:', className = 'style1'),
                           html.Td('{0:,.2f}%'.format(not_rated_per) + ' ' + 'share in' + ' ' + str(select_years),
                                   className = 'style2'),
                       ]),
                   ])
               ], className = 'box_style')

    ]

if __name__ == '__main__':
    app.run_server(debug=True)