import main

def marksheet_generator(reg_no):
    if reg_no in main.d:
        marksheet = {}
        for subject in main.d[reg_no][2]:
            mark = eval(input(f"Enter mark for {subject}: "))
            marksheet[subject] = mark
        main.d[reg_no].pop()  # Remove the old marksheet
        main.d[reg_no].append(marksheet)
        
        print("Marksheet")
        print("\n=============================================================\n")
        print("Registration No", reg_no)
        print("Name:", main.d[reg_no][0])
        print("Roll NO:", main.d[reg_no][1])
        print("Marksheet")
        for subject, mark in marksheet.items():
            if subject=="Customs" and reg_no.startswith("CUS"):
                print("Subject:", subject, "Mark:", mark,"Pass mark:65")
            elif subject=="Customs" and reg_no.startswith("GST"):
                print("Subject:", subject, "Mark:", mark,"Pass mark:65")
            elif subject=="Allied Acts":
                print("Subject:", subject, "Mark:", mark,"Pass mark:",50)
            elif subject=="Administration":
                print("Subject:", subject, "Mark:", mark,"Pass mark:",65)
            elif subject=="GST":
                print("Subject:", subject, "Mark:", mark,"Pass mark:",65)


marksheet_generator('CUS0923AA001')
marksheet_generator("GST0923AB001")

            
            
                







