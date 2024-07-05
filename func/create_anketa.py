import shutil
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows

from .miacbase_sql import base_sql


def create_anketa(oid: str) -> str:

    DICT = {
        "Отделения": ("otdelenia_vrachi", 3, 1),
    }
    DATA = {}

    SQL = open("func/sql/otdelenia_vrachi.sql", "r").read()
    SQL = SQL.replace("__OID__", oid)
    DATA["otdelenia_vrachi"] = base_sql(SQL)

    file_path = "/tmp/test_excel.xlsx"
    shutil.copyfile("func/organization_report.xlsx", file_path)

    wb = openpyxl.load_workbook(file_path)

    for key, value in DICT.items():
        ws = wb[key]
        print(value)
        rows = dataframe_to_rows(DATA[value[0]], index=False, header=False)
        for r_idx, row in enumerate(rows, int(value[1])):
            for c_idx, val in enumerate(row, int(value[2])):
                ws.cell(row=r_idx, column=c_idx, value=val)

    wb.save(file_path)

    return file_path
