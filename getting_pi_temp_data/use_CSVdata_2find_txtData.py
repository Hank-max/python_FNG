
import os
import csv

txt_file_dir = os.listdir('C:/development/python_FNG/getting_pi_temp_data')

############### Getting the keywords from the CSV file ###############
with open('C:/development/python_FNG/getting_pi_temp_data/key_data.csv', 'r') as csv_file_path:
    csvreader = csv.reader(csv_file_path)
    for row in csvreader:
        script = row[1]
        print(scsript)
        
#count the number of rows in the csv file
keyword = 'EV_002'

########## Checking file directory for specific name #################
for fname in txt_file_dir:
    if keyword in fname:
        
        print(fname, " checked")