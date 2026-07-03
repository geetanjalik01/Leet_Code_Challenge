import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red_sales = (
        orders.merge(company, on="com_id")
              .loc[lambda x: x["name"] == "RED", "sales_id"]
              .unique()
    )
    return sales_person.loc[
        ~sales_person["sales_id"].isin(red_sales),
        ["name"]
    ]