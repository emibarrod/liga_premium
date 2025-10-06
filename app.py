

import streamlit as st
from google_sheets import get_data_from_sheet, get_match_history_from_sheet
from data_processing import process_data, get_player_match_history
from plotting import get_player_stats_table

# --- App Configuration ---
st.set_page_config(page_title="LIGA PREMIUM BADAJOZ", layout="wide" \
"")

# --- Main App ---
def main():
    st.title("LIGA PREMIUM BADAJOZ")

    # --- Google Sheet Name ---
    sheet_name = "liga_premium" # Replace with your sheet name

    if sheet_name:
        # --- Fetch and Process Data ---
        df = get_data_from_sheet(sheet_name)
        matches_df = get_match_history_from_sheet(sheet_name)
        processed_df = process_data(df, matches_df)

        if processed_df is not None:
            # --- Create Tabs ---
            tab1, tab2 = st.tabs(["Clasificación", "Estadísticas de Jugador"])

            with tab1:
                # --- Display League Rankings ---
                st.header("Clasificación")
                st.dataframe(processed_df[['Ranking', 'Jugador', 'Victorias', 'Derrotas', 'Empates', 'Puntos', 'Partidas totales', 'Winrate', "Winrate de Oponentes"]], hide_index=True)

            with tab2:
                # --- Player Specific Stats ---
                st.header("Estadísticas de Jugador")
                player = st.selectbox("Selecciona un Jugador", processed_df['Jugador'].unique())
                if player:
                    st.dataframe(get_player_stats_table(processed_df, player))

                    # -- Match History --
                    st.header("Historial de Partidas")
                    player_match_history = get_player_match_history(matches_df, player)
                    if player_match_history is not None and not player_match_history.empty:
                        st.dataframe(player_match_history)
                    else:
                        st.write("No se encontró historial de partidas para este jugador.")
        else:
            st.error("No se pudieron obtener o procesar los datos de la Hoja de Google. Verifique el nombre de la hoja y las credenciales.")

if __name__ == "__main__":
    main()

