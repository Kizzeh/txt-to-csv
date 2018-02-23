import sys
import csv 

# arguments
text_file = sys.argv[1]
output_file = sys.argv[2]

input_data = []

# creating input list
with open(text_file) as input_file:
    for i in input_file:
        input_data.append((input_file.readline().strip('\n')))

# saving the list to a csv
with open(output_file, 'w', newline='') as opt_file:
    writer = csv.writer(opt_file)
    writer.writerow(input_data) 

print("Created File Successfully")