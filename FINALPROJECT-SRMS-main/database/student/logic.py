from student.models import *
from student.libraries import *
import smtplib,ssl

def sorted_set(class_name,variable_name):
	Total_Groups = set()
	Total_Year_Of_Admission = set()
	Total_Class = set()
	students =  Student.objects.all()
	groups = Groups.objects.all()
	for student in students:
		Total_Year_Of_Admission.add(student.Year_Of_Admission)
	for group in groups:
		Total_Groups.add(group.Group)
		Total_Class.add(group.Class)

	if variable_name == 'Group':
		return sorted(Total_Groups)
	elif variable_name == 'Year_Of_Admission':
		return sorted(Total_Year_Of_Admission)
	elif variable_name == 'Class':
		return sorted(Total_Class)
def Find_Month(Month):
	mon = {'Jan.': 1,'Feb.': 2,'Mar.': 3, 'April':4, 'May': 5, 'June' : 6, 'Jul.' : 7,'Aug.':8,'Sept.': 9,
	'Oct.': 10, 'Nov.' : 11 , 'Dec.' : 12}
	return mon[Month]

def Bargraph(Id,Year,Group,Semester,Course):
	rollnumbers = Student.objects.filter(Group = Group).filter(Year_Of_Admission = Year).values_list('Roll_Number').order_by('Roll_Number')
	workingdays = Student_Attendance.objects.filter(Teacher_Id_Attendance = Id).filter(Course_Code = Course).filter(Semester = Semester)
	len_Workingdays = set()
	data = {
		'Roll Number' : [],
		'Total_Present' : [],
		'Total_Absent' : [],
		'Percentage' : [],
		'Marks' : []
	}
	for i in workingdays:
		len_Workingdays.add(i.Date_Time_Original.date())
	for roll in rollnumbers:
		present = len(workingdays.filter(Roll_Number_Attendance = roll).filter(Attendance_Date = 'PRESENT'))
		if len(workingdays) != 0:
			data['Roll Number'].append(roll[0])
			data['Total_Present'].append(present)
			data['Total_Absent'].append(len(workingdays.filter(Roll_Number_Attendance = roll).filter(Attendance_Date = 'ABSENT')))
			data['Percentage'].append(round((present*100)/len(len_Workingdays),2))
		else:
			pass
	ind = [0]
	total_percentage = {
		'below 75%': 0,
		'above 75%': 0,
		'above 80%': 0,
		'above 85%': 0,
		'above 90%': 0,
	}
	for i in data['Percentage']:
		if i < float(75):
			total_percentage['below 75%'] += 1
			data['Marks'].append(0)
			#print('hello')
		elif i < float(80):
			total_percentage['above 75%'] += 1
			data['Marks'].append(2)
		elif i < float(85):
			total_percentage['above 80%'] += 1
			data['Marks'].append(3)
		elif i < float(90):
			total_percentage['above 85%'] += 1
			data['Marks'].append(4)
		elif i <= float(100):
			total_percentage['above 90%'] += 1
			data['Marks'].append(5)
	if len(workingdays) != 0:
		dataframe = pd.DataFrame(data)
		dataframe_percentage = pd.DataFrame({'percent' : ['below 75%','above 75%','above 80%','above 85%','above 90%'],
		'index' : [total_percentage['below 75%'],total_percentage['above 75%'],total_percentage['above 80%'],total_percentage['above 85%'],
		total_percentage['above 90%']]})
		average_percentage = dataframe['Percentage'].mean()
		return dataframe_percentage,average_percentage,len(len_Workingdays),dataframe
	else:
		dataframe = {}
		dataframe_percentage = {}
		average_percentage = 0
		return dataframe_percentage,average_percentage,len(len_Workingdays),dataframe
	#barplot.show()

def marks_details(exam_type,marks):
	class_total = 0
	for i in marks:
		if i.Marks_Alloted != None:
			class_total += i.Marks_Alloted
	class_average = class_total/len(marks)
	return class_average

def Total_Marks(marks,roll):
	I_1 = marks.filter(Marks_Type = 'I Internal')
	I_2 = marks.filter(Marks_Type = 'II Internal')
	Sem = marks.filter(Marks_Type = 'Semester')
	Atten = marks.filter(Marks_Type = 'Attendance')
	Assign = marks.filter(Marks_Type = 'Assignment')
	data =  {
		'Name' : [],
		'Roll' : [],
		'I_1' : [],
		'I_2' : [],
		'Assign' : [],
		'Sem' : [],
		'Atten' : [],
		'In_Total' : [],
		'Total' : []
	}
	for i in roll:
		data['Name'].append(i.First_Name+' '+i.Last_Name)
		data['Roll'].append(i.Roll_Number)
		I_1_1 = I_1.filter(Roll_Number_Marks = i)
		for j in I_1_1:
			m1 = j.Marks_Alloted
			data['I_1'].append(m1)
		I_2_2 = I_2.filter(Roll_Number_Marks = i)
		for j in I_2_2:
			m2 = j.Marks_Alloted
			data['I_2'].append(m2)
		Assign_2 = Assign.filter(Roll_Number_Marks = i)
		for j in Assign_2:
			m3 = j.Marks_Alloted
			data['Assign'].append(m3)
		Atten_3 = Atten.filter(Roll_Number_Marks = i)
		for j in Atten_3:
			m4 = j.Marks_Alloted
			data['Atten'].append(m4)
		Sem_4 = Sem.filter(Roll_Number_Marks = i)
		for j in Sem_4:
			m5 = j.Marks_Alloted
			data['Sem'].append(m5)
		list_1 = ['m1','m2','m3','m4','m5']
		data_1 = {'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5}
		for i in list_1:
			if data_1[i] is None:
				data_1[i] = 0
			else:
				data_1[i] = float(data_1[i])
		m6 = ((data_1['m1']+data_1['m2'])/4)+data_1['m3']+data_1['m4']
		data['In_Total'].append(m6)
		data['Total'].append(m6+data_1['m5'])
	dataframe = []
	for i in range(len(roll)):
		dataframe.append([data['Name'][i],data['Roll'][i],data['I_1'][i],data['I_2'][i],data['Assign'][i]
		,data['Sem'][i],data['Atten'][i],data['In_Total'][i],data['Total'][i]])
	return dataframe

def email_send(receivers,Rollnumber,Admissionnumber,fname,lname):
	fromaddr = 'siddharthapb095@gmail.com'
	toaddr = receivers
	# MIMEMultipart 
	msg = MIMEMultipart() 
	# senders email address 
	msg['From'] = 'siddharthapb095@gmail.com'
	# receivers email address 
	msg['To'] = receivers
	# the subject of mail
	msg['Subject'] = "subject_of_the_mail"
	# the body of the mail 
	body = "Dear"+" "+lname+" "+fname+",\nYou application is subimtted and addmission process is completed.\nlogin credentials are-\nusername - "+Rollnumber+"\npassword - "+Rollnumber+"\nAdmission Number - "+Admissionnumber+"\npassword is temporary and can be changed."
	msg.attach(MIMEText(body, 'plain'))
	# creates SMTP session 
	email = smtplib.SMTP('smtp.gmail.com', 587) 
	# TLS for security 
	email.starttls() 
	# authentication 
	email.login('siddharthapb095@gmail.com', "tonxkifdtelivwqs") 
	# Converts the Multipart msg into a string 
	message = msg.as_string() 
	# sending the mail 
	email.sendmail(fromaddr, toaddr, message) 
	# terminating the session 
	email.quit()
	'''port = 465  # For SSL
	smtp_server = "smtp.gmail.com"
	sender = 'siddharthapb095@gmail.com'
	password = 'Baddani2002'
	message = """From: From SIDDHTHARTHA COLLEGE OF ARTS AND SCIENCES Subject:
	You application is subimtted and addmission process is completed 
	login credentials
	username - """+Rollnumber+"""
	password - """+Rollnumber+"""
	Admission Number - """+Admissionnumber+"""
	password is temporary and can be changed""" 
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login(sender, password)
		server.sendmail(sender, receivers, message)
	try:
		smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		smtp_server.ehlo()
		smtp_server.login(sender, password)
		smtp_server.sendmail(sender, receivers, message)
		smtp_server.close()
		print ("Email sent successfully!")
	except Exception as ex:
		print ("Something went wrong….",ex)'''