import unittest
import numpy as np
import pandas as pd

    
# Task 1: NumPy Basics
def test_numpy_array_creation(arr):
    expected = np.array([0, 0, 0, 0, 1, 0, 0, 0, 0, 0])
    np.testing.assert_array_equal(arr, expected)

def test_numpy_matrix_creation(matrix):
    expected = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
    np.testing.assert_array_equal(matrix, expected)

def test_numpy_operations(arr1, arr2):
    np.testing.assert_array_equal(arr1 + arr2, np.array([5, 7, 9]))
    np.testing.assert_array_equal(arr1 - arr2, np.array([-3, -3, -3]))
    np.testing.assert_array_equal(arr1 * arr2, np.array([4, 10, 18]))
    np.testing.assert_array_equal(arr1 / arr2, np.array([0.25, 0.4, 0.5]))

def test_numpy_slicing(sliced):
    expected = np.array([30, 40, 50, 60, 70])
    np.testing.assert_array_equal(sliced, expected)

# Task 2: Pandas Basics
def test_pandas_series_creation(series):
    assert series['a'] == 10
    assert series['e'] == 50

def test_dataframe_reading_and_manipulation(df):
    df['Tax'] = df['Salary'] * 0.1
    assert df.loc[0, 'Tax'] == 5000
    assert df.loc[1, 'Tax'] == 6000
    filtered_df = df[df['Age'] > 36]
    assert len(filtered_df) == 1
    assert filtered_df.iloc[0]['Name'] == "Bob"

def test_dataframe_aggregation(sales_data):
    total_sales = sales_data.groupby("Region")["Sales"].sum()
    assert total_sales["North"] == 2200
    assert total_sales["South"] == 1500

def test_dataframe_merging(customers, orders):
    merged = pd.merge(customers, orders, on="CustomerID")
    assert len(merged) == 2
    assert "OrderID" in merged.columns

def test_dataframe_pivot_table(sales_data):
    pivot_table = sales_data.pivot_table(values="Sales", index="Region", columns="Product", aggfunc="sum")
    assert pivot_table.loc["North", "A"] == 2200
    assert pivot_table.loc["South", "B"] == 1500

if __name__ == "__main__":
    unittest.main()