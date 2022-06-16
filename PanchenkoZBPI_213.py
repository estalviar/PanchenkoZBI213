import json
from functools import reduce
from statistics import mean


"""task1"""
def fact(x):
  if x == 0:
    return 1
  else:
    return x * fact(x - 1) 


"""task2"""
def filter_even(li):
	 return list(filter((lambda x: x % 2 == 0), li))


"""task3"""
def square(li):
  return list(map(lambda x: x**2, li)) 


"""task4"""
def bin_search(li, element):
    mid = 0
    start = 0
    end = len(li)
    step = 0

    while start <= end:
        step = step + 1
        
        mid = (start + end) // 2
        if element == li[mid]:
            return mid
        
        if element < li[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


"""task5"""
def is_palindrome(string):
    
    new_string = ''.join(i for i in string if i.isalpha()).lower()
    i, j = 0, len(new_string) - 1
    while j + 1 > i:
        if new_string[i] != new_string[j]:
          return "NO"
        i += 1
        j -= 1
    return "YES"


"""task6"""
def calculate(path2file):
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '//': lambda x, y: x // y,
        '%': lambda x, y: x % y,
        '**': lambda x, y: pow(x, y),
    }
    with open(path2file) as f:
        lines = f.readlines()
        results = []
        for i in range(len(lines)):
            line_content = lines[i].split()
            results.append(operations[line_content[0]](int(line_content[1]), int(line_content[2])))
        return reduce(lambda x, y: str(x) + ',' + str(y), results)

"""task7"""
def substring_slice(path2file_1, path2file_2):
    with open(path2file_1) as f_1, open(path2file_2) as f_2:
        lines = f_1.readlines()
        intervals = f_2.readlines()
        results = []
        for i in range(len(lines)):
            interval = intervals[i].split()
            results.append(lines[i][int(interval[0]):int(interval[1]) + 1])
        return " ".join(results)



"""task8"""
def decode_ch(sting_of_elements):
   
    buf = ''
    result = ""
   

    elems = json.load(open('periodic_table.json'))
    for i in range(len(sting_of_elements) - 1):
        buf += sting_of_elements[i]
       
        if buf in elems and not sting_of_elements[i+1].islower():
            result += elems[buf]
            buf = ''
           
    buf += sting_of_elements[-1]
    if buf in elems:
        result += elems[buf]
    return result

"""task9"""

class Student:
    
    def __init__(self, name, surname, grade=None):
        self.name = name
        self.surname = surname
        self.full_name = name + " " + surname
        
        if grade is not None:
            self.grades = grade
        else:
            self.grades = [3, 4, 5]

    def greeting(self):
        return "Hello, I am Student"

    def mean_grade(self):
        return sum(self.grades) / len(self.grades)

    def is_otlichnik(self):
        return "YES" if self.mean_grade() >= 4.5 else "NO"

    def __add__(self, other):
        
        if isinstance(other, Student):
            return self.name + " is friends with " + other.name
    
    def __str__(self):
        return self.full_name

"""task10"""

class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)
