import pandas as pd
from xsmb.config import REGION_CODE

def filter_region(data, region_code=REGION_CODE):
    return [
        item
        for item in data
        if item["province"]["region"]["code"] == region_code
    ]

def to_dataframe(data, seven_day=7):
    data = sorted(
        data,
        key=lambda item: item["formatted_date"],
        reverse=True
    )

    # Take the latest 7 records
    data = data[:seven_day]

    rows = []

    for item in data:
        row = {
            "description": item["province"]["region"]["description"],
            "formatted_date": item["formatted_date"]
        }

        for result in item["results"]:
            prize = result["prizeCode"]
            values = result["values"]
            row[prize] = ", ".join(values)

        rows.append(row)

    return pd.DataFrame(rows)


