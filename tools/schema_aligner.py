import pandas as pd

def align_datasets(github_data, csv_data):
    df_git = pd.DataFrame(github_data)
    df_git["value"] = df_git["stars"]

    df_git = df_git[["created_at", "value"]]
    df_git = df_git.rename(columns={"created_at": "year"})

    df_csv = csv_data.copy()
    df_csv["year"] = 2014  # inferred year
    df_csv = df_csv[["year", "value"]]

    combined = pd.concat([df_git, df_csv], ignore_index=True)
    combined["value"] = combined["value"].fillna(combined["value"].mean())

    return combined
