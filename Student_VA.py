# Student Virtual Assistant

# Libraries for accessing Google Scholar and scheduling reminders
import webbrowser
import schedule
import time

# Function to access Google Scholar
def search_scholar(query):
  webbrowser.open(f"https://scholar.google.com/scholar?q={query}")

# Function to input schedule
def input_schedule():
  schedule = {}
  while True:
    class_name = input("Enter class name (or type 'done' if finished): ")
    if class_name == "done":
      break
    class_time = input("Enter class time (e.g. 9:00 AM): ")
    schedule[class_name] = class_time
  return schedule

# Function to input assignments
def input_assignments():
  assignments = []
  while True:
    assignment = input("Enter assignment (or type 'done' if finished): ")
    if assignment == "done":
      break
    assignments.append(assignment)
  return assignments

# Function to remind student to hydrate
def remind_hydrate():
  print("Don't forget to drink water and stay hydrated!")

# Main function to run the virtual assistant
def run_assistant():
  print("Welcome to the Student Virtual Assistant")
  
  # Input schedule
  print("Please enter your schedule:")
  schedule = input_schedule()
  print(f"Your schedule: {schedule}")
  
  # Input assignments
  print("Please enter your assignments:")
  assignments = input_assignments()
  print(f"Your assignments: {assignments}")
  
  # Access Google Scholar
  query = input("What would you like to search on Google Scholar? ")
  search_scholar(query)
  
  # Schedule reminders to hydrate
  schedule.every(1).hours.do(remind_hydrate)
  
  # Start reminders
  while True:
    schedule.run_pending()
    time.sleep(1)

# Run the virtual assistant
if __name__ == "__main__":
  run_assistant()

