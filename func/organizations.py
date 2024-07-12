# организации вытаскиваем
import requests
import json

URL = "http://10.128.66.207:2226/nsiui/Api/Grid"


atr = {
    "tag": "dictionary_item",
    "id_dictionary": 64,
    "attributes": ["oid", "display"],
    "regime": "data",
    "count": 1000,
    "page": 1,
    "filter": [
        {"field": "active", "value": " LIKE '%true%'"},
        {"field": "active", "value": " LIKE '%true%'"},
        {"field": "oid", "value": " LIKE '%.13.13.12.2.78.%'"},
        {"field": "inn", "value": "IS NOT NULL"},
        {"field": "gov", "value": " NOT LIKE '%едерал%'"},
        {"field": "gov", "value": " NOT LIKE '%астн%'"},
        {"field": "gov", "value": " NOT LIKE '%бщество%'"},
        {"field": "gov", "value": " NOT LIKE '%оспотребнадзор%'"},
        {"field": "gov", "value": " NOT LIKE '%омерческие%'"},
        {"field": "gov", "value": " NOT LIKE '%социальной политике%'"},
        {"field": "gov", "value": " NOT LIKE '%инистерство%'"},
        {"field": "gov", "value": " NOT LIKE '%Российская Академия наук%'"},
    ],
}


def get_organizations() -> list:
    data = {"data": json.dumps(atr), "guid": ""}
    req = requests.post(URL, json=data, verify=False)
    list_ = req.json()["response"]["data"]

    for _ in list_:
        del _[0]
        _[1] = (
            _[1]
            .replace("Государственное бюджетное учреждение", "ГБУ")
            .replace("Общество с ограниченной ответственностью", "ООО")
            .replace(
                "Санкт-Петербургское государственное казенное учреждение здравоохранения",
                "СПб ГКУЗ",
            )
            .replace(
                "Санкт-Петербургское государственное бюджетное учреждение здравоохранения",
                "СПб ГБУЗ",
            )
            .replace("Федеральное государственное бюджетное учреждение", "ФГБУ")
            .replace(
                "Федеральное государственное бюджетное образовательное учреждение высшего образования",
                "ФГБОУВО",
            )
            .replace(
                "Санкт-Петербургское Государственное Бюджетное Стационарное Учреждение Социального Обслуживания",
                "СПб ГБСУСО",
            )
            .replace(
                "Санкт-Петербургское государственное автономное стационарное учреждение социального обслуживания",
                "СПб ГАУСУСО",
            )
            .replace(
                "Санкт-Петербургское государственное бюджетное стационарное учреждение социального обслуживания",
                "СПб ГБУСУСО",
            )
            .replace(
                "Санкт-Петербургское государственное автономное учреждение здравоохранения",
                "СПб ГАУЗ",
            )
        )

    return list_
