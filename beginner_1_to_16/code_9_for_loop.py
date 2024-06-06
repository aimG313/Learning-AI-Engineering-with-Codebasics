'''expense = [2340, 2500, 2100, 3100, 2980]    
sum = 0
for item in expense:
  sum = sum + item

print("Total expense:", sum)'''

'''start = int(input("Where to start:"))
end = int(input("Where to end:"))
for i in range(start,end):
  print(i)'''

'''expense = [2340, 2500, 2100, 3100, 2980]    
total = 0
for i in range(len(expense)):
  print('Month:',(i+1),'Expense:',expense[i])
  total = total + expense[i]
print("Total Expense:",total)'''


# Define a function to get the salary for a specified number of months
def get_salary(num_months):
    # Initialize an empty list to store the salaries
    salary_list = []
    # Iterate over the range of specified number of months
    for i in range(num_months):
        # Prompt the user to input the salary for the current month,
        # converting the input to a floating-point number
        salary = float(input(f"Enter salary for month {i+1}: "))
        # Append the entered salary to the salary_list
        salary_list.append(salary)
    # Return the list of salaries
    return salary_list

'''# Define the main function
def main():
    # Prompt the user to enter the number of months
    num_months = int(input("Enter the number of months: "))
    # Print a message indicating the number of months for which salaries will be entered
    print(f"Enter the salary for {num_months} months:")
    # Call the get_salary function with the specified number of months and store the returned list of salaries
    salaries = get_salary(num_months)
    # Print the list of salaries
    print("Salary list:", salaries)

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Call the main function
    main()'''

'''key_location = "chair"
locations = ["garage", "living room","chair","closet"]

for i in locations:
    if i == key_location:
        print("Key found in",i)
        break
    else:
        print("key is not found in ",i)'''

'''for i in range(1,10):
    if i%2 == 0:
        continue
    print(i)'''

i = 1
while i<=5:
    print(i)
    i = i + 1

