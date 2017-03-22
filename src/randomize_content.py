#!/usr/bin/python
import sys
import random
import argparse

def main(argv):
	parser = argparse.ArgumentParser()
	parser.add_argument("--input", required=True, help="input file name located in the files folder")
	parser.add_argument("--output", help="file name of the output to be located in the output folder")
	parser.add_argument("--count", type=int, help="number of items to be printed")
	args = parser.parse_args()
	filename = args.input + ".txt"
	inputFile = "files/" + filename
	outputFile = "output/" + filename
	if args.output is not None:
		outputFile = "output/" + args.output + ".txt"
	content = get_all_lines(inputFile)
	content = get_shuffled_items(content, args.count)
	write_reviewer(outputFile, content)

def get_all_lines(inputFile):
	with open(inputFile) as f:
		content = f.readlines()
	return content

def get_shuffled_items(content, count = None):
	random.shuffle(content)
	if count is not None and count < len(content): 
		return content[0:count]
	return content

def write_reviewer(outputFile, content):
	with open(outputFile, "w") as f:
		f.writelines(content)

if __name__ == "__main__":
   main(sys.argv[1:])