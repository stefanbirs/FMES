import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as offline
offline.init_notebook_mode()
def get_data(file_name,name_val):

    file=open(file_name,"r")
    data=file.readlines()
    x_val=[]
    y_val=[]
    for line in data:
        data_values=line.split(',')
        #print(len(data_values))
        if(len(data_values)>1):
            x_val.append(float(data_values[0]))
            y_val.append(float(data_values[1]))
    trace=go.Scatter(
        x = x_val,
        y = y_val,
        mode='lines+markers',
        name=name_val
    )
    file.close()
    return trace
data_1=get_data("Graph4Final.txt","WithSystem")
#data_2=get_data("Graph3FinalSystem.txt","WithSystem")
plotly.offline.plot({
"data": [data_1],
"layout": go.Layout(
    title="Drone Hub vs Distance from Centre",
    yaxis=dict(title = 'Time (seconds)'),
    xaxis=dict(title = 'Distance from Centre'))
}, auto_open=True)
