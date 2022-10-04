# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 10:24:21 2022

@author: alber
"""

import beam_solver

data = [
    {
        "length" : 8000,
        "width" : 250,
        "depth" : 400,
        "fc_prime" : 28,
        "fy" : 420,
        "cc" : 40,
        "conc_gamma" : 2400, ##kgs.cu.m
        "phi" : 0.9,
        "type" : "simply supported",
        "live" : 45,
        "dead" : 28.46
        },

    {
        "length" : 5000,
        "width" : 250,
        "depth" : 400,
        "fc_prime" : 28,
        "fy" : 420,
        "cc" : 40,
        "conc_gamma" : 2400, ##kgs.cu.m
        "phi" : 0.9,
        "type" : "simply supported",
        "live" : 45,
        "dead" : 28.46
    },
    {
        "length" : 10000,
        "width" : 250,
        "depth" : 400,
        "fc_prime" : 28,
        "fy" : 420,
        "cc" : 40,
        "conc_gamma" : 2400, ##kgs.cu.m
        "phi" : 0.9,
        "type" : "simply supported",
        "live" : 45,
        "dead" : 28.46
    }
]

for i in data: 
    print(beam_solver.beamMoment(i))

# print(beam_solver.beamMoment(data))