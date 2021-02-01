#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 19:39:57 2021

@author: thomas
"""

import numpy as np


# calculate sample mean

def samp_mean(x,x_mu_prev,N):
    return (1/N)*(x + (N-1)*x_mu_prev)


if __name__ == '__main__':
    
    N = 10
    x = np.arange(10)
    
    x_mu    = 0
    mu_prev = 0
    for i in range(N):
        x_mu    = samp_mean(x[i],mu_prev,i+1)
        mu_prev = x_mu
        print(x_mu)
        