import json
from fastapi import APIRouter, File, UploadFile
import pandas as pd

router = APIRouter()

@router.post("/convert_csv/")
async def convert_excel_to_json(file: UploadFile = File(...)):
    try:
        # Download the CSV file
        df = pd.read_csv(file.file)

        # create a dictionary to hold the data
        data_dict = {}

        # loop through the columns of the dataframe
        for col in df.columns:
            # add the column data to the dictionary
            data_dict[col] = df[col].tolist()
            print(df[col].tolist())

        # create the final dictionary with the "data" key
        final_dict = {"data": data_dict}

        # convert the dictionary to JSON with ensure_ascii=False
        json_data = json.dumps(final_dict, ensure_ascii=False)

        # replace all instances of NaN with null in the JSON string
        json_data = json_data.replace("NaN", "null")

        return json.loads(json_data)
    except Exception as e:
        print(e)
        return {"error": "Internal server error"}
