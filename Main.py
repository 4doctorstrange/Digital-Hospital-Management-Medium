from Record import Record
from Input import Input

while True:
	print("----------------------------------------------------------------------")
	print("Hello, select a number from given description to perform operation : ")
	print(''' 1 -> Add Patients/Patients \n 2-> Display all \n 3-> Update Patient\n 4-> exit \n'''  )
	q=int(input())

	if q==1:
		ip=Input()
		ip.get_input()

	elif q==2:
		rec=Record()
		rec.show_all()

	elif q==3:
		ide=input(" Enter Id of the patient ")
		n=int(input(" Select the Column that is to be updated\n 1->Medical Details\n 2->Discharge Date\n 3->Discharge Comment "))
		r=Record()
		if n==1:
			st=input(" Enter updated Details: ")
			r.update_medicaldetails(ide,st)
		elif n==2:
			st=input(" Enter Discharge Date in format-> MM/DD/YY (including '/'): ")
			r.update_dischargedate(ide,st)

		else:
			no=int(input(" Select discharge comment 1->Cured or 2->Deceased: "))
			if no==1:
				r.update_cure(ide,"Cured")
			else:
				date_of_death=input("Enter Date of death in format-> MM/DD/YY (including '/'): ")
				time_of_death=input("Enter Time of death in format-> HH:MM:SS (including ':'): ")
				fin=date_of_death+" "+time_of_death
				r.update_deceased(ide,"Deceased",fin)
	else:
		print("Thanks!")
		break
		
