import pylightxl


def xlsx_reader(path, sheet_index=0):
    db = pylightxl.readxl(fn=path)
    try:
        sheet = db.ws(ws=db.ws_names[sheet_index])
    except IndexError:
        return []

    for row in sheet.rows:
        yield row



def xlsx_dict_reader(*args, **kwargs):
    r = xlsx_reader(*args, **kwargs)
    keys = next(r)
    for row in r:
        yield dict(zip(keys, row))
