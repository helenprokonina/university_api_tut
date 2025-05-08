import streamlit as st 
import requests


#Endpoint urls
create_student_url = 'http://localhost:8080/student'
delete_student_url = 'http://localhost:8080/student'
get_students_url = 'http://localhost:8080/students'


def create_student(first_name, last_name):
    payload={
        'first_name': first_name,
        'last_name': last_name
    }
    response = requests.post(create_student_url, json=payload)
    if response.status_code == 200:
        st.success("Student created successfully!")
    else:
        st.error("Failed to create a student")
        
def delete_student(student_id):
    delete_url = f"{delete_student_url}/{student_id}"
    response = requests.delete(delete_url)
    if response.status_code == 200:
        st.success("Student deleted successfully!")
    else:
        st.error("Failed to delete a student")   
        
def get_students():
    response = requests.get(get_students_url)
    if response.status_code == 200:
        students = response.json()
        st.write("List of students")
        for student in students:
            st.write(f"-{student['id']}: {student['first_name']} {student['last_name']}")
    else:
        st.error("Failed to retrieve students")         
    
    


#Main app
def main():
    st.title("University API Tutorial")
    
    #Input fields
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    
    #Create student
    if st.button("Submit"):
        create_student(first_name, last_name)
    
    #Delete student
    student_id = st.text_input("Student ID to delete")
    if st.button("Delete"):
        delete_student(student_id)
        
    #All students
    get_students()   
        
    
    
    
if __name__ == "__main__":
    main()    