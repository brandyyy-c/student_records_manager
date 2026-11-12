student_records = {
    'brandon': 78,
    'faith': 85,
    'kevin': 62
}

def add_student(student_records,info):
    key,value=info
    key=key.lower()
    if key in student_records:
        return f"Student '{key}' already exists! Cannot add this student."
    else:
        student_records[key]=value
        return f"Student '{key}' added with mark '{value}' successfully!"

def update_student(student_records,corrections):
    key,new_value=corrections
    key=key.lower()
    if key in student_records:
        student_records[key]=new_value
        return f"Student '{key}' updated to '{new_value}' successfully!"
    else:
        return f"Student '{key}' does not exist! Cannot update a non-existing student."

def delete_student(student_records, key):
    
    key=key.lower()
    if key in student_records:
        student_records.pop(key)
        return f"Student '{key}' deleted successfully!"
    else:
        return f"Student not found!"

def view_students(student_records):
    if student_records=={}:
        return "No student records available."
    else:
        result= "Current Student Records:\n"
        for key,value in student_records.items():
            result=result + key.capitalize() + ':' + str(value) + '\n'


print(add_student(student_records, ('mary', 90)))

print(update_student(student_records, ('brandon', 95)))

print(delete_student(student_records, 'kevin'))

print(view_students(student_records))


    
 
