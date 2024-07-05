import shutil
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows

from .miacbase_sql import base_sql


def create_anketa(oid: str) -> str:

    # начну с вкладки отделения, там где врачи
    SQL = open("func/sql/otdelenia_vrachi.sql", "r").read()
    SQL = SQL.replace("__OID__", oid)

    DF = base_sql(SQL)

    file_path = "/tmp/test_excel.xlsx"
    shutil.copyfile("func/organization_report.xlsx", file_path)

    wb = openpyxl.load_workbook(file_path)

    ws = wb["Отделения"]
    rows = dataframe_to_rows(DF, index=False, header=False)
    for r_idx, row in enumerate(rows, 3):
        for c_idx, value in enumerate(row, 1):
            ws.cell(row=r_idx, column=c_idx, value=value)

    wb.save(file_path)

    return file_path
