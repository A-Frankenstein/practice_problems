#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#create a dict from a list
schoolList = ["trees", "salamandar", "tropicalFish", "Edgar", "Matthew", "Tony", "gerbil", "whitemice"]
schoolVals = "x"
schoolDict = dict.fromkeys(schoolList, schoolVals)
#print(schoolDict)

schoolDict2 = {}
for pet in schoolList:
    schoolDict2[pet] = "o"
#print(schoolDict2)
