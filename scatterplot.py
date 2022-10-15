import plotly.graph_objects as go
import plotly.express as px

import pandas as pd
import os
import data_collection as dc

time_step = 50
time = 0
#df = dc.slider_wrapper(1000)

df = pd.DataFrame(columns=["latitude", "longitude", "color", "size", "time"])
df["size"] = df["size"].astype(int)
while(time<2400):
    df = df.append(dc.slider_wrapper(time), ignore_index=True)
    time += time_step

fig=px.scatter_mapbox(df,


                      lon=df['longitude'],
                      lat=df['latitude'],
                      zoom=15,
                      color_continuous_scale=px.colors.sequential.Plasma,
                      size=df['size'],
                      width=1200,
                      height=900,
                      animation_frame=df["time"],
                      )
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":50,"l":0,"b":10})
#fig.update_layout(hovermode="size")


# Create and add slider
steps = []
# for i in range(len(fig.data)):
#     step = dict(
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
    steps=steps
)]

fig.update_layout(
    sliders=sliders
)

output = os.path.join(os.getcwd() , "map.html")
fig.write_html("map.html")

