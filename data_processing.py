
import pandas as pd

# Function to process the data
def process_data(df, matches_df):
    if df is not None:
        df['Partidas totales'] = df['Victorias'] + df['Derrotas'] + df['Empates']
        df['Winrate'] = (df['Victorias'] / df['Partidas totales']).fillna(0)
        df['Puntos'] = df['Victorias'] * 3 + df['Empates'] * 1

        if matches_df is not None:
            opp_winrates = {}
            for player in df['Jugador']:
                opponents = []
                for index, row in matches_df.iterrows():
                    if row['Jugador1'] == player:
                        opponents.append(row['Jugador2'])
                    elif row['Jugador2'] == player:
                        opponents.append(row['Jugador1'])
                
                if opponents:
                    opponent_winrates_list = df[df['Jugador'].isin(opponents)]['Winrate'].tolist()
                    if opponent_winrates_list:
                        opp_winrates[player] = sum(opponent_winrates_list) / len(opponent_winrates_list)
                    else:
                        opp_winrates[player] = 0
                else:
                    opp_winrates[player] = 0
            
            df["Winrate de Oponentes"] = df['Jugador'].map(opp_winrates)

        df = df.sort_values(by='Puntos', ascending=False)
        df = df.reset_index(drop=True)
        df["Ranking"] = df.index + 1
        return df
    return None

# Function to get player's match history
def get_player_match_history(df, player_name):
    if df is not None:
        return df[((df['Jugador1'] == player_name) | (df['Jugador2'] == player_name))]
    return None
