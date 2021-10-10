import xlrd


def xls_reader(path, sheet_index=0):
    wb = xlrd.open_workbook(path)
    try:
        sheet = wb.sheet_by_index(sheet_index)
    except IndexError:
        return []

    row_idx = -1
    while True:
        row_idx += 1
        try:
            row = sheet.row_values(row_idx)
        except IndexError:
            break

        yield row


def xls_dict_reader(*args, **kwargs):
    r = xls_reader(*args, **kwargs)
    keys = next(r)
    for row in r:
        yield dict(zip(keys, row))
