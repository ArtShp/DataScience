import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
pd.set_option('display.max_rows', None)

data = pd.read_csv('../../datasets/COVID-19.csv')

data[['Confirmed', 'Deaths', 'Recovered']] = data[['Confirmed', 'Deaths', 'Recovered']].astype(int)
data['Country/Region'] = data['Country/Region'].replace('Mainland China', 'China')
data['Active_cases'] = data['Confirmed'] - data['Deaths'] - data['Recovered']

dataBelarus = data[(data['Country/Region'] == 'Belarus')].reset_index(drop=True)
dataBelarus_op = dataBelarus.groupby(['ObservationDate', 'Country/Region'])[
    ['Confirmed', 'Deaths', 'Recovered', 'Active_cases']
].sum().reset_index().reset_index(drop=True)


figure = go.Figure()

# Подтверждённые
figure.add_trace(go.Scatter(x=dataBelarus_op['ObservationDate'],
                            y=dataBelarus_op['Confirmed'],
                            mode='lines+text',
                            name='Confirmed cases COVID',
                            )
                 )

figure.add_annotation(
    x='03/19/2020',
    y=dataBelarus_op['Confirmed'].max(),
    text='COVID Lockdown in Belarus',
    font=dict(size=16, color='red')
)

figure.add_shape(
    # Вертикальная линия
    dict(
        type='line',
        x0='03/19/2020',
        y0=dataBelarus_op['Confirmed'].max(),
        x1='03/19/2020',
        line=dict(
            color='red',
            width=5
        )
    )
)

###########

figure.add_annotation(
    x='04/19/2020',
    y=dataBelarus_op['Confirmed'].max(),
    text='Month after lockdown',
    font=dict(size=16, color='green')
)

figure.add_shape(
    # Вертикальная линия
    dict(
        type='line',
        x0='04/19/2020',
        y0=dataBelarus_op['Confirmed'].max()-30000,
        x1='04/19/2020',
        line=dict(
            color='green',
            width=5
        )
    )
)


# Активные случаи
figure.add_trace(go.Scatter(x=dataBelarus_op['ObservationDate'],
                            y=dataBelarus_op['Active_cases'],
                            mode='lines+text',
                            name='Active cases COVID',
                            marker_color='rgb(153,58,204)',
                            )
                 )


# Смертельные случаи
figure.add_trace(go.Scatter(x=dataBelarus_op['ObservationDate'],
                            y=dataBelarus_op['Deaths'],
                            mode='lines+text',
                            name='Deaths cases COVID',
                            marker_color='rgb(0,0,0)',
                            )
                 )

# Выздоровевшие случаи
figure.add_trace(go.Scatter(x=dataBelarus_op['ObservationDate'],
                            y=dataBelarus_op['Recovered'],
                            mode='lines+text',
                            name='Recovered cases COVID',
                            marker_color='rgb(204,255,0)',
                            )
                 )

figure.update_layout(title='Evolution of Confirmed, Active cases in Belarus', template='plotly_white')

figure.show()
