import plotly
import plotly.graph_objs as go
from plotly.offline import plot
from plotly.subplots import make_subplots
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="airportservices-delhi"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM parkingstands")
records = mycursor.fetchall()
len1 = len(records)

mycursor.execute("SELECT * FROM trolley")
records1 = mycursor.fetchall()
len2 = len(records1)

mycursor.execute("SELECT * FROM informationdesk")
records2 = mycursor.fetchall()
len3 = len(records2)

mycursor.execute("SELECT * FROM currencyexchange")
records3 = mycursor.fetchall()
len4 = len(records3)

mycursor.execute("SELECT * FROM luggagestorage")
records4 = mycursor.fetchall()
len5 = len(records3)

mycursor.execute("SELECT * FROM boardinggates")
records5 = mycursor.fetchall()
len6 =  len(records5)

mycursor.execute("SELECT * FROM arrivalbaggagebelt")
records6 = mycursor.fetchall()
len7 =  len(records6)
label = ['Arrival Baggage Belt','Boarding Gates','Currency Exchange','Information Desk','Luggage Storage','Parking Stands','Trolleys']
fig = make_subplots(rows=1, cols=2, specs=[[{"type": "bar"}, {"type": "pie"}]], subplot_titles=['Bar Chart', 'Pie Chart'])
trace1=go.Bar(
    x=label,
    y=[len1,len2,len3,len4,len5,len6,len7],
    name="",
    marker = {'color' : ['cyan','darkviolet','red','green','blue','orange'] }
    )

trace2=go.Pie(values=[len1,len2,len3,len4,len5,len6,len7],
labels=label,
name="")
fig.add_trace(trace1,row=1, col=1)
fig.add_trace(trace2,row=1, col=2)

fig.update_layout(title='Service Consumption', xaxis={'title':'Service name'},
    yaxis={'title':'Units of Comsumption'})
plotly.offline.plot(fig, filename='C:\\xampp\\htdocs\\Project\\delhidbchart.html',validate=False)
