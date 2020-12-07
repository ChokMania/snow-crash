# coding: utf-8
import argparse

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("str", help="file to decrypt")
	args = parser.parse_args()
	args.str = args.str.encode("utf-8", "surrogateescape")
	for i in range(len(args.str)):
		print(chr(args.str[i] - i), end="")
	print()
