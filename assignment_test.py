import unittest
import numpy as np
import pandas as pd

    
# Task 1: NumPy Basics
# 1.
def test_numpy_array_creation(arr):
    expected = np.array([0, 0, 0, 0, 1, 0, 0, 0, 0, 0])
    np.testing.assert_array_equal(arr, expected)

# 2.
def test_numpy_matrix_creation(matrix):
    assert matrix.shape == (4, 4), "Array shape is incorrect"
    assert 0 <= matrix.min() <= 15 and 0 <= matrix.max() <= 15, "Array values are out of bounds"

# 3.
def test_numpy_operations(addition, subtraction, division, multiplication):
    np.testing.assert_array_equal(addition, np.array([[45, 59, 12], [11, 48, 26], [47, 25, 17]]))
    np.testing.assert_array_equal(subtraction, np.array([[37,  1,  8], [ 1, 22, 20], [-1, -7,  3]]))
    np.testing.assert_array_equal(division, np.array([[10.25,  1.03448276,  5.], [1.2,  2.69230769,  7.66666667], [0.95833333,  0.5625,  1.42857143]]))
    np.testing.assert_array_equal(multiplication, np.array([[164, 870,  20], [ 30, 455,  69], [552, 144,  70]]))

# 4.
def test_numpy_slicing(sliced):
    expected = np.array([30, 40, 50, 60, 70])
    np.testing.assert_array_equal(sliced, expected)

# 5.
def test_numpy_methods(arr, add, average, max):
    
    assert arr.shape == (3, 3), "Array shape is incorrect"
    #
    expected_sum = 221
    expected_average = 24.55
    expected_max = 60
    np.testing.assert_array_equal(add, expected_sum)
    np.testing.assert_array_equal(average, expected_average)
    np.testing.assert_array_equal(max, expected_max) 

# Task 2: Pandas Basics
# 1.
def test_pandas_series_creation(series):
    assert series['a'] == 10
    assert series['e'] == 50

# 2.
def test_dataframe_reading_and_manipulation(df):
    assert df.loc[0, 'Tax'] == 7319.3
    assert df.loc[1, 'Tax'] == 8539.8
    filtered_df = df[df['Age'] > 36]
    assert len(filtered_df) == 11
    assert filtered_df.iloc[0]['Name'] == "Bob"

# 3.
def test_dataframe_aggregation(total_sales):
    assert total_sales["North"] == 2200
    assert total_sales["South"] == 2800

# 4.
def test_dataframe_merging(merged):
    assert len(merged) == 4
    assert "OrderID" in merged.columns

# 5.
def test_dataframe_pivot_table(pivot_table):
    assert pivot_table.loc["North", "A"] == 200
    assert pivot_table.loc["South", "B"] == 400

if __name__ == "__main__":
    # call the functions