#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 11:58:09 2025

@author: thosvarley
"""

import subprocess
import PIL.Image as Image
import numpy as np
from sklearn.cluster import k_means


def load_desktop() -> np.ndarray:

    background = subprocess.check_output(
        "gsettings get org.cinnamon.desktop.background picture-uri",
        shell=True)
    
    background = background.decode("utf-8")[8:-2]
    
    image = Image.open(background)
    
    return np.asarray(image)


def rgb_to_hex(
        red:int, 
        green:int, 
        blue:int) -> str:
    
    return "{:02X}{:02X}{:02X}".format(red, green, blue)


def rgb_to_luminance(
        red:int, 
        green:int, 
        blue:int) -> float:
    
    red /= 255
    green /= 255
    blue /= 255
    
    return 0.2126*red + 0.7152*green + 0.0722*blue


def rgb_to_luminosity(red:int, green:int, blue:int) ->float:
    
    red /= 255
    green /= 255
    blue /= 255
    
    mx = max(red, green, blue)
    mn = min(red, green, blue)
    
    return mx - mn 


def rgb_to_saturation(
        red:int,
        green:int,
        blue:int) -> float:
    
    red /= 255
    green /= 255
    blue /= 255
    
    mx = max(red, green, blue)
    mn = min(red, green, blue)
    
    luminosity = mx-mn 
    
    if luminosity > 0.5:
        saturation = (mx - mn) / (2 - mx - mn)
    else:
        saturation = (mx - mn) / (mx + mn)
    
    return saturation


def average_background(data:np.ndarray) -> str:
    
    avg_red = int(data[:,:,0].mean())
    avg_green = int(data[:,:,1].mean())
    avg_blue = int(data[:,:,2].mean())
    
    return rgb_to_hex(avg_red, avg_green, avg_blue)


def single_channel_background(data:np.ndarray) -> str:
    
    avg_red = int(data[:,:,0].mean())
    avg_green = int(data[:,:,1].mean())
    avg_blue = int(data[:,:,2].mean())
    
    avgs = np.array([avg_red, avg_green, avg_blue])
    
    argmax = np.argmax(avgs)
    mx = np.max(avgs)
    
    winner = np.zeros(3, dtype="int")

    if mx < 128:
        mx = 255 - mx

    winner[argmax] = mx
    
    return rgb_to_hex(*winner)


def clustering_criteria_background(
        data:np.ndarray,
        n_samples = 10_000,
        n_clusters = 10,
        criteria = "luminosity") -> str:
    
    row_samples = np.random.randint(0, data.shape[0], n_samples)
    col_samples = np.random.randint(0, data.shape[1], n_samples)
    
    samples = data[row_samples, col_samples, :]
    
    centroids, membership, _ = k_means(samples, n_clusters, n_init = 1)
    centroids = centroids.astype(int)
    
    ids, sizes = np.unique(membership, return_counts=True)
    
    if criteria == "size":
        argmax = np.argmax(sizes)
    elif criteria == "saturation":
        argmax = np.argmax([rgb_to_saturation(*x) for x in centroids])
    elif criteria == "luminance":
        argmax = np.argmax([rgb_to_luminance(*x) for x in centroids])
    elif criteria == "luminosity":
        argmax = np.argmax([rgb_to_luminosity(*x) for x in centroids])
        
    winner = centroids[argmax,:]
    
    return rgb_to_hex(*winner)