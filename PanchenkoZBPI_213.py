"""task1"""
def fact(x):
  if x == 1:
    return x
  else:
    return x * fact(x - 1) #Вызываем ту же функцию

print(fact(4))
"""task2"""
def filter_even(li):
	 return list(filter((lambda x: x % 2 == 0), li))

x = filter_even([12,14,18,19,21,7])
print(x)
"""task3"""
def square(li):
  return list(map(lambda x: x**2, li)) 

print(square([1,2,3,4,5]))
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

print(bin_search([2,5,7,9,11,17,222],11))
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

print(is_palindrome("Madam, I'm Adam"))
print(is_palindrome("А роза упала на лапу Азора"))
"""task6"""
def calculate(path2file):
    result = ""
    with open(path2file) as f:
        
        contents = f.readlines()
        for expression in contents:
            ls = expression.split()
            
            if ls[0] == "+":
                result += f'{int(ls[1]) + int(ls[2])},'
            if ls[0] == '-':
                result += f'{int(ls[1]) - int(ls[2])},'
            if ls[0] == '*':
                result += f'{int(ls[1]) * int(ls[2])},'
            if ls[0] == '//':
                result += f'{int(ls[1]) // int(ls[2])},'
            if ls[0] == '%':
                result += f'{int(ls[1]) % int(ls[2])},'
            if ls[0] == '**':
                result += f'{int(ls[1]) ** int(ls[2])},'
               
    return result[:-1]

name_file = input('Введите имя файла: ')
print(calculate(name_file))
"""task7"""
def substring_slice(path2file_1, path2file_2):
    f1, f2 = open(path2file_1, "r"), open(path2file_2, "r") 
    numbers = []
    contents = f2.readlines() 
    for expression in contents:
        ls = expression.split() 
        numbers.append((int(ls[0]), int(ls[1]))) 

    result = []
    for index, token in enumerate(f1.readlines()):
        token = token[:-1] 
        result.append(token[numbers[index][0]:numbers[index][1] + 1]) 
    f3 = open("out.txt", "w")
    
    for elem in result:
        f3.write(elem + ' ')
    f1.close()
    f2.close()
    f3.close()
    return result

print(substring_slice(input("Введите название первого файла(.txt): "), input("Введите название второго файла(.txt): ")))
"""task8"""
import json
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



print(decode_ch("NOTiFICaTiON"))
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


st1 = Student("Vasya", "Sur1", [5,5,5,5,4])
st2 = Student("Alex", "Sur2")
print(st1.is_otlichnik())
print(st1)
"""task10"""
class MyError(Exception):

    def __init__(self, msg):
        self.msg = msg


"""функция пример"""
def fact(n):
    if n < 0:
        raise MyError("Value less 0")
    res = 1
    while n != 0:
        res *= n
        n -= 1
    return res

print(fact(-1))