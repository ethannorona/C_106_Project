import csv
import numpy as np
import plotly.express as px

def getDataSource(data_path):
    coffeeDrank = []
    hoursOfSleep = []
    
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        
        for row in df:
            coffeeDrank.append(float(row["Coffee in ml"]))
            hoursOfSleep.append(float(row["sleep in hours"]))
    
    return {"x" : coffeeDrank, "y" : hoursOfSleep}
    
def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between coffee drank vs hours of sleep: ", correlation[0,1])
    
def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x="Coffee in ml", y="sleep in hours", color="week")
        fig.show()
        
def setup():
    data_path = "./data/cups of coffee vs hours of sleep.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)
    
setup()