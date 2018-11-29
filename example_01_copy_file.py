#!/usr/bin/python3

#=======================================================================================================================
def main():
  in_file = "some data file.txt"
  out_file = "copy of some data file.txt"

  fp_in = open(in_file, "r")
  fp_out = open(out_file, "w")

  for in_data in fp_in:          # do this section once for every line in the input file
    in_data = in_data.strip()    # remove leading and trailing whitespace

    fp_out.write(in_data)        # write in_data to the output file
    fp_out.write("\n")           # and also write an end-of-line character

  fp_in.close()
  fp_out.close()

  print("File copied, end of run")
#=======================================================================================================================

main()
