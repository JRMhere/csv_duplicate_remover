import csv
import sys


def rm_dup_rows(inl):
    #inl = a list of dicts, per csv.DictReader input
    nl = []
    for item in inl:
        if item not in nl:
            nl.append(item)
    return nl #a list of dictionaries

def rm_by_col(inl):
    #inl = a list of dicts, per csv.DictReader input

    #Each column gets its own list in the new dictionary of lists.
    #For each column, add its entry to that corresponding list only if it's not already in the list.
    #Then return the dictionary.

    nl = {}
    for item in inl: #item = dictionary
        for ent in item: #ent = column header
            if ent not in nl:
                nl[ent] = []
            if item[ent] not in nl[ent]:    
                nl[ent].append(item[ent])
    return nl

def dl_to_ld(inl):
    #inl = a dictionary of lists.

    #example of dictionary of lists - {'x': [1, 5], 'y': [2, 6], 'z': [3], 'a': [4], 'b': [5], 'c': [6], 'd': [7], 'e': [8], 'f': [9]}
    il = inl.items()
    nl = []
    nl.append({})
    #Determine the maximum length of one of the lists in inl.
    maxlen = 0 #this will ultimately be the length of the list of dictionaries - the number of dictionaries in the list.
    for item in il:
        if maxlen < len(item[1]):
            maxlen = len(item[1])
            for i in range(len(nl), maxlen):
                nl.append({})
        for i in range(len(item[1])):
            nl[i][item[0]] = item[1][i]
    return nl #list of dictionaries

def ld_to_dl(inl):
    #inl = a list of dictionaries.

    #TODO convert a list of dictionaries into a dictionary of lists.
    pass

def remove_duplicates(infile, outfile, wholeRow):
    #infile = the address of the file to be converted.
    #outfile = address to write to
    #wholeRow = True if we want to remove duplicate rows, False if we're dealing at the column level.
    l = []
    with open(infile, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            l.append(row)
    if wholeRow:
        o = rm_dup_rows(l)
        o = dl_to_ld(o)
    else:
        o = rm_by_col(l)
    with open(outfile, 'w', newline='') as csvfile:
        #when this is called, o should be a list of dictionaries by this point.
        fieldnames = []
        for item in o[0]:
            fieldnames.append(item)
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in o:
            writer.writerow(row)