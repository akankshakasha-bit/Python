student_data = {1:{'name':'sara','age':6},2:{'name':'jeff','age':7},3:{'name':'alia','age':9},4:{'name':'sara','age':6}}
print(student_data.items())                                                   
result = {}
for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result)