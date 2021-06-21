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


import networkx as nx

__author__ = "Pau Riba, Anjan Dutta"
__email__ = "priba@cvc.uab.cat, adutta@cvc.uab.cat"

if __name__ == '__main__':

    path_dataset = './test/data/'
    #name_dataset = 'Letters'
    name_dataset = 'AIDS-train'



    aed = VanillaAED()
    hed = VanillaHED()

    path_dataset = os.path.join(path_dataset, name_dataset)
    #files = glob.glob(path_dataset + '/*.gml')
    files = glob.glob(path_dataset + '/*.gexf')

    start = time.time()
    for f1, f2 in itertools.combinations_with_replacement(files, 2):
        # Read graphs
        # g1 = nx.read_gml(f1)
        # print(g1)
        # g2 = nx.read_gml(f2)


        g1 = nx.read_gexf(f1)

        g2 = nx.read_gexf(f2)






        # Distance AED
        distAED, _ = aed.ged(g1, g2)

        # Distance HED
        distHED, _ = hed.ged(g1, g2)


        #print(g1.graph['class'] + ' <-> ' + g2.graph['class'] + ' | HED: ' + str(distHED) + ' AED: ' + str(distAED) + ' | ' + str(distHED<=distAED) + (' Exact GED ' if distHED==distAED else ''))
        print(f1 + '<-> ' + f2 + ' | HED: ' + str(distHED) + ' AED: ' + str(distAED) + ' | ' + str(distHED<=distAED) + (' Exact GED ' if distHED==distAED else ''))
    end =  time.time()

    print(end-start)
