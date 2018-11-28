#!/usr/bin/python3

#=======================================================================================================================
def main():
  in_file = "data_file.csv"
  out_file = "new_data_file_1.txt"

  fp_in = open(in_file, "r")
  fp_out = open(out_file, "w")

  for in_data in fp_in:
    in_data = in_data.strip()             # remove leading and trailing whitespace

    data_list = in_data.split(",")        # make a list (called data_list) from the comma-separated data items in in_data

    fp_out.write(data_list[0])            # write out only the first item in the list (which starts with item zero)
    fp_out.write("\n")

  fp_in.close()
  fp_out.close()

  print("File 1 created, end of run")
#=======================================================================================================================

main()
