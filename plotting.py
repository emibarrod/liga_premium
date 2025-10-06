
import plotly.express as px
import pandas as pd

# Function to plot standings
def plot_standings(df):
    if df is not None:
        fig = px.bar(df, x='Jugador', y='Victorias', title='Clasificación de la Liga')
        return fig
    return None

# Function to plot winrate
def plot_winrate(df):
    if df is not None:
        fig = px.bar(df, x='Jugador', y='Winrate', title='Winrate de cada Jugador')
        return fig
    return None

# Function to create a table with player stats
def get_player_stats_table(df, player_name):
    if df is not None:
        player_df = df[df['Jugador'] == player_name]
        if not player_df.empty:
            stats_df = player_df[['Victorias', 'Derrotas', 'Empates', 'Partidas totales', 'Winrate', 'Puntos', 'Winrate de Oponentes']].T
            stats_df.columns = ['Estadísticas']
            return stats_df
    return None
