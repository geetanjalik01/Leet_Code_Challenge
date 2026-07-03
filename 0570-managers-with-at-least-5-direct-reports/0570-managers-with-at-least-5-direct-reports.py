import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    manager_ids = employee["managerId"].value_counts()
    manager_ids = manager_ids[manager_ids >= 5].index

    return employee[employee["id"].isin(manager_ids)][["name"]]