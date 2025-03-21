#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 10:07:27 2025

@author: thosvarley
"""

import colorlib as cl

background = cl.load_desktop()

primary_color = cl.clustering_criteria_background(background)
header_color = "708090"

username = "FRAMEWORK 13"
split = username.split(" ")

network_address = "wlp1s0"

order = [
    "header",
    "system",
    "network",
    "ram",
    "memory",
    "cpu"
    ]

with open("conky.conf", "w") as config:

    for file in order:
        
        template_path = f"templates/{file}.conky"
       
        with open(template_path, "r") as template:
            
            contents = template.read()
            contents = contents.replace("#PRIMARY_COLOR", f"#{primary_color}")
            contents = contents.replace("#HEADER_COLOR", f"#{header_color}")
            
            if file == "system":
                contents = contents.replace("USER", split[0])
                contents = contents.replace("NAME", split[1])		
            if file == "network":
                contents = contents.replace("ID", network_address)
            
            config.write(contents)
            config.write("\n")
            
            if file == "header":
                config.write("conky.text = [[")
            
            template.close()
    
    config.write("]]")
    config.close() 
