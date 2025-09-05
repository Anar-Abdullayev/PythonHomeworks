from _functools import reduce

import pandas as excelService

df = excelService.read_excel("dataset.xlsx")  # you can specify sheet_name="Sheet1" if needed
employees = df.to_dict(orient="records")
print(employees)
# 1) Map: 'Name' sütununu hamısını böyük hərflərə çevirərək yeni siyahı yaradın.
task1 = list(map(lambda employee: {**employee, "Name": employee["Name"].upper()}, employees))
print('Task 1')
print(task1)

# 2) Map: 'SalaryAZN' dəyərlərini 10% artımla (round) yeni siyahıda göstərin.
task2 = list(map(lambda employee: {**employee, "SalaryAZN": round(employee["SalaryAZN"]*1.1, 2)}, employees))
print('Task 2')
print(task2)

# 3) Filter: Yalnız 'City' = 'Baku' olan əməkdaşları seçin (sətir siyahısı).
task3 = list(filter(lambda x: x["City"] == 'Baku', employees))
print('Task 3')
print(task3)

# 4) Filter: 'Age' >= 30 və 'Department' = 'Engineering' olanları çıxarın.
task4 = list(filter(lambda employee: employee["Age"] >= 30 and employee["Department"] == 'Engineering', employees))
print('Task 4')
print(task4)

# 5) Filter: 'Remote' = True və 'Performance' >= 80 olan sətirləri seçin.
task5 = list(filter(lambda employee: employee["Remote"] and employee["Performance"] >= 80, employees))
print('Task 5')
print(task5)

# 6) Reduce: Bütün 'SalaryAZN' toplamını hesablayın.
task6 = reduce(lambda x, y: x + y["SalaryAZN"], employees, 0)
print('Task 6')
print(task6)

# 7) Reduce: 'SalaryAZN' üzrə maksimumu və minimumu tapın.
task7Max =  max(employees, key=lambda x: x["SalaryAZN"])
task7Min =  min(employees, key=lambda x: x["SalaryAZN"])
print('Task 7')
print(task7Max["SalaryAZN"], task7Min["SalaryAZN"])

# 8) Map+Filter: 'Skills' içində 'python' olan əməkdaşların adlarını böyük hərflərlə qaytarın.
task8 = list(map(lambda x: {**x, "Name": x["Name"].upper() } , filter(lambda employee: str(employee["Skills"]).__contains__("python"), employees)))
print('Task 8')
print(task8)

# 9) Map: 'JoinDate' dəyərlərini 'YYYY-MM' formatına salın.
task9 = list(map(lambda x: {**x, "JoinDate": x["JoinDate"][:-3]}, employees))
print('Task 9')
print(task9)

# 10) Filter+Reduce: 'City' = 'Baku' olanların 'SalaryAZN' cəmini hesablayın.
task10 = reduce(lambda x, y: x+y["SalaryAZN"], filter(lambda employee: employee['City'] == 'Baku', employees), 0)
print('Task 10')
print(task10)

# 11) Map: 'Performance' balına görə kateqoriya təyin edin: 1-59='Low', 60-79='Medium', 80-100='High'.
def getPerformance(point):
    if (point >= 0 and point<=59):
        return 'Low'
    elif (point >= 60 and point<=79):
        return 'Medium'
    elif (point >= 80 and point<=100):
        return 'High'
    else:
        return 'None'
task11 = list(map(lambda x: {**x, "Category": getPerformance(x['Performance'])}, employees))
print('Task 11')
print(task11)

# 12) Filter: 'Skills' içində 'django' VƏ 'docker' olan sətirləri çıxarın.
task12 = list(filter(lambda employee: employee["Skills"].__contains__('django') and employee["Skills"].__contains__('docker'), employees))
print('Task 12')
print(task12)

# 13) Map: 'Age' → gələn il üçün yaş (Age+1) siyahısını yaradın.
task13 = list(map(lambda x: {**x, "Age": x["Age"]+1}, employees))
print('Task 13')
print(task13)

# 14) Filter+Map: 'Department' = 'Data' olanların maaşını 15% artırıb yeni siyahı yaradın.
task14 = list(map(lambda x: {**x, "SalaryAZN": round(x["SalaryAZN"]*1.15, 2)}, filter(lambda employee: employee['Department'] == 'Data', employees)))
print('Task 14')
print(task14)

# 15) Bonus: 'Engineering' şöbəsində 'python' bilənlərin orta maaşını hesablayın.
engineers = list(filter(lambda x: x['Department'] == 'Engineering' and x['Skills'].__contains__('python'), employees))
averageSalary = reduce(lambda x, y: x + y['SalaryAZN'], engineers, 0)/len(engineers)
print('Task 15')
print(engineers)
print(averageSalary)