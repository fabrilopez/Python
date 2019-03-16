# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 21:58:15 2019

@author: Fabricio
"""
import os.path

import matplotlib
matplotlib.use("MacOSX")
# matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.figure import Figure
from matplotlib.colors import PowerNorm  # ,LogNorm, SymLogNorm,

from astropy.io import fits

import tkinter as tk

import json


class SkyToyClass(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "SkyToy")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = SkyFrame(container, self)
        self.frames[SkyFrame] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(SkyFrame)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class SkyFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

# change 'figure_width': 1920, 'figure_height': 1080 =(19.2,10.8)
        f = Figure(figsize=(8, 6))
        a = f.add_subplot(111)
        f.subplots_adjust(left=None, bottom=None, right=1, top=1)

        hdu_list = fits.open(sky_image)
        hdu_list.info()
        img = hdu_list[0].data

        normalise = PowerNorm(gamma=power_normalise)

        a.imshow(img, origin='lower', cmap='gray', norm=normalise, vmax=max_saturation)

        # Embedding In Tk
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Show ToolBar
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        # Activate Zoom
        toolbar.zoom(self)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        hdu_list.close()


def LoadJson():

        filepath = os.path.realpath('../skytoy/sky_config.json')
        json_data = json.load(open(filepath))

        json_path = json_data.get('path')
        json_image_scaling = json_data.get('image_scaling')
        json_max_saturation = json_data.get('max_saturation')
        json_power_normalise = json_data.get('power_normalise')

        return json_path, json_image_scaling, json_max_saturation, json_power_normalise


if __name__ == '__main__':
    # loads JSON file parameters
    path, image_scaling, max_saturation, power_normalise = LoadJson()

    # loads Image
    sky_image = os.path.realpath('../' + path)

    app = SkyToyClass()
    app.mainloop()

    print('Quitting')
