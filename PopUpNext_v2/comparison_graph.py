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
        mode = 'lines + markers',
        name=name_val
    )
    file.close()
    return trace
data_1=get_data("G3WithDrone.txt","WithDrone")
data_2=get_data("G2WithoutDrone1st.txt","WithoutDrone")
plotly.offline.plot({
"data": [data_1,data_2],
"layout": go.Layout(
    title="Total user cost comparison",
    yaxis=dict(title = 'Cost'),
    xaxis=dict(title = 'Traffic Density'))
}, auto_open=True)
