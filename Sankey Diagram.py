import plotly.graph_objects as go
import pandas as pd

# data
label = ["Risk Assessments", "CANI", "Other", # Risk assessments
		 "Regional Case", "Without Enforcement", "With Enforcement"] # subsequent inspection grade

source = [0, 0, 0, 0, 3, 3]

target = [1, 2, 3, 3, 4, 5]

value =  [35800, 1700, 15200, 1700, 14100, 2800]

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

data = go.Sankey(link = link, node = node, arrangement = "freeform") # could also be "snap" or "freeform"
  
# plot
fig = go.Figure(data)
fig.update_layout(title_text = "Provider Events", font_size = 10, hovermode = "x")
fig.show()

# print(data)
