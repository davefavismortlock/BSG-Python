#!/usr/bin/python3

#=======================================================================================================================
def main():
  in_file = "data_file.csv"
  out_file = "no_0.0005_data_file.txt"

  fp_in = open(in_file, "r")
  fp_out = open(out_file, "w")

  for in_data in fp_in:
    in_data = in_data.strip()             # remove leading and trailing whitespace

    data_list = in_data.split(",")        # make a list (data_list) from the comma-separated data items

    ntest = float(data_list[1])           # read the second item in data_list as a floating-point number
    if ntest == 0.0005:                   # is this number equal to 0.0005?
      continue                            # it is, so skip the rest of the loop

    fp_out.write(data_list[0])            # it isn't, so write out the first item in the list
    fp_out.write("\n")

  fp_in.close()
  fp_out.close()

  print("Errors removed, end of run")
#=======================================================================================================================

main()
