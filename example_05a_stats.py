#!/usr/bin/python3

import numpy

#=======================================================================================================================
def main():
  in_file = "data_file.csv"
  fp_in = open(in_file, "r")

  ndata_list = []

  for in_data in fp_in:
    in_data = in_data.strip()             # remove leading and trailing whitespace

    data_list = in_data.split(",")        # make a list (data_list) from the comma-separated data items in in_data

    ndata = float(data_list[2])           # ndata is the third item in the list, in the form of a floating point number
    ndata = ndata * 10

    ndata_list.append(ndata)

  fp_in.close()

  # we have our list of data ready, so do some binning
  # see https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.histogram.html
  number_of_bins = 12
  (bins, bin_edges)  = numpy.histogram(ndata_list, number_of_bins)

  out_file = "binned_data.txt"            # setup and open the output file
  fp_out = open(out_file, "w")

  print_text = []                         # create an empty list
  for i in range(len(bins)):              # go through the bins array
    thisLine = str(bin_edges[i])          # and create a string containing this value of bin_edges
    thisLine += ",    "                   # append a comma and some spaces to the string
    thisLine += str(bins[i])              # append this value of bins to the string
    
    print_text.append(thisLine)           # append the string to the print_text list

  print_text.append(str(bin_edges[-1]))   # after the loop, append the last value of bin_edges to the print_text list
  
  for line in print_text:                 # go through the print_text list, item by item
    fp_out.write(line)                    # and write this item to the output file
    fp_out.write("\n")                    # write an end-of-line character to the output file

  fp_out.close()

  print("Data binned, end of run")
#=======================================================================================================================

main()
