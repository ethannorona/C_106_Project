import csv
import numpy as np
import plotly.express as px

def getDataSource(data_path):
    marks_in_percentage = []
    days_present = []
    
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        
        for row in df:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))
    
    return {"x" : marks_in_percentage, "y" : days_present}
    
def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between marks in percentage vs days present: ", correlation[0,1])
    
def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Marks In Percentage",y="Days Present",color="Roll No")
        fig.show()
        
def setup():
    data_path = "./data/Student Marks vs Days Present.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)
    
setup()