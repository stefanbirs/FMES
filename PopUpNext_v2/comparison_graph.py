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
            x_val.append((data_values[0]))
            y_val.append(float(data_values[1]))
    trace=go.Bar(
        x = x_val,
        y = y_val,
        name=name_val
    )
    file.close()
    return trace
data_1=get_data("Graph3Final.txt","WithoutSystem")
data_2=get_data("Graph3FinalSystem.txt","WithSystem")
plotly.offline.plot({
"data": [data_1,data_2],
"layout": go.Layout(
    title="Various Cities System vs Non-System",
    barmode='group',
    yaxis=dict(title = 'Time (seconds)'),
    xaxis=dict(title = 'Various Cities'))
}, auto_open=True)
