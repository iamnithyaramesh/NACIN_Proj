import pandas as pd
import pyodbc
import main

# Create a list of dictionaries
data_list = []
for i in range(len(main.final)):
    data = {
        'Office': main.office_list[i],
        'Registration_Number': main.final[i],
        'Name_of_Applicant': main.name_list[i],
        'Exam_Code': main.reg_nos[i],
        'No_of_Subjects': main.sub_list[i]
    }
    data_list.append(data)

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data_list)

# Write the DataFrame to an Excel file
excel_file_path = 'exam.xlsx'
df.to_excel(excel_file_path, index=False)

print(f'Data has been written to {excel_file_path}')

# Switching data to Access Database
access_conn_str = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\nithy_my2jqm\Documents\test_database.accdb;'
access_conn = pyodbc.connect(access_conn_str)
cursor = access_conn.cursor()

# Create the table if it does not exist
create_table_query = """CREATE TABLE ExamData (
    Office LONGTEXT,
    Registration_Number LONGTEXT PRIMARY KEY,
    Name_of_Applicant LONGTEXT ,
    Exam_Code NUMBER,
    No_of_Subjects NUMBER
);
"""
cursor.execute(create_table_query)
access_conn.commit()

# Insert data into the Access database
for _, row in df.iterrows():
    insert_query = f"""
    INSERT INTO ExamData (Office, Registration_Number, Name_of_Applicant, Exam_Code, No_of_Subjects)
    VALUES ('{row['Office']}', '{row['Registration_Number']}', '{row['Name_of_Applicant']}', {row['Exam_Code']}, {row['No_of_Subjects']});
    """
    cursor.execute(insert_query)
    access_conn.commit()

# Close the database connection
cursor.close()
access_conn.close()

print('Data has been written to Access Database.')
