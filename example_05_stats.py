#!/usr/bin/python3

import numpy

#=======================================================================================================================
def main():
  in_file = "data_file.csv"
  fp_in = open(in_file, "r")

  ndata_list = []

  for in_data in fp_in:
    in_data = in_data.strip()             # remove leading and trailing whitespace

    data_list = in_data.split(",")        # make a list (indata) from the comma-separated data items

    ndata = float(data_list[2])           # ndata is the third item in the list, in the form of a floating point number
    ndata = ndata * 10

    ndata_list.append(ndata)

  fp_in.close()

  # we have our list of data ready, so do some binning
  # see https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.histogram.html
  number_of_bins = 6
  bins = numpy.histogram(ndata_list, number_of_bins)

  print(bins)

  print("Calculated stats, end of run")
#=======================================================================================================================

main()
