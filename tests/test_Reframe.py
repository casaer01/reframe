from reframe import Relation
import pandas as pd
import pytest

#was session is now module
#@pytest.fixture(scope="module", autouse=True)

#python -m pytest tests/test_Reframe.py
NaN = float('NaN')

@pytest.fixture(scope="module")
def r():
    data_real = {"name": ["Carol", "Bob"], "age": [86, 4]}
    df = pd.DataFrame(data=data_real)
    return Relation(df)

@pytest.fixture(scope="module")
def r2():
    data_real = {"name": ["Larry", "Bob", "Lucy"], "age": [20, 4, 25]}
    df02 = pd.DataFrame(data=data_real)
    return Relation(df02)

@pytest.fixture(scope="module")
def r3():
    data_real = {"name": ["Larry", "Bob", "Lucy"], "Birthyear":[1999, 2015, 1994]}
    df03 = pd.DataFrame(data=data_real)
    return Relation(df03)

@pytest.fixture(scope="module")
def r4():
    data_real = {"Birthyear": [1999], "name": ["Larry"]}
    df04 = pd.DataFrame(data=data_real)
    return Relation(df04)

@pytest.fixture(scope="module")
def r5():
    data_real = {"Class": ["History", "Art", "Drama", "History", "Art"], "Start Time": ["10:00", "9:00", "12:00", "13:00", "18:00"]}
    df05 = pd.DataFrame(data=data_real)
    return Relation(df05)

@pytest.fixture(scope="module")
def r6():
    data_real = {"Year": [1996, 1996, 1997, 1998, 1998, 1998], "Revenue": [2000,3400,1200,500,650,200]}
    df06 = pd.DataFrame(data=data_real)
    return Relation(df06)

def test_outerjoin01(r,r2):
    data_expected = {"name": ["Carol", "Bob", "Larry", "Lucy"], "age": [86, 4, 20, 25]}
    df_expected = pd.DataFrame(data=data_expected)
    r_expected = Relation(df_expected)
    assert r.outerJoin(r2).equals(r_expected)

def test_outerjoin02(r,r3):
    data_expected = {"name": ["Carol", "Bob", "Larry", "Lucy"], "age": [86.0, 4.0, NaN, NaN],"Birthyear":[NaN, 2015.0, 1999.0, 1994.0]}
    df_expected = pd.DataFrame(data=data_expected)
    r_r3_expected = Relation(df_expected)
    assert r.outerJoin(r3).equals(r_r3_expected)

def test_outerjoin03(r,r4):
    
    data_expected = {"name" : ["Carol", "Bob", "Larry"], "age" : [86.0, 4.0, NaN], "Birthyear" :[NaN, NaN, 1999.0]}
    df_ecpected = pd.DataFrame(data=data_expected)
    r_r4_expected = Relation(df_ecpected)
    assert r.outerJoin(r4).equals(r_r4_expected)

def test_groupby01(r):
    data_expected = {"name": ["Bob", "Carol"], "count_age": [1,1]}
    df_expected = pd.DataFrame(data=data_expected)
    r_groupbyExpected = Relation(df_expected)
    assert r.groupby(["name"]).count('age').equals(r_groupbyExpected)

def test_groupby02(r5):
    data_expected = {"Class": ["Art", "Drama", "History"], "count_Start Time": [2,1,2]}
    df_expected = pd.DataFrame(data=data_expected)
    r_groupbyExpected = Relation(df_expected)
    assert r5.groupby("Class").count("Start Time").equals(r_groupbyExpected)

def test_groupby03(r6):
    data_expected = {"Year": [1996,1997,1998], "sum_Revenue": [5400,1200,1350]}
    df_expected = pd.DataFrame(data=data_expected)
    r_groupbyExpected = Relation(df_expected)
    assert r6.groupby("Year").sum("Revenue").equals(r_groupbyExpected)