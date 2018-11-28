#!/usr/bin/python3

#=======================================================================================================================
def main():
  in_file = "some data file.txt"
  out_file = "error-free data file.txt"

  fp_in = open(in_file, "r")
  fp_out = open(out_file, "w")

  for in_data in fp_in:
    in_data = in_data.strip()             # remove leading and trailing whitespace

    if in_data.find("Updating") >= 0:     # look for the word "Updating" in in_data
      continue                            # if it is found, continue with the next iteration of the loop

    fp_out.write(in_data)                 # not found, so write out in_data
    fp_out.write("\n")

  fp_in.close()
  fp_out.close()

  print("Errors removed, end of run")
#=======================================================================================================================

main()
