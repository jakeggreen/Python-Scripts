import plotly.graph_objects as go

# data
label = ["Outstanding", "Good", "Requires improvement", "Inadequate", "Outstanding", "WRN", "Active", "Resigned", "Cancelled"]
source = [0, 0, 0, 0]
target = [4, 1, 2, 3]
value =  [3, 7, 3, 4]

# data to dict, dict to sankey
link = dict(
			source = source, 
			target = target, 
			value = value
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
fig.update_layout(title_text = "Provider Events", font_size = 10)
fig.show()

# print(data)
