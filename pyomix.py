##########################################################################
#  - PyOmiX - Analysis Workflow                                          #
#  - Python Script                                                       #
#  - April 29,2019                                                       #
#  - Copyright: Ahmed Omar, Mohamed Magdy, Usama Bakry, and Waleed Amer  #
#  - Nile University                                                     #
##########################################################################

# ----------------------------------------------------------------------
# Importing libraries
# ----------------------------------------------------------------------
import re
import requests
import subprocess
import argparse
import os

porj_dir=os.getcwd()
# project Description
print('========================================================================')
print('PyOmiX v1.0 | by Ahmed Omar, Mohamed Magdy, Usama Bakry and Waleed Amer.')
print('Check https://github.com/ubakry/pyomix for updates.')
print('========================================================================')

args = None

# ----------------------------------------------------------------------


def get_args():
    """"""
    parser = argparse.ArgumentParser(
        description="PyOmiX - Analysis WorkFlow",
        epilog="This is where you might put example usage"
    )

    # required argument
    parser.add_argument('-i', action="store", required=True,
                        help='Swiss-Prot ids txt file directory')
    parser.add_argument('-d', action="store", required=True,
                        help='fasta file well be used as refrance for alignment')

    # optional arguments
    parser.add_argument('-o', action="store",
                        help='The output directory', default='.')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    arguments = vars(parser.parse_args())
    return arguments
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Creating reference database for alignment using DIAMOND (makedb)
# ----------------------------------------------------------------------


def makedb():
    print('create refrance database for alignment using diamond (makedb)')
    make_db = ['diamond', 'makedb', '--in', args['d'], '-d', 'db']
    make_db_proc = subprocess.Popen(
        make_db, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # check the process
    stdout, stderr = make_db_proc.communicate()
    print(stderr.decode())
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Function to download FASTA File from UniProt and NCBI
# ----------------------------------------------------------------------


def getfasta(id):
    if re.search(r"[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2}", id):
        parameters = {"query": id, "format": "fasta"}
        fasta = requests.get(
            "https://www.uniprot.org/uniprot/", params=parameters)
        fastafile = open(id + ".fasta", "w")
        fastafile.write(fasta.text)
        fastafile.close()
    elif re.search(r"[A-Z][0-9]{5}[.][0-9]|[A-Z]{2}[A-Z_][0-9]{5,9}[.][0-9]", id):
        parameters = {"db": "protein", "id": id,
                      "rettype": "fasta", "retmode": "text"}
        fasta = requests.get(
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi", params=parameters)
        fastafile = open(id + ".fasta", "w")
        fastafile.write(fasta.text)
        fastafile.close()
    else:
        print("Wrong ID .. Check your IDs list")
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Function to make directories for SWISS-Prot ids
# ----------------------------------------------------------------------


def makdirs(file, parent_dir="/pymoix-results"):
    if parent_dir == "/pymoix-results":
        os.mkdir(args['o'] + parent_dir, int(0o755))
        os.chdir(args['o'] + parent_dir)
        for id in file:
            os.mkdir(str(os.getcwd())+"/"+id.rstrip("\n"), int(0o755))
            os.chdir(str(os.getcwd())+"/"+id.rstrip("\n"))
            getfasta(id.rstrip("\n"))
            os.chdir(args['o'] + parent_dir)
    else:
        os.mkdir(args['o'] + "/pymoix-results" + parent_dir +
                 "/"+"align_accessions", int(0o755))
        os.chdir(args['o'] + "/pymoix-results" +
                 parent_dir+"/"+"align_accessions")
        for id in file:
            getfasta(id.rstrip("\n"))
        merge(args['o'] + "/pymoix-results" +
              parent_dir+"/"+"align_accessions/")
        os.chdir(args['o'] + "/pymoix-results")

# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Function for alignment using DIAMOND
# ----------------------------------------------------------------------
def diamond_align(fasta):
	# alignment using blastp
	diamond = ['diamond', 'blastp', '-q', fasta, '-d', 'db.dmnd', '-f', '6', 'qseqid', '-o', args['o'] +"/pymoix-results"+#####+'id_list.txt']
	diamond_proc = subprocess.Popen(diamond, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stdout, stderr = diamond_proc.communicate()
	print(stderr.decode())
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Function to merge multiple fasta files in one fasta file.
# ----------------------------------------------------------------------


def merge(dir):
    print('Merging multiple fasta files in one fasta file')
    files = dir + '*.fasta'
    out = dir + 'all.fasta'
    os.system('cat ' + files + ' > ' + out)
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Function to perform multiple sequence alignment.
# ----------------------------------------------------------------------


def clustalo(file):
    print('Performing multiple sequence alignment.')
    os.system("python3 "+ porj_dir +"/modules/clustalo.py -i "+file+" -o clustal-res.fasta")
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Function to create a phylogenetic tree.
# ----------------------------------------------------------------------


def phylo(file):
    print('Creating the phylogenetic tree.')
    os.system("python3 "+ porj_dir +"/modules/simple_phylogeny.py --sequence "+file+" --email info@pyomix.com")
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Main function
# ----------------------------------------------------------------------


def main():
    file = open(args['i'])
    makdirs(file)
    file.close()
# ----------------------------------------------------------------------


if __name__ == '__main__':
    args = get_args()
    main()
