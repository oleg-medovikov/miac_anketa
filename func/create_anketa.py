import shutil
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows

from .miacbase_sql import base_sql


def create_anketa(oid: str) -> str:

    DICT = {
        "Отделения": ("otdelenia_vrachi", 3, 1),
        "Корпуса стационара": ("zdania", 3, 1),
        "Коечный фонд": ("koiki", 3, 1),
        "Медицинское оборудование": ("oborudovanie", 3, 1),
    }

    file_path = "/tmp/test_excel.xlsx"
    shutil.copyfile("func/organization_report.xlsx", file_path)

    wb = openpyxl.load_workbook(file_path)

    for key, value in DICT.items():

        SQL = open(f"func/sql/{value[0]}.sql", "r").read()
        SQL = SQL.replace("__OID__", oid)
        DF = base_sql(SQL)

        ws = wb[key]
        rows = dataframe_to_rows(DF, index=False, header=False)
        for r_idx, row in enumerate(rows, int(value[1])):
            for c_idx, val in enumerate(row, int(value[2])):
                ws.cell(row=r_idx, column=c_idx, value=val)

    wb.save(file_path)

    return file_path
