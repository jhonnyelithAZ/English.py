import csv
from datetime import datetime

def add_daily_blocker():

    blocker = input("what is your Daily Blocker MS Oneidy? ")
    current_date = datetime.now().strftime("%D/%M/%Y %H:%M")

    data={
        'Date': current_date,
        'Daily blocker': blocker
    }

    file_name= 'daily_blocker.csv'
    with open(file_name, 'a', newline='') as csvfile:
        fieldnames= ['Date','Daily blocker']
        writer= csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() ==0:
            writer.writeheader()

        writer.writerow(data)
    
    print("Daily blocker saved correctly :)")

add_daily_blocker()

"""
Protocol selection:  -I will reach out to my team lead via Slak because the error is impacting our API deployment 
and i need to align our rollback strategy before the client demo tomorrow.-

Vocabulary integration: 
The script implements a simple data persistence logic
in a CSV file(daily_blocker.csv). It prompts the user for input ("what is your Daily Blocker?"),
fetches the entered value and current date,and appends this data to the CSV file without overwriting existing records,
ensuring persistence of daily blockers.
"""