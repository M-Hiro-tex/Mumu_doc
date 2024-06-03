import numpy as np
import vispy.scene
from vispy.scene import visuals
from mkdocs.plugins import BasePlugin

class VisPyPlugin(BasePlugin):
    def on_page_content(self, html, page, config, files):
        # Load data from file
        glist = np.load("./glist_50000/glist_50000_7colors_0.npy")
        glist_array = np.array(glist)

        # VisPy Visualization Setup
        canvas = vispy.scene.SceneCanvas(keys='interactive', show=False, bgcolor='white')
        view = canvas.central_widget.add_view()

        # Create scatter plot (nodes)
        scatter = visuals.Markers()
        scatter.set_data(glist_array, edge_color=None, face_color=(1, 1, 1, .5), size=5)
        view.add(scatter)

        # Add lines between points based on the specified algorithm
        a = np.sqrt(2)
        lower_bound = a * np.sqrt(6) / 12
        upper_bound = (6/5) * a / np.sqrt(6)

        # Iterate through all pairs of points
        lines_data = []
        for i in range(len(glist_array)):
            for j in range(i+1, len(glist_array)):
                distance = euclidean_distance(glist_array[i], glist_array[j])
                if lower_bound <= distance < upper_bound:
                    lines_data.append((glist_array[i], glist_array[j]))

        # Create and add lines if there are any
        if lines_data:
            lines = np.array(lines_data)
            line_visual = visuals.Line(pos=lines.reshape(-1, 3), connect='segments', color=(0, 0, 0))
            view.add(line_visual)

        # Update the canvas
        canvas.update()

        # Camera setup
        view.camera = 'turntable'

        # Return the HTML code
        return canvas.render()
