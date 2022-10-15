import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import os

df = pd.read_csv (r'C:\Users\goenk\Downloads\SAS_GUTS_Hackathon-20221014T172129Z-001\SAS_GUTS_Hackathon\locationfinal.csv')
print(df.head(10))
print(df.tail(10))

fig=px.scatter_mapbox(df,


                      lon=df['lon'],
                      lat=df['lat'],
                      zoom=5,
                      color=df['color'],
                      size=df['size'],
                      width=1200,
                      height=900,
                      title='Car Share')
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

output = os.getcwd() + "/map.html"
fig.write_html("output")
