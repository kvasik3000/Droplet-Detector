import pandas as pd
import numpy as np
import sys
import pytest
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))  # noqa
from do_xslx import get_num, update_num, do_df, to_exel  # type: ignore  # noqa


def test_get_num():
    assert get_num() == 1


def test_update_num():
    update_num(5)
    assert get_num() == 5


def test_do_df():
    # Create mock contours
    contour1 = np.array([[0, 0], [0, 10], [10, 10]], dtype=np.int32)
    contour2 = np.array([[0, 0], [0, 5], [5, 5]], dtype=np.int32)
    contours = [contour1, contour2]
    df = do_df(contours)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(contours)
    assert "Площадь капли" in df.columns
    for i, row in df.iterrows():
        assert row.name == i
        assert isinstance(row["Площадь капли"], float)


def test_to_exel():
    data = pd.DataFrame({"A": [1, 2, 3]})
    update_num(0)
    to_exel(data)
    assert get_num() == 4


# Run the tests
pytest.main()
