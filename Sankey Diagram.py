import plotly.graph_objects as go
import pandas as pd

# data
label = ["WRN", "Suspension", "NTI", "Enforcement Notice", # Enforcement type
		 "Outstanding", "Good", "Requires improvement", "Inadequate"] # subsequent inspection grade

source = [0, 0, 0, 0]

target = [4, 5, 6, 7]

value =  [1, 3, 4, 2]

colors = ['#EBBAB5', '#FEF3C7', '#A6E3D7', '#CBB4D5',
		  '#EBBAB5', '#FEF3C7', '#A6E3D7', '#CBB4D5',
		  '#EBBAB5', '#FEF3C7', '#A6E3D7', '#CBB4D5',
		  '#EBBAB5', '#FEF3C7', '#A6E3D7', '#CBB4D5']

# data to dict, dict to sankey
link = dict(
			source = source, 
			target = target, 
			value = value,
			# color = colors
			)

node = dict(
			pad = 15,
			thickness = 20,
			line = dict(color = "black", width = 0.5),
			label = label,
			color = "blue"
			)

data = go.Sankey(link = link, node = node, arrangement = "perpendicular") # could also be "snap" or "freeform"
  
# plot
fig = go.Figure(data)
fig.update_layout(title_text = "Provider Events", font_size = 10, hovermode = "x")
fig.show()

# print(data)
