import os

from recycle import xlsx_utils


DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')


def test_xlsx_reader():
    path = os.path.join(DATA_DIR, 'test.xlsx')
    data = list(xlsx_utils.xlsx_reader(path))
    assert len(data) == 5
    assert list(data[0]) == ['a', 'b', 'c', 'd']
    assert data[1][0] == 1
    assert data[4][3] == 'fourth'

    data = list(xlsx_utils.xlsx_reader(path, sheet_index=1))
    assert data == []


def test_xlsx_dict_reader():
    path = os.path.join(DATA_DIR, 'test.xlsx')
    data = list(xlsx_utils.xlsx_dict_reader(path))

    assert list(data[0].keys()) == ['a', 'b', 'c', 'd']
    assert len(data) == 4
    assert data[0]['a'] == 1
    assert data[3]['d'] == 'fourth'
