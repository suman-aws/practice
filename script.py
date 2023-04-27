import argparse

# Create an argument parser
parser = argparse.ArgumentParser()

# Add the command line arguments
parser.add_argument('--var1', type=str, help='Description of var1')
parser.add_argument('--var2', type=str, help='Description of var2')

# Parse the command line arguments
args = parser.parse_args()

# Retrieve the values of the variables
var1 = args.var1
var2 = args.var2

# ... use var1 and var2 in your script ...
