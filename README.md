
# Pokemon League Standings Streamlit App

This is a Streamlit app that reads data from a Google Sheet and displays the standings of a Pokemon league.

## How to Run

1.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

2.  **Set up Google Sheets API Credentials:**

    *   Enable the Google Sheets API and Google Drive API in the [Google Cloud Console](https://console.cloud.google.com/).
    *   Create a service account and get the credentials.
    *   Create a file named `secrets.toml` inside the `.streamlit` directory.
    *   Place the credentials in the `secrets.toml` file in TOML format.
    *   Share your Google Sheet with the email address of the service account.

3.  **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

## Google Sheet Format

Your Google Sheet should have two tabs named `wins_losses` and `matches`.

### Sheet1

This tab contains the player summaries and should have the following columns:

*   `Player`: The name of the player.
*   `Wins`: The number of wins.
*   `Losses`: The number of losses.
*   `Ties`: The number of ties.

### Matches

This tab contains the match history and should have the following columns:

*   `player1`: The name of the first player.
*   `player2`: The name of the second player.
*   `winner`: The name of the winner.
