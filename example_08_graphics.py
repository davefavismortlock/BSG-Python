#!/usr/bin/python3

import matplotlib.pyplot as plt


#=======================================================================================================================
def main():
  in_file = "data_file.csv"
  fp_in = open(in_file, "r")

  ndata_list = []

  for in_data in fp_in:
    in_data = in_data.strip()             # remove leading and trailing whitespace

    data_list = in_data.split(",")        # make a list (indata) from the comma-separated data items

    ndata = float(data_list[2])           # ndata is the third item in the list, in the form of a floating point number
    ndata = ndata * 1000                  # make the numbers a bit bigger (so it is easier to read labels on graph)

    ndata_list.append(ndata)

  fp_in.close()

  n, bins, patches = plt.hist(ndata_list, 50)   # set up a histogram using data_list, with 50 bins
  plt.show()                                    # and plot it

  print("Data graphed, end of run")
#=======================================================================================================================

main()


