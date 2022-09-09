'''
Purpose: This program provides demo visualizations one can create using wejo data
Author: szhao
Date: 9/7/2022
'''
'''
setup.py is used to set up the ODBC connection to the wejo SQL Server database
'''
# import libraries
import pandas as pd
from datetime import datetime
import pyodbc 
import geopandas as gpd
import matplotlib.pyplot as plt
import warnings

import helpers.queryFun as queryF
import helpers.plotFun as plotF


warnings.filterwarnings('ignore')

# connect to SQL Server and do some queries
def connect(yourPathToSettings):
    try:
        # parse path to add connection
        pathToSettings = yourPathToSettings
        server = ""
        database = ""
        username = ""
        password = ""

        with open(pathToSettings) as f:
            for line in f:
                if line[:3] == "ser":
                    # strip() get rid of the new line character at the end
                    server = line.partition(' = ')[2].strip()
                if line[:3] == "dat":
                    database = line.partition(' = ')[2].strip()
                if line[:3] == "use":
                    username = line.partition(' = ')[2].strip()
                if line[:3] == "pas":
                    password = line.partition(' = ')[2].strip()
        f.close()

        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

        sqlSyntax1 = """
        SELECT * FROM [Wejo].[dbo].[DE_NewData]
        WHERE 1 = 1
        AND [location.postalCode] = '06160';
        """
        sqlSyntax2 = """
        SELECT * FROM [Wejo].[dbo].[VM_NewData]
        WHERE 1 = 1
        AND [location.postalCode] = '06160'
        AND capturedTimestamp LIKE '2021-01-16%';
        """
        
        # # use cursor.execute and cursor.fetch
        # cursor = cnxn.cursor()
        # print("Connected to SQL Server")

        # queryF.getAllRows(cursor, sqlSyntax, False)
        # queryF.getOneRowAtATime(cursor, sqlSyntax, False)
        # queryF.getNRows(cursor, sqlSyntax1, False, 100)
        # queryF.getNRows(cursor, sqlSyntax2, False, 100)

        # # close cursor
        # cursor.close()


        # # read sql query results as dataframe
        # df = pd.read_sql(sqlSyntax2, cnxn)
        # print(df.head(10))
        # plotF.plotPoints(df)

    except pyodbc.Error as error:
        print(error)
    
    finally:
        if cnxn:
            cnxn.close()
            print("Connection is closed")



if __name__ == "__main__":

    # settingsFilePath = "conf\settings.txt"
    # connect(settingsFilePath)

    # # by postalcode
    # f1 = plt.figure(1)
    # df1 = pd.read_csv(r"sample\r4.csv")
    # plotF.plotPoints(df1)
    # f2 = plt.figure(2)
    # df2 = pd.read_csv(r"sample\r5.csv")
    # plotF.plotPoints(df2)
    # plotF.plotPointsByCategory(df1, "event_eventType")

    # by date
    f8 = plt.figure(8)
    df1 = pd.read_csv(r"sample\r8.csv")
    plotF.plotPoints2(df1)
    f9 = plt.figure(9)
    df2 = pd.read_csv(r"sample\r9.csv")
    plotF.plotPoints2(df2)

 
    # pp = gpd.GeoDataFrame(df1, geometry=gpd.points_from_xy(df1.location_longitude, df1.location_latitude))
    # ax1 = pp.plot(marker='*', color='blue', alpha=0.2, markersize=5, )


    
    plt.show()

