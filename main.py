import datetime
import sys

d = {}
candidate={}

final=[]
office_list=[]
name_list=[]
sub_list=[]
reg_nos=[]

def register_no_generation(office):
    generator_code = ''
    access_dictionary = {'Customs': 'CUS', 'GST': 'GST'}
    x = datetime.datetime.now()
    date = x.strftime("%m%y")

    try:
        if "Customs" in office:
            generator_code += access_dictionary['Customs']
        elif "GST" in office:
            generator_code += access_dictionary['GST']
        else:
            raise ValueError("Invalid Value")

        generator_code += date
        return generator_code
    
    except ValueError as ve:
        print(ve)
        sys.exit()


def office_no_generator(x, y):
    return str(chr(x)) + str(chr(y))


flag = True
prev = ''
x = 65
y = 64

while flag:
    choice = int(input("Enter 1 to add entries, Enter 2 to quit: "))

    if choice == 1:
        curr = input("Enter office name: ")
        no_of_candidates = int(input("Enter number of candidates:"))
        for i in range(no_of_candidates):
            office_list.append(curr)

        if prev != curr and y <= 91:
            y += 1
            if y == 73 or y == 79:
                y += 1
        else:
            x += 1
            y = 65

        prev = curr
        office_code = office_no_generator(x, y)
        registration_code = register_no_generation(curr)

        i = 1
        while i <= no_of_candidates:
            try:
                name = input("Enter name of the candidate: ")
                name_list.append(name)
                reg_no = int(input("Enter Registration Number: "))
                reg_nos.append(reg_no)
                sub = int(input("Enter Subjects (between 1 and 4): "))
                sub_list.append(sub)

                if 1 <= sub <= 4:
                    final_code = registration_code + office_code + '00' + str(i)
                    candidate[final_code]= [name, reg_no, sub]
                    d[curr]=[]
                    d[curr].append(candidate)
                    i += 1
                    final.append(final_code)


                else:
                    raise ValueError("Number of subjects should be between 1 and 4")

            except ValueError as ve:
                print(ve)
                sys.exit()

    elif choice == 2:
        flag = False

print(d)
print(final)
print(office_list)
print(sub_list)
print(name_list)
print(reg_nos)
