import pandas as pd
from pathlib import Path

def create_folder() -> Path:
    cwd = Path.cwd()
    path_folder = cwd / "results"
    path_folder.mkdir(exist_ok=True)
    return path_folder

def save_as_csv(df: pd.DataFrame, filename: str) -> None:
    path = create_folder() / filename
    df.to_csv(path, index=False)
    print(f"File {filename} created:", path)

def save_as_xlsx(dataframes: list[pd.DataFrame], sheet_names: list[str], filename: str) -> None:
    path = create_folder() / filename
    with pd.ExcelWriter(path) as writer:
        for i in range(len(dataframes)):
            dataframes[i].to_excel(writer, sheet_name=sheet_names[i], index=False)
    print(f"File {filename} created:", path)
