#! /usr/bin/env python
#### TODO CLI for find folder or check files present in pwd 
#### output to defined folder or std out
#### take GOI input (firect string/ file inojt?)
#### check if files exist folders use os. library.

#GOI = "speA2" # set gene of interest (GOI) to user input
#GOI= "group_3687"

import argparse
import sys
from os.path import exists


def support_script(args):
    GOI = args.gene_of_interest
    Input_file = args.input_file

    Gene_list = {}
    accessory_list = {} #set up accessory list dictionary
    core_list = {} # set up core list dictionary
    count_core = {} # have a count for the number of times a GOI occurs between a particular core pair
    with open(Input_file, "r") as fp:
        #line = fp.readline()
        #cnt = 1
        #while line: # while loops sow for loops fast, switch to for.
        for line in fp.readlines():
            #print("Line {}: {}".format(cnt, line.strip()))
            line_list = (line.strip().split('\t'))
            if (GOI in line_list): # if the GOI is one of the core or accessory genes
                genome=(line_list[0]) # set genome ID
                core1=(line_list[1]) # set core gene 1
                core2=(line_list[2]) # set core gene 2
                acces=(line_list[3]) # set accessory gene
                Gene_list[genome] = [core1, core2,acces] # set {Genome : [genes]} dictionary
                
                if (acces == GOI): # only count lines where the accessory gene is GOI
                    accessory_list[genome] = [core1, core2,acces] # make dictionary of genome 
                    core_pair = str("{} and {}".format(core1,core2)) # make hashable object of gene pairs
                    
                    if core_pair in count_core: # if the pair has been seen before increase the occurences
                        count_core[core_pair] += 1
                        
                    else: # if a novel core_core pair start the count
                        count_core[core_pair] = 1
                    ##TODO case where genome appears multiple times
                    print("{} is an accessory gene between genes {} and {} in {}". format(GOI,core1,core2,genome))
                
                elif (core1 == GOI or core2 == GOI):
                    ##TODO case where GOI is a core gene
                    ## TODO add f instead of format
                    print("{} is a core gene between genes {} and {} in {}". format(GOI,core1,core2,genome))
                
                else :
                    print("This is weird your gene of interest {} is in the file but doesn't appear to be located in the expected columns of the table provided, make sure you have the correct corekaburra input file.".format(GOI))
            #else:
                
                #print("your gene of interest {} doesn't appear to be located in the table provided, make sure you have the exact gene name provided in the pangenome output files.".format(GOI))
                    #print(Gene_list)
            #line = fp.readline()
            #cnt += 1
        #print(accessory_list)
        #print(count_core)
    for core_pair_set in count_core.keys():
        print(f"GOI {GOI} occurs between {core_pair_set} {count_core[core_pair_set]} times in your pangenome")
        #get result of occurences between core_core_pairs
    print(len(Gene_list))



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Summarise the location of a Gene of interest in the pangenome relative to core-core pairs defined by Corekaburra")
    parser.add_argument("-if", "--input_file", 
                        help="requires corekaburra core_core_accessory_gene_content.tsv", 
                        type=str, required=True)
    parser.add_argument("-goi", "--gene_of_interest", 
                        help="the group name of the gene of interest from your pangenome", type=str, required=True)
    args = parser.parse_args()
    support_script(args)