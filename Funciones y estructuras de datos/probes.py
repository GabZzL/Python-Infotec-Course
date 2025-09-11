# One dimension array
uni_list = [1,2,3,4,5]
# Bidimensional array
double_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

first_element = uni_list[0]

# get access to the elements
print(first_element)

print(double_list[0][1])

for element in uni_list:
    print(element)

for array in double_list:
    print(array)
    
# modify values
uni_list[0] = 0
uni_list.append(6)

print(uni_list)

double_list[0] = [0.1, 0.2, 0.3]
double_list.append([1000, 2000, 3000])
double_list[0][0] = 0.01

double_list.remove([100, 200, 300])
double_list.insert(2, [11, 21, 31])

print(double_list)