import requests
import json
import pandas as pd


def get_nsi_requests(dictionary, mo_oid: str, attributes: list, columns: list):
    atr = {
        "tag": "dictionary_item",
        "id_dictionary": dictionary,
        "attributes": attributes,
        "regime": "data",
        "count": 1000,
        "page": 1,
        "filter": [
            {"field": "mo_oid", "value": f" = '{mo_oid}'"},
        ],
    }

    data = {"data": json.dumps(atr), "guid": ""}
    URL = "http://10.128.66.207:2226/nsiui/Api/Grid"
    req = requests.post(URL, json=data, verify=False)

    if req.status_code == 200:
        response_data = req.json().get("response", {}).get("data", [])
        if not response_data:
            return pd.DataFrame(columns=columns)
        df = pd.DataFrame(data=response_data, columns=columns)
        return df
    else:
        print(f"Failed to retrieve data. Status code: {req.status_code}")
        print(req.text)
        print(atr)
        return None


def get_combined_df(mo_oid: str):
    try:
        # Первый запрос
        dictionary1 = 215
        attributes1 = ["code", "depart_type_name", "depart_kind_name"]
        columns1 = [
            "Идентификатор здания из ФРМО",
            "OID структурного подразделения",
            "Тип структурного подразделения",
            "Вид структурного подразделения",
        ]
        df1 = get_nsi_requests(dictionary1, mo_oid, attributes1, columns1)

        # Второй запрос
        dictionary2 = 989
        attributes2 = ["code", "depart_name"]
        columns2 = [
            "Идентификатор отделения из ФРМО",
            "OID отделения стационара",
            "Полное наименование отделения стационара",
        ]
        df2 = get_nsi_requests(dictionary2, mo_oid, attributes2, columns2)

        if df1 is None or df2 is None:
            return pd.DataFrame()

        # Обработка второго DataFrame
        df2["OID структурного подразделения"] = df2[
            "OID отделения стационара"
        ].str.rsplit(pat=".", n=1, expand=True)[0]

        # Объединение DataFrame
        df = df1.merge(df2, how="outer", on="OID структурного подразделения")

        # Удаление ненужной колонки
        # try:
        #    del df["Идентификатор отделения из ФРМО"]
        # except ValueError:
        #    pass

        return df

    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame()
