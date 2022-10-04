
"""
Created on Tue Oct  4 08:31:35 2022

@author: user
"""

import math

def ceil(x, s):
    return s * math.ceil(float(x)/s)

##Loads
Live = 45
Dead = 28.46

data = {
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
        }

def beamMoment(data):
    ##Preliminary Sizing
    wu = (1.2*data["live"]+1.6*data["live"])/data["length"]
    def minDepth(type,length): ##milimeter
        if(type == "both ends continuous"):
            depth_min = length/21
        elif(type == "simply supported") :
            depth_min = length/16
        return ceil(depth_min,100)
    
    def momentInertia(b,h):
        inertia = (b*pow(h,3))/12
        return inertia
    
    dep_req = minDepth(data["type"],data["length"])
    sw_beam = data["conc_gamma"]*data["width"]*dep_req*(9.81/pow(1000,3))
    # print(sw_beam)
    
    fc = round(0.45*data["fc_prime"],2)
    fs = round(0.6*data["fy"],2)
    
    def beta(fc_input): 
        if(fc_input<=28):
            beta_1 = 0.85
        else:
            if(fc_input>=55):
                beta_1 = 0.65
            else:
                beta_1 = round(0.85-0.05*(fc_input-28)/7,2)
        return beta_1
            
            
    rho_b = 0.85*beta(data["fc_prime"])*data["fc_prime"]*600/(data["fy"]*(600+data["fy"]))
    rho_max = 0.75*rho_b
    q = rho_max*data["fy"]/data["fc_prime"]
    
    ##Beam Design Calculation (For Singly Reinforced)
    Mu_actual = round((wu*pow(data["length"],2))/(8*pow(10,6)),2)
    mu_max = 0.9*data["width"]*dep_req*data["fy"]*rho_max*(1-0.59*q)/1000000
    
    return mu_max

# print( beamMoment(data) )
# if(Mu_actual>Mu_max1):
    
#     Type_r = "Doubly Reinforced"
# else:
#     Type_r = "Singly Reinforced"

# ##First Iteration
# Ku = round(rho_b*fy*(1-0.59*q),4)

# if(Type_r=="Singly Reinforced"):
    
#     bd_squared = round((Mu_actual*pow(10,6))/(phi*Ku),2)
#     d = round(pow(bd_squared/0.5,1/3),2)
#     d = ceil(d,50)
#     b = round(d*0.75,2)
#     h = round(d+cc,2)
#     W_beam = round(23.6*b*h/pow(10,6),2)
#     Wu1 = round(W_beam+Wu,2)
#     if(Wu1>Wu):
#         Condition = "change Wb"
#     else:
#         Condition = "accept Wb"
# else:
#     bd_squared = ""
#     d = ""
#     d = ""
#     b = ""
#     h = ""
#     W_beam = ""
#     Wu1 = ""


# print(d)