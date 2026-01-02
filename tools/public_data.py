import pandas as pd

def load_public_csv():
    url = "https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv"
    df = pd.read_csv(url)

    df = df.rename(columns={
        "Population": "value",
        "State": "entity"
    })

    return df[["entity", "value"]]
