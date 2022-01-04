import openpyxl


def xlsx_reader(path, sheet_index=0):
    wb = openpyxl.load_workbook(filename=path, read_only=True)
    try:
        sheet = wb[wb.sheetnames[sheet_index]]
    except IndexError:
        return []

    for values in sheet.values:
        yield values


def xlsx_dict_reader(*args, **kwargs):
    r = xlsx_reader(*args, **kwargs)
    keys = next(r)
    for row in r:
        yield dict(zip(keys, row))
