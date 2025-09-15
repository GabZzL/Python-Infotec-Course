# ARRAYS
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

# SETS
set_a = set([1, 2, 3])
set_b = set([3, 4, 5])
union_set = set_a | set_b
union_set.update([6, 6, 7, 8])
intersection_set = set_a & set_b
print(union_set)
print(intersection_set)

# DICTIONARIES
students = {
    "Alice": {
        "grades": [95, 88, 92],
        "subjects": ["Math", "History", "Science"]
    },
    "Bob": {
        "grades": [78, 85, 80],
        "subjects": ["English", "Art", "Math"]
    }
}

students["Gabriel"] = {
    "grades": [80, 80, 80],
    "subjects": ["English", "Math", "Physics"]
}

students["Alice"]["subjects"].append("Computer Science")

print(students)

# TUPLES
coordinates = tuple([11.50, 45.2, 23.2])
print(coordinates)

# CASTING
value_1 = "50"
value_2 = "56.99"

num_1 = int(value_1)
num_2 = float(value_2)

total = num_1 + num_2
print(round(total, 2)) 

letters = ["a", "r", "m", "a", "n", "d", "o"]
name = ''.join(map(str, letters))
print(name)

# FUNCTIONS
def iva_calculator(mount):
    iva = mount * 0.19
    return iva

# calculate final amount
initial_amount = 1000
iva = iva_calculator(initial_amount)
total = initial_amount + iva
print(total)

# RECURSION
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

print("factorial: ")
final_value = factorial(5)
print(final_value) 
