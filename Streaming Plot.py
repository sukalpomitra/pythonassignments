import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import *
from datetime import datetime
import time
import json
import urllib2

stream_ids = tls.get_credentials_file()['stream_ids']

# Get stream id from stream id list 
stream_c1 = stream_ids[0]
stream_c2 = stream_ids[1]
stream_c3 = stream_ids[2]
stream_c4 = stream_ids[3]
stream_c5 = stream_ids[4]
stream_c6 = stream_ids[5]
stream_c7 = stream_ids[6]
stream_c8 = stream_ids[7]
stream_c9 = stream_ids[8]
stream_c10 = stream_ids[9]
stream_c11 = stream_ids[10]
stream_c12 = stream_ids[11]
stream_c13 = stream_ids[12]
stream_c14 = stream_ids[13]
stream_c15 = stream_ids[14]
stream_c16 = stream_ids[15]
stream_c17 = stream_ids[16]
stream_c18 = stream_ids[17]
stream_c19 = stream_ids[18]

# Make instance of stream id object 
streamc1 = Stream(
    token=stream_c1,  # (!) link stream id to 'token' key
    maxpoints=80      # (!) keep a max of 80 pts on screen
)

streamc2 = Stream(
    token=stream_c2,  # (!) link stream id to 'token' key
    maxpoints=80      # (!) keep a max of 80 pts on screen
)

streamc3 = Stream(
    token=stream_c3,  # (!) link stream id to 'token' key
    maxpoints=80      # (!) keep a max of 80 pts on screen
)

streamc4 = Stream(
    token=stream_c4,  # (!) link stream id to 'token' key
    maxpoints=80      # (!) keep a max of 80 pts on screen
)

streamc5 = Stream(
    token=stream_c5,  # (!) link stream id to 'token' key
    maxpoints=80      # (!) keep a max of 80 pts on screen
)

streamc6 = Stream(
    token=stream_c6,  # (!) link stream id to 'token' key
    maxpoints=80      # (!) keep a max of 80 pts on screen
)

streamc7 = Stream(
    token=stream_c7,  # (!) link stream id to 'token' key
    maxpoints=80      # (!) keep a max of 80 pts on screen
)

streamc8 = Stream(
    token=stream_c8,  # (!) link stream id to 'token' key
    maxpoints=80      # (!) keep a max of 80 pts on screen
)

streamc9 = Stream(
    token=stream_c9,  # (!) link stream id to 'token' key
    maxpoints=80      # (!) keep a max of 80 pts on screen
)

streamc10 = Stream(
    token=stream_c10,  # (!) link stream id to 'token' key
    maxpoints=80      # (!) keep a max of 80 pts on screen
)

streamc11 = Stream(
    token=stream_c11,  # (!) link stream id to 'token' key
    maxpoints=80      # (!) keep a max of 80 pts on screen
)

streamc12 = Stream(
    token=stream_c12,  # (!) link stream id to 'token' key
    maxpoints=80      # (!) keep a max of 80 pts on screen
)

streamc13 = Stream(
    token=stream_c13,  # (!) link stream id to 'token' key
    maxpoints=80      # (!) keep a max of 80 pts on screen
)

streamc14 = Stream(
    token=stream_c14,  # (!) link stream id to 'token' key
    maxpoints=80      # (!) keep a max of 80 pts on screen
)

streamc15 = Stream(
    token=stream_c15,  # (!) link stream id to 'token' key
    maxpoints=80      # (!) keep a max of 80 pts on screen
)

streamc16 = Stream(
    token=stream_c16,  # (!) link stream id to 'token' key
    maxpoints=80      # (!) keep a max of 80 pts on screen
)

streamc17 = Stream(
    token=stream_c17,  # (!) link stream id to 'token' key
    maxpoints=80      # (!) keep a max of 80 pts on screen
)

streamc18 = Stream(
    token=stream_c18,  # (!) link stream id to 'token' key
    maxpoints=80      # (!) keep a max of 80 pts on screen
)

streamc19 = Stream(
    token=stream_c19,  # (!) link stream id to 'token' key
    maxpoints=80      # (!) keep a max of 80 pts on screen
)


# Initialize trace of streaming plot by embedding the unique stream_id
tracec1 = Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=streamc1         # (!) embed stream id, 1 per trace
)

tracec2 = Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=streamc2         # (!) embed stream id, 1 per trace
)

tracec3 = Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=streamc3         # (!) embed stream id, 1 per trace
)

tracec4 = Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=streamc4         # (!) embed stream id, 1 per trace
)

tracec5 = Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=streamc5         # (!) embed stream id, 1 per trace
)

tracec6 = Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=streamc6         # (!) embed stream id, 1 per trace
)

tracec7 = Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=streamc7         # (!) embed stream id, 1 per trace
)

tracec8 = Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=streamc8         # (!) embed stream id, 1 per trace
)

tracec9 = Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=streamc9         # (!) embed stream id, 1 per trace
)

tracec10 = Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=streamc10         # (!) embed stream id, 1 per trace
)

tracec11 = Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=streamc11         # (!) embed stream id, 1 per trace
)

tracec12 = Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=streamc12         # (!) embed stream id, 1 per trace
)

tracec13 = Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=streamc13         # (!) embed stream id, 1 per trace
)

tracec14 = Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=streamc14         # (!) embed stream id, 1 per trace
)

tracec15 = Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=streamc15         # (!) embed stream id, 1 per trace
)

tracec16 = Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=streamc16         # (!) embed stream id, 1 per trace
)

tracec17 = Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=streamc17         # (!) embed stream id, 1 per trace
)

tracec18 = Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=streamc18         # (!) embed stream id, 1 per trace
)

tracec19 = Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=streamc19         # (!) embed stream id, 1 per trace
)


data = Data([tracec1, tracec2, tracec3, tracec4
            , tracec5, tracec6, tracec7, tracec8
            , tracec9, tracec10, tracec11, tracec12
            , tracec13, tracec14, tracec15, tracec16
            , tracec17, tracec18, tracec19])

# Add title to layout object
layout = Layout(title='Time Series')

# Make a figure object
fig = Figure(data=data, layout=layout)

response = urllib2.urlopen('http://eegapp12.appspot.com/eeg/api/')
jsonData = json.load(response)   

# (@) Send fig to Plotly, initialize streaming plot, open new tab
unique_url = py.plot(fig, filename='EEG CHART')   

# (@) Make instance of the Stream link object, 
#     with same stream id as Stream id object
sc1 = py.Stream(stream_c1)
sc2 = py.Stream(stream_c2)
sc3 = py.Stream(stream_c3)
sc4 = py.Stream(stream_c4)
sc5 = py.Stream(stream_c5)
sc6 = py.Stream(stream_c6)
sc7 = py.Stream(stream_c7)
sc8 = py.Stream(stream_c8)
sc9 = py.Stream(stream_c9)
sc10 = py.Stream(stream_c10)
sc11 = py.Stream(stream_c11)
sc12 = py.Stream(stream_c12)
sc13 = py.Stream(stream_c13)
sc14 = py.Stream(stream_c14)
sc15 = py.Stream(stream_c15)
sc16 = py.Stream(stream_c16)
sc17 = py.Stream(stream_c17)
sc18 = py.Stream(stream_c18)
sc19 = py.Stream(stream_c19)

# (@) Open the stream
sc1.open()
sc2.open()
sc3.open()
sc4.open()
sc5.open()
sc6.open()
sc7.open()
sc8.open()
sc9.open()
sc10.open()
sc11.open()
sc12.open()
sc13.open()
sc14.open()
sc15.open()
sc16.open()
sc17.open()
sc18.open()
sc19.open()
while True:
    for json in jsonData:
        x = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        yc1 = json['c1']
        yc2 = json['c2']
        yc3 = json['c3']
        yc4 = json['c4']
        yc5 = json['c5']
        yc6 = json['c6']
        yc7 = json['c7']
        yc8 = json['c8']
        yc9 = json['c9']
        yc10 = json['c10']
        yc11 = json['c11']
        yc12 = json['c12']
        yc13 = json['c13']
        yc14 = json['c14']
        yc15 = json['c15']
        yc16 = json['c16']
        yc17 = json['c17']
        yc18 = json['c18']
        yc19 = json['c19']


        # (-) Both x and y are numbers (i.e. not lists nor arrays)

        # (@) write to Plotly stream!
        sc1.write(dict(x=x, y=yc1))
        sc2.write(dict(x=x, y=yc2))
        sc3.write(dict(x=x, y=yc3))
        sc4.write(dict(x=x, y=yc4))
        sc5.write(dict(x=x, y=yc5))
        sc6.write(dict(x=x, y=yc6))
        sc7.write(dict(x=x, y=yc7))
        sc8.write(dict(x=x, y=yc8))
        sc9.write(dict(x=x, y=yc9))
        sc10.write(dict(x=x, y=yc10))
        sc11.write(dict(x=x, y=yc11))
        sc12.write(dict(x=x, y=yc12))
        sc13.write(dict(x=x, y=yc13))
        sc14.write(dict(x=x, y=yc14))
        sc15.write(dict(x=x, y=yc15))
        sc16.write(dict(x=x, y=yc16))
        sc17.write(dict(x=x, y=yc17))
        sc18.write(dict(x=x, y=yc18))
        sc19.write(dict(x=x, y=yc19))

        # (!) Write numbers to stream to append current data on plot,
        #     write lists to overwrite existing data on plot (more in 7.2).

        time.sleep(0.08)  # (!) plot a point every 80 ms, for smoother plotting


# (@) Close the stream when done plotting
sc1.close() 
sc2.close() 
sc3.close()
sc4.close()
sc5.close()
sc6.close()
sc7.close()
sc8.close()
sc9.close()
sc10.close()
sc11.close()
sc12.close()
sc13.close()
sc14.close()
sc15.close()
sc16.close()
sc17.close()
sc18.close()
sc19.close()   


# In[ ]:



