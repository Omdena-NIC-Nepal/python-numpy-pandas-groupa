import numpy as np
import pandas as pd

# Test function for numpy
def test_numpy_exercises():
    # Test 1: Create an array of 10 zeros with the fifth element set to 1
    arr = np.zeros(10, dtype=int)
    arr[4] = 1
    assert np.array_equal(arr, np.array([0, 0, 0, 0, 1, 0, 0, 0, 0, 0])), "Test 1 Failed"

    # Test 2:
    arr_matrix = np.arange(16).reshape(4, 4)
    assert np.array_equal(arr_matrix, np.arange(16).reshape(4, 4)), "Test 2 Failed"

    # Test 3: Creating an Array
    arr1 = np.arange(1, 11)
    assert np.array_equal(arr1, np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), "Test 3 Failed"

    # Test 4: Array Operations
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([10, 20, 30, 40, 50])
    
    assert np.array_equal(a + b, np.array([11, 22, 33, 44, 55])), "Test 4 Addition Failed"
    assert np.array_equal(a - b, np.array([-9, -18, -27, -36, -45])), "Test 4 Subtraction Failed"
    assert np.array_equal(a * b, np.array([10, 40, 90, 160, 250])), "Test 4 Multiplication Failed"
    assert np.array_equal(a / b, np.array([0.1, 0.1, 0.1, 0.1, 0.1])), "Test 4 Division Failed"

    # Test 5: Array Slicing
    arr2 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    sliced = arr2[2:7]  # index 2 to 6
    assert np.array_equal(sliced, np.array([30, 40, 50, 60, 70])), "Test 5 Failed"

    # Test 6: NumPy Methods
    arr3 = np.random.randint(1, 50, (3, 3))
    mean_value = arr3.mean()
    sum_value = arr3.sum()
    max_value = arr3.max()
    
    assert isinstance(mean_value, (float, np.floating)), "Test 6 Mean Failed"
    assert isinstance(sum_value, (int, np.integer)), "Test 6 Sum Failed"
    assert isinstance(max_value, (int, np.integer)), "Test 6 Max Failed"

    print("All tests passed successfully!")


# Test function for pandas
def test_pandas_exercises():
    try:
        # Test Exercise 1: Creating Pandas Series
        series = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
        assert isinstance(series, pd.Series), "Exercise 1 Failed: Not a Pandas Series"
        assert list(series.values) == [10, 20, 30, 40, 50], "Exercise 1 Failed: Values mismatch"

        # Test Exercise 2: Reading CSV File
        df = pd.DataFrame({
            "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
            "Age": [25, 32, 40, 28, 50],
            "Salary": [50000, 60000, 75000, 55000, 90000]
        })
        assert isinstance(df, pd.DataFrame), "Exercise 2 Failed: Not a DataFrame"

        # Test Exercise 3: Slicing DataFrame
        sliced_df = df.iloc[:3]
        assert sliced_df.shape[0] == 3, "Exercise 3 Failed: Incorrect number of rows"

        # Test Exercise 4: Adding a Column (Tax Calculation)
        df["Tax"] = df["Salary"] * 0.1
        assert "Tax" in df.columns, "Exercise 4 Failed: Column 'Tax' not added"
        assert np.isclose(df["Tax"][0], 5000.0), "Exercise 4 Failed: Incorrect Tax Calculation"

        # Test Exercise 5: Filtering Data
        filtered_df = df[df["Age"] > 30]
        assert all(filtered_df["Age"] > 30), "Exercise 5 Failed: Incorrect filtering"

        print("All exercises passed successfully! ✅")

    except AssertionError as e:
        print(e)

# Run the test script
test_numpy_exercises()


# Run the test function
test_pandas_exercises()