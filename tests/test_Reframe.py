from reframe import Relation
import pandas as pd
import pytest

def outer_join():
    pass

@pytest.fixture(scope="session", autouse=True)
#python -m pytest tests/test_Reframe.py
def test_groupby():
    dbReal01 = {"name" : ["Carol", "Bob"], "age" : [86, 4]}
    dbReal02 = {"name" : ["Earl", "Bob"], "age" : [43, 4]}

    dExpected = {"name" : ["Carol", "Bob"], "age" : [86, 4]}

    df01 = pd.DataFrame(data=dbReal01)
    df02 = pd.DataFrame(data=dbReal02)

    df01Expected = pd.DataFrame(data=dExpected)

    r = Relation(df01)
    rpro = r.project(["name"])
    assert r.equals(rpro)