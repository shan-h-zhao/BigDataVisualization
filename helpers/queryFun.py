'''
Purpose: This program provides demo visualizations one can create using wejo data
Author: szhao
Date: 9/7/2022
'''
'''
queryFun.py provides some sample query functions
'''

# function to query all records
def getAllRows(cursor, sqlQuery, printOut):
    cursor.execute(sqlQuery)
    rows = cursor.fetchall()
    print("Total row count is: ", len(rows))
    # if print is True
    if printOut:
        for row in rows:
            print(row)
            print("\n")
    
# function to query one row at a time
def getOneRowAtATime(cursor, sqlQuery, printOut):
     cursor.execute(sqlQuery)
     row = cursor.fetchone()
     while row:
        # if print is true
        if printOut:
            print(row[0])
        row = cursor.fetchone()

# function to query a defined number of rows
def getNRows(cursor, sqlQuery, printOut, batchSize):
    cursor.execute(sqlQuery)
    rows = cursor.fetchmany(batchSize)
    i = 0
    while rows:
        print(i)
        i += 1
        # if print is true
        if printOut:
            print(rows)
            print("\n")
        rows = cursor.fetchmany(batchSize)
            


