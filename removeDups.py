#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#remove duplicates from a list
schoolDupList = ["trees", "salamandar", "trees", "tropicalFish", "Edgar", "trees", "Matthew"]
schoolDeDup = list(dict.fromkeys(schoolDupList))
#print(schoolDeDup)

schoolDeDup2 = []
for pet in schoolDupList:
    if pet not in schoolDeDup2:
        schoolDeDup2.append(pet)
#print(schoolDeDup2)
