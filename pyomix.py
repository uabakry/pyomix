##########################################################################
#  - PyOmiX - Analysis Workflow                                          #
#  - Python Script                                                       #
#  - April 1,2019                                                        #
#  - Copyright: Ahmed Omar, Mohamed Magdy, Usama Bakry, and Waleed Amer  #
#  - Nile University                                                     #
##########################################################################

# Importing libraries
import os
import argparse

args = None

# ----------------------------------------------------------------------
def get_args():
    """"""
    parser = argparse.ArgumentParser(
        description="PyOmiX - Analysis WorkFlow",
        epilog="This is where you might put example usage"
    )

    # required argument
    parser.add_argument('-i', action="store", required=True, help='Swiss-Prot ids txt file directory')

    # optional arguments
    parser.add_argument('-o', action="store", help='The output directory', default='.')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    arguments = vars(parser.parse_args())
    return arguments
# ----------------------------------------------------------------------

if __name__ == '__main__':
    args = get_args()

# Function to make directories for swiss-prot ids
# ----------------------------------------------------------------------
def makdirs(file):
    os.mkdir(args['o'] + "/pymoix-results", int(0o755))
    os.chdir(args['o'] + "/pymoix-results")
    for line in file:
        os.mkdir(str(os.getcwd())+"/"+line.rstrip("\n"), int(0o755))
# ----------------------------------------------------------------------

file = open(args['i'])
makdirs(file)
file.close()