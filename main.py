# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 11:08:46 2025

@author: IITM
"""

from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt

data_path = r"D:\Benisha\Farhan\Battery_Modeling_Web_Application\LTVS_1P14S _0.5C 3rd cycle_complete_modified.xlsx"
img_path = r"D:\Benisha\Farhan\Battery_Modeling_Web_Application\Scripts\static\cellV_plot.png"

#%%

def plot_image():   
    data = pd.read_excel(data_path)
    
    plt.figure()
    plt.plot(range(len(data)), data.loc[:,'Cell_1':'Cell_14'])
    # plt.legend()
    plt.ylabel('Voltage (V)', size = 10, fontweight = 'bold')
    plt.title('Cell Voltage', fontweight = 'bold')
    plt.grid(linestyle = 'dotted')
    plt.savefig(img_path, dpi =1500)
    plt.close()
    

#%%
app = Flask(__name__)

@app.route("/")

def display_homepage():
    plot_image()
    return render_template("home.html")
    
if __name__ == "__main__":
    app.run(debug = True)


#%%

