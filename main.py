#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    main.py

    Distance computation and comparison between different aproximated graph edit distance techniques with the same costs.
"""

from aproximated_ged.VanillaAED import VanillaAED
from aproximated_ged.VanillaHED import VanillaHED

import os
import glob
import time
import itertools
import numpy as np


import networkx as nx

__author__ = "Pau Riba, Anjan Dutta"
__email__ = "priba@cvc.uab.cat, adutta@cvc.uab.cat"

if __name__ == '__main__':

    path_dataset = './test/data/'
    #name_dataset = 'Letters'
    #name_dataset = 'AIDS-train'
    name_dataset = 'NCI1'





    aed = VanillaAED()
    hed = VanillaHED()

    path_dataset = os.path.join(path_dataset, name_dataset)
    #files = glob.glob(path_dataset + '/*.gml')
    files = glob.glob(path_dataset + '/*.gml')
    files_sorted = sorted(files, key = lambda file :  int(file.split("/")[-1].split(".")[0])) # 1-4000 排序

    graph_list = [nx.read_gml(i) for i in files_sorted]

    start = time.time()

    aed_array = np.zeros((len(graph_list), len(graph_list)))
    hed_array = np.zeros((len(graph_list), len(graph_list)))

    for i in range(len(graph_list)):
        for j in range(len(graph_list) - i):
            distAED, _ = aed.ged(graph_list[i], graph_list[j+i])
            distHED, _ = hed.ged(graph_list[i], graph_list[j+i])
            aed_array[i, j+i] = distAED
            hed_array[i, j+i] = distHED
            #print(str(i) + '<-> ' + str(j) + ' | HED: ' + str(distHED) + ' AED: ' + str(distAED) + ' | ' + str(distHED<=distAED) + (' Exact GED ' if distHED==distAED else ''))






    np.save('aed_array.npy', aed_array)
    np.save('hed_array.npy', hed_array)
    end =  time.time()
    print(end-start)




    # for f1, f2 in itertools.combinations_with_replacement(files, 2):
    #     # Read graphs
    #     # g1 = nx.read_gml(f1)
    #     # print(g1)
    #     # g2 = nx.read_gml(f2)

    #     print(f1)
    #     print(int(f1.split("/")[-1].split(".")[0]))

    #     # g1 = nx.read_gexf(f1)
    #     # g2 = nx.read_gexf(f2)
    #     g1 = nx.read_gml(f1)
    #     g2 = nx.read_gml(f2)

    #     # Distance AED
    #     distAED, _ = aed.ged(g1, g2)

    #     # Distance HED
    #     distHED, _ = hed.ged(g1, g2)
    #     #print(g1.graph['class'] + ' <-> ' + g2.graph['class'] + ' | HED: ' + str(distHED) + ' AED: ' + str(distAED) + ' | ' + str(distHED<=distAED) + (' Exact GED ' if distHED==distAED else ''))
    #     print(f1 + '<-> ' + f2 + ' | HED: ' + str(distHED) + ' AED: ' + str(distAED) + ' | ' + str(distHED<=distAED) + (' Exact GED ' if distHED==distAED else ''))
    # end =  time.time()

    print(end-start)
