# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 21:58:15 2019

@author: Fabricio
"""
import os.path

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib.colors import PowerNorm  # ,LogNorm, SymLogNorm,

from astropy.io import fits

import tkinter as tk

import json

#LARGE_FONT= ("Verdana", 12)


class SkyToyClass(tk.Tk):

    def __init__(self, *args, **kwargs):
      
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "SkyToy")        
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
    
        frame = SkyFrame(container,self)
        self.frames[SkyFrame] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(SkyFrame)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
                
class SkyFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
                   #change 'figure_width': 1920, 'figure_height': 1080 =(19.2,10.8)
        f = Figure(figsize=(13.66,6.78))
        a = f.add_subplot(111)
        f.subplots_adjust(left=None, bottom=None, right=1, top=1)
        
        hdu_list = fits.open(sky_image)
        hdu_list.info()
        img=hdu_list[0].data
        
        normalise = PowerNorm(gamma=power_normalise)
        
        a.imshow(img, origin='lower', cmap='gray', norm=normalise, vmax=max_saturation)
                     
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
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
    
    path, image_scaling, max_saturation, power_normalise = LoadJson()
    
    sky_image = os.path.realpath('../'+path)
    target = (189.997632708, -11.6230542778)
    parameters = {'RA': 189.997, 'Dec': -11.623,
                  'width': 1920, 'height': 1080,
                  'figure_width': 1920, 'figure_height': 1080}

    
    app = SkyToyClass()
    app.mainloop()

    print('Quitting')


