#!/usr/bin/python3

#=======================================================================================================================
def main():
  in_file = "data_file.csv"
  out_file = "new_data_file_3.txt"

  fp_in = open(in_file, "r")
  fp_out = open(out_file, "w")

  for in_data in fp_in:
    in_data = in_data.strip()             # remove leading and trailing whitespace

    data_list = in_data.split(",")        # make a list (data_list) from the comma-separated data items in in_data

    fp_out.write(data_list[0])            # write out the first item in the list (starts with item zero)
    fp_out.write("\t\t")

    ndata = float(data_list[2])           # ndata is the third item in the list, in the form of a floating point number
    ndata = ndata * 35.567

    fp_out.write("%7.6f" % ndata )        # write out the newly-calculated number
    fp_out.write("\n")

  fp_in.close()
  fp_out.close()

  print("File 3 created, end of run")
#=======================================================================================================================

main()
