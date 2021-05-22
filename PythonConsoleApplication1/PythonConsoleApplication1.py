

import argparse
import csv

class SMSdataManagement(object):
    def __init__(self):
        if user_choice==1:
            self.RollNo=args.RollNo
            self.Name=args.Name
            self.DOB=args.DOB
            
       
        self.CourseId=args.CourseId
            
        if choice==2:
            self.CourseName=args.CourseName
            self.Duration=args.Duration
            self.Fess=args.Fees
            

    def StoringStudentData_CSV(self):
        with open('Studentdata.csv','w',newline='') as stu_file:
            writer=csv.writer(stu_file) 
            writer.writerow(['RollNo','Name','DOB','CourseId'])
            writer.writerow([args.RollNo,args.Name,args.DOB,args.CourseId]) 
    def StoringCourseData_CSV(self):
        with open('Coursedata.csv','w',newline='') as course_file:
            writer=csv.writer(course_file) 
            writer.writerow(['CourseId','CourseName','Duration','Fees'])
            writer.writerow([args.CourseId,args.CourseName,args.Duration,args.Fees])  
    def DisplayStudent(self):
        with open('Studentdata.csv','r') as student_file:
            reader=csv.reader(student_file)
            for line in reader:
                print(line)        
    def DisplayCourse(self):
        with open('Coursedata.csv','r') as course_file:
            reader=csv.reader(course_file)
            for line in reader:
                print(line)
   
       
if __name__ == '__main__':
    
    # Creating the welcome message
    print("Welcome To SMS \n Tell us who you are \n 1.Student \n 2.Admin")
    choice = int(input("Enter 1 if you are a student \nEnter 2 if you are admin\n"))
    if choice == 1:
        print("1.Register \n2.View Course\n3.Apply for a course")
        user_choice = int(input("Enter 1 if you want to register\n Enter 2 if you want to view courses \nEnter 3 if you want to apply for a course"))
        if user_choice == 1:
            print('Enter the rollno as -R (your roll no) -N (name) -D (dob) -CI(CourseId)')
            parser = argparse.ArgumentParser(description='DataManagement')
            args = parser.parse_args()
            parser.add_argument('-R','--RollNo',type=int,help='Enter the Roll number of the student ')
            parser.add_argument('-N','--Name',metavar='Name',type=str,help='Enter the name of the student')  
            parser.add_argument('-D','--DOB',metavar='DOB',type=str,help='Enter the DOB in dd/mm/yy format')
            parser.add_argument('-CI','--CourseId',type=str,help='Enter the course id of the course the student prefers')
            #RollNo=input("RollNo")
            class_obj = SMSdataManagement()
            class_obj.StoringStudentData_CSV()
            #print(Name)          
            #Obtaining_student_data()
            registered = 1
        if user_choice == 2:
            args = parser.parse_args()
            class_obj = SMSdataManagement()
            class_obj.DisplayCourse()
        if user_choice == 3:
            if registered == 1:
                print('Enter the -CI(CourseId)')
                #Obtaining_student_data()
                parser = argparse.ArgumentParser(description='DataManagement')
                parser.add_argument('-R','--RollNo',type=int,help='Enter the Roll number of the student ')
                parser.add_argument('-N','--Name',metavar='Name',type=str,help='Enter the name of the student')  
                parser.add_argument('-D','--DOB',metavar='DOB',type=str,help='Enter the DOB in dd/mm/yy format')
                parser.add_argument('-CI','CourseId',type=str,help='Enter the course id of the course the student prefers')
            else:
                print("please register before applying for the course ")
                user_choice = int(input("Enter 1 if you want to register\n Enter 2 if you want to view courses \nEnter 3 if you want to apply for a course"))




    if choice == 2:
        user_choice=2
        class_obj = SMSdataManagement()

        print("Welcome Admin /nEnter 1 to Add a new Course \nEnter 2 to View Courses \nEnter 3 to View Student\n")
        admin_choice=int(input("Enter your choice"))
        if admin_choice==1:
            print('Enter the CourseId as -CI (CourseId) -CN (Course name) -Du (duration) -F(fees)')
            parser.add_argument('-CI','CourseId',type=str,help='Enter the course id of the course the student prefers')           
            parser.add_argument('-CN','CorseName',type=str,help='Enter the name of the course the student prefers')            
            parser.add_argument('-Du','Duration',type=str,help='Enter the Duration intrms of years')
            parser.add_argument('-F','fees',type=int,help='Enter the fees for the course')  
        if admin_choice==2:
            class_obj.DisplayCourse()
        if admin_choice==3:  
            class_obj.DisplayStudent()       
