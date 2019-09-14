import sys
import parser_helper

def main(args):
  readList = []

  with open(args.file_name) as f:
    for line in f:
      line = line.rstrip()
      readList.append(line)

  indent_chars = "  "  # (2, 4, 8 spaces) or 1 tab

  print("{")
  print(indent_chars + "\"" + " ".join(args.name) + "\": {")

  def add_quotation(val):
    return "\"" + val + "\""

  mapped_prefix = map(add_quotation, args.prefix)

  print(indent_chars*2 + "\"prefix\": [ " + ", ".join(mapped_prefix) + " ],")
  print(indent_chars*2 + "\"body\": [")  
  
  # printing the code from the file
  for index, row in enumerate(readList):
    if index == 0:
      args.name

    print(indent_chars*3 + "\"" + row + "\"", end="")
    if index < len(readList) - 1: 
      print(",")
    else:
      print()   

  print(indent_chars*2 + "],")
  print(indent_chars*2 + "\"description\": \"" + " ".join(args.desc) +  "\"")

  print(indent_chars + "}")
  print("}")

if __name__ == "__main__":
  args = parser_helper.get().parse_args()
  main(args)