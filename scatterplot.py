import plotly.graph_objects as go
import plotly.express as px

import pandas as pd
import os
import data_collection as dc



df = dc.slider_wrapper(1000)
print(df.head(10))
print(df.tail(10))

fig=px.scatter_mapbox(df,


                      lon=df['longitude'],
                      lat=df['latitude'],
                      zoom=15,
                      color=df['color'],
                      size=df['size'],
                      width=1200,
                      height=900,
                      )
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":50,"l":0,"b":10})


# Create and add slider
steps = []
# for i in range(len(fig.data)):
#    step = dict(
#         method="update",
#         args=[{"visible": [False] * len(fig.data)},
#               {"title": "Slider switched to step: " + str(i)}],  # layout attribute
#     )
#     step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
#     steps.append(step)

sliders = [dict(
    active=10,
    currentvalue={"prefix": "Time in hours: "},
    pad={"t": 48},
    #steps=steps
)]

fig.update_layout(
    sliders=sliders
)

output = os.path.join(os.getcwd() , "map.html")
fig.write_html("map.html")
