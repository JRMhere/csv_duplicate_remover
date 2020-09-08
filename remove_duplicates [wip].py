import csv
import sys


def rm_dup_rows(inl):
    #inl = a list of dicts, per csv.DictReader input
    #TODO any row that is a duplicate will be removed. Then return the list of dictionaries.

    pass

def rm_by_col(inl):
    #inl = a list of dicts, per csv.DictReader input

    #TODO Go through each item in the list of dictionaries.
    #Each column gets its own list in the new dictionary of lists.
    #For each column, add its entry to that corresponding list only if it's not already in the list.
    #Then return the dictionary.

    pass

def dl_to_ld(inl):
    #inl = a dictionary of lists.

    #TODO convert a dictionary of lists into a list of dictionaries.

    pass

def ld_to_dl(inl):
    #inl = a list of dictionaries.

    #TODO convert a list of dictionaries into a dictionary of lists.

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
        writer = csv.DictWriter(csvfile)
        for row in o:
            writer.writerow(row)