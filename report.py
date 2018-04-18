# coding: utf-8
import csv
import time

# Dirty global variable so I don't touch original author code
# This variable collect data to create a report.csv
data = []
    
def createReport(rows, reportName="report_"):

    # Define file name with date and extention
    csvFileName = reportName + time.strftime("%Y-%m-%d") + ".csv"

    # Define report field name
    fieldName = ["Type", "Name", "Old_ID", "Old_Parent_ID", "New_ID", "New_Parent_ID", "Processed"]

    with open(csvFileName, 'w') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=fieldName)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == '__main__':

    for x in range(10):
        data.append({
            "Type" : "test",
            "Name" : "row" + str(x),
            "Old_ID" : x * x,
            "Old_Parent_ID" : x,
            "New_ID" : ":)",
            "New_Parent_ID" : x + x,
            "Processed" : True
        })
    
    createReport(data)
    print "Done"