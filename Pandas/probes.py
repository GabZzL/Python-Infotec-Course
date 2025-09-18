import pandas as pd

# SERIES AND DATAFRAMES
data = {
    'Integers': pd.Series([1, 2, 3], dtype='int64'),
    'Decimals': pd.Series([1.2, 2.2, 3.3], dtype='float64'),
    'Text': pd.Series(['a', 'b', 'c'], dtype='object'),
    'Boolean': pd.Series([True, False, True], dtype='bool'),
    'Date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']),
    'Categories': pd.Series(['high', 'medium', 'short'], dtype='category')
}

df = pd.DataFrame(data)

print(df)
print(df.dtypes)

# MANIPULATING SERIES
# by position
names = pd.Series(['armando', 'emilio', 'alejandro'], dtype='object')

one_name = names[0]
two_names = names[[0, 2]]

print(one_name)
print(two_names)

# data manipulation
numbers = pd.Series([10, 20, 20, None, 40, 50])

print(f'Count: {numbers.count()}')
print(f'Sum: {numbers.sum()}')
print(f'Cum Sum:\n{numbers.cumsum()}')
print(f'Value Counts:\n{numbers.value_counts()}')
print(f'Min: {numbers.min()}')
print(f'Max: {numbers.max()}')
print(f'Mean: {numbers.mean()}')
print(f'Var: {numbers.var()}')
print(f'sdt: {numbers.std()}')
print(f'Describe:\n{numbers.describe()}')

# MANIPULATING DATAFRAMES
students = {
    'Names': pd.Series(['armando', 'emilio', 'ivan'], dtype='object'),
    'Grades': pd.Series([9.9, 5.8, 8.6], dtype='float64'),
    'Pass': pd.Series([True, False, True], dtype='bool')
}

student_dt = pd.DataFrame(students)

# by position (row, column)
one_student = student_dt.iloc[1, 0]

print(one_student)

print(f'Information:\n{student_dt.info()}')
print(f'Shape: {student_dt.shape}')
print(f'Columns: {student_dt.columns}')
print(f'Head:\n{student_dt.head(1)}')
print(f'Tail:\n{student_dt.tail(1)}')
print(f'Count:\n{student_dt.count()}')
print(f'Sum:\n{student_dt.sum()}')
print(f'Correlation:\n{student_dt.corr()}')