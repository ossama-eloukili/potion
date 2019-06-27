#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:09:49 2019

@author: matteo
"""
import math

def gauss_smooth_const(max_feat, std):
    psi = 2 * max_feat / (math.sqrt(2 * math.pi) * std)
    kappa = max_feat**2 / std**2
    xi = max_feat**2 / std**2
    return psi, kappa, xi

def std_smooth_const():
    psi = 4 / math.sqrt(2 * math.pi * math.e)
    kappa = 2
    xi = 2
    return psi, kappa, xi

def gibbs_smooth_const(max_feat, temp):
    psi = 2 * max_feat / temp
    kappa = 4 * max_feat**2 / temp**2
    xi = 2 * max_feat**2 / temp**2
    return psi, kappa, xi

def gauss_lip_const(max_feat, max_rew, disc, std):
    lip = 2 * max_feat**2 * max_rew / (std* (1 - disc))**2 * (
            1 + 2 * disc / (math.pi * (1 - disc)))
    return lip

def std_lip_const(max_rew, disc):
    lip = 4 *  max_rew / (1 - disc)**2 * (
            1 + 4 * disc / (math.pi * math.e * (1 - disc)))
    return lip

def gibbs_lip_const(max_feat, max_rew, disc, temp):
    lip = 2 * max_feat**2 * max_rew / (temp * (1 - disc))**2 * (
            3 + 4 * disc / (1 - disc))
    return lip

def pirotta_coeff(max_feat, max_rew, disc, std, action_vol):
    return max_rew * max_feat**2 / ((1 - disc)**2 * std**2) * \
            (action_vol / (math.sqrt(2 * math.pi) * std) + disc 
             / (2 * (1 - disc)))