# By submitting this assignment, I agree to the following: 
# "Aggies do not lie, cheat, or steal, or tolerate those who do." 
# "I have not given or received any unauthorized aid on this assignment." 
# 
# Name: Daniel Yeung
# Section: 204 
# Assignment: Week 11 Canvas Lab (individual): Surveying to File 
# Date: 10/30/2023

# Initialize dictionaries to store data for each year
year_data = {
    'Freshman': {'count': 0, 'min_age': float('inf'), 'max_age': float('-inf')},
    'Sophomore': {'count': 0, 'min_age': float('inf'), 'max_age': float('-inf')},
    'Junior': {'count': 0, 'min_age': float('inf'), 'max_age': float('-inf')},
    'Senior +': {'count': 0, 'min_age': float('inf'), 'max_age': float('-inf')}
}

# Continuously ask for user input
while True:
    year = input("Enter your year of school (or 'quit' to exit): ").strip().title()
    
    if year == 'Quit':
        break
    
    if year not in year_data:
        print("Invalid year. Please enter a valid year.")
        continue
    
    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Invalid age. Please enter a valid age.")
        continue
    
    # Update data for the entered year
    year_data[year]['count'] += 1
    year_data[year]['min_age'] = min(year_data[year]['min_age'], age)
    year_data[year]['max_age'] = max(year_data[year]['max_age'], age)

# Write the data to the file
with open('Student_Data_23Fa.txt', 'w') as file:
    file.write("Year        |  Number of Students   Minimum Age   Maximum Age\n")
    file.write("-" * 60 + "\n")
    
    for year, data in year_data.items():
        file.write(f"{year.ljust(11)} |  {str(data['count']).ljust(20)} {str(data['min_age']).ljust(13)} {data['max_age']}\n")

print("Data has been saved to 'Student_Data_23Fa.txt'.")