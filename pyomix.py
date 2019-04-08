##########################################################################
#  - PyOmiX - Analysis Workflow                                          #
#  - Python Script                                                       #
#  - April 9,2019                                                        #
#  - Copyright: Ahmed Omar, Mohamed Magdy, Usama Bakry, and Waleed Amer  #
#  - Nile University                                                     #
##########################################################################

## project Description ..
print('PyOmiX v0.1 | by Ahmed Omar, Mohamed Magdy, Usama Bakry and Waleed Amer\n'
      , 'Check https://github.com/ubakry/pyomix for updates.\n')

# Importing libraries
import os
import argparse
import subprocess

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
    parser.add_argument('-d', action="store", required=True, help='fasta file well be used as refrance for alignment')

    # optional arguments
    parser.add_argument('-o', action="store", help='The output directory', default='.')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    arguments = vars(parser.parse_args())
    return arguments
# ----------------------------------------------------------------------

if __name__ == '__main__':
    args = get_args()

# ----------------------------------------------------------------------
# create refrance database for alignment using diamond (makedb)
print('create refrance database for alignment using diamond (makedb)')
make_db = ['diamond', 'makedb', '--in', args['d'], '-d', 'db']
make_db_proc = subprocess.Popen(make_db, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# check the process
stdout, stderr = make_db_proc.communicate()
print(stderr.decode())

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

# ----------------------------------------------------------------------
# function for alignment using diamond
# ----------------------------------------------------------------------

def diamond_align(fasta):
    # alignment using blastp
    diamond = ['diamond', 'blastp', '-q', fasta, '-d', 'db.dmnd', '-f', '6', 'qseqid', '-o', 'id_list.fa']
    diamond_proc = subprocess.Popen(diamond, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = diamond_proc.communicate()
    print(stderr.decode())
