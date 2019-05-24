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

# Setting the project directory in a variable
proj_dir=os.getcwd()
# project Description
print('========================================================================')
print('PyOmiX v1.0 | by Ahmed Omar, Mohamed Magdy, Usama Bakry and Waleed Amer.')
print('Check https://github.com/uabakry/pyomix for updates.')
print('========================================================================')

args = None

# ----------------------------------------------------------------------
# Getting arguments from user using command line.
# ----------------------------------------------------------------------
def get_args():
	""""""
	# Creating argument parser object
	parser = argparse.ArgumentParser(
		description="PyOmiX - Analysis WorkFlow",
		epilog="This is where you might put example usage"
	)

	# required arguments
	parser.add_argument('-i', action="store", required=True,
						help='Swiss-Prot ids txt file directory')
	parser.add_argument('-d', action="store", required=True,
						help='The reference database')

	# optional arguments
	parser.add_argument('-o', action="store",
						help='The output directory', default='.')
	parser.add_argument('--version', action='version', version='%(prog)s 1.0')

	# Converting the arguments to a dictionary (keys -> args names and values -> user values)
	arguments = vars(parser.parse_args())
	return arguments
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Creating reference database for alignment using DIAMOND (makedb command).
# ----------------------------------------------------------------------
def makedb():
	# Printing on terminal
	print('[    PROCESS    ] Creating refrance database for alignment using diamond (makedb command)...')
	# Running the makedb command
	# --in -> the input database
	# -d -> the output indexed database that will be used in alignment
	os.system(proj_dir+'/modules/diamond makedb --in \''+ args['d']+ '\' -d '+args['o']+'db')
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Downloading FASTA File from UniProt and NCBI.
# ----------------------------------------------------------------------
def getfasta(id):
	# Printing on terminal
	print('[    PROCESS    ] Downloading fasta file of the id: '+id+'...')
	# IF the id matches the uniprot id regular expression
	if re.search(r"[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2}", id):
		# Setting parameters for the request
		parameters = {"query": id, "format": "fasta"}
		# Requesting the fasta file from uniprot
		fasta = requests.get(
			"https://www.uniprot.org/uniprot/", params=parameters)
		# Creating fasta file and writing the requested squence in the file
		fastafile = open(id + ".fasta", "w")
		fastafile.write(fasta.text)
		fastafile.close()
	# IF the id matches the ncbi id regular expression
	elif re.search(r"[A-Z][0-9]{5}[.][0-9]|[A-Z]{2}[A-Z_][0-9]{5,9}[.][0-9]", id):
		# Setting parameters for the request
		parameters = {"db": "protein", "id": id,
					  "rettype": "fasta", "retmode": "text"}
		# Requesting the fasta file from ncbi
		fasta = requests.get(
			"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi", params=parameters)
		# Creating fasta file and writing the requested squence in the file
		fastafile = open(id + ".fasta", "w")
		fastafile.write(fasta.text)
		fastafile.close()
	else:
		# Printing the error message if the id doesn't match the uniprot or ncbi regular expression
		print("[     ERROR     ] Wrong ID .. Check your IDs list")
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Alignment using DIAMOND (blastp command).
# ----------------------------------------------------------------------
def diamond_align(fasta,id):
	# Printing on terminal
	print('[    PROCESS    ] Aligning fasta file of the id: '+id+'...')
	# Running the blastp command
	# -q -> the input fasta file
	# -d -> the output indexed database that will be used in alignment
	# -f -> the output format
	# -o -> the output file name
	os.system(proj_dir+'/modules/diamond blastp -q '+ fasta+ ' -d '+args['o']+'/db.dmnd -f 6 sseqid -o '+id+'_id_ls.txt')
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Merging fasta files in one fasta file.
# ----------------------------------------------------------------------
def merge(dir):
	# Printing on terminal
	print('[    PROCESS    ] Merging fasta files...')
	files = dir + '/*.fasta'
	out = dir + '/all.fasta'
	# Running the cat command
	# files -> all fasta files
	# out -> the merged fasta file
	os.system('cat ' + files + ' > ' + out)
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Performing multiple sequence alignment.
# ----------------------------------------------------------------------
def clustalo(file,id):
	# Printing on terminal
	print('[    PROCESS    ] Performing multiple sequence alignment...')
	# Running the clustalo python script
	# --sequence -> the input fasta file
	# --stype -> sequences type
	# --outfile -> the output files name
	# --email -> the user's email
	os.system("python3 "+ proj_dir +"/modules/clustalo.py --sequence "+file+" --stype protein --outfile "+id+"_clustal_res --email ubakry94@gmail.com")
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Making directories for ids
# ----------------------------------------------------------------------
def makdirs(file, parent_dir="/pymoix-results"):
	# Checking if parent directory of the input file is /pyomix-results 
	if parent_dir == "/pymoix-results":
		# Creating the pyomix-results directory
		os.mkdir(args['o'] + parent_dir, int(0o755))
		# Changing the working directory to pyomix-results
		os.chdir(args['o'] + parent_dir)
		# Looping on all ids in the file
		for id in file:
			# Removing \n from each id
			id=id.rstrip("\n")
			# Creating variable with the directory path for the id
			id_dir_path=str(os.getcwd())+"/"+id
			# Creating the id directory
			os.mkdir(id_dir_path, int(0o755))
			# Changing the working directory to id directory
			os.chdir(id_dir_path)
			# Calling getfasta() function
			getfasta(id)
			# Creating variable with the directory path of id fasta file
			fa_path=id_dir_path+"/"+id+".fasta"
			# Checking if the fasta file is existed
			exists = os.path.isfile(fa_path)
			if exists:
				# Calling the alignment function
				diamond_align(fa_path,id)
				# Creating variable with directory path of ids list file
				ids_file=open(id_dir_path+"/"+id+"_id_ls.txt")
				# Calling makdirs function
				makdirs(ids_file,"/"+id)
				# Closing the ids list file
				ids_file.close()
				# Creating variable with directory path of merged fasta file
				all_file=id_dir_path+"/align_accessions/all.fasta"
				# Calling clustalo function
				clustalo(all_file,id)
			# Changing the working directory to the parent directory
			os.chdir(args['o'] + parent_dir)
	else:
		dir_path=args['o'] + "/pymoix-results" + parent_dir + "/align_accessions"
		# Creating the align_accessions directory
		os.mkdir(dir_path, int(0o755))
		# Changing the working directory to align_accessions
		os.chdir(dir_path)
		# Looping on all ids in the file
		for id in file:
			# Removing \n from each id
			id=id.rstrip("\n")
			# Calling getfasta() function
			getfasta(id)
		# Calling merging fasta function
		merge(dir_path)
		# Changing the working directory to the parent directory
		os.chdir(args['o'] + "/pymoix-results" + parent_dir)
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# Main function
# ----------------------------------------------------------------------
def main():
	# Opening the input file that containing swiss-prot ids
	file = open(args['i'])
	# Calling makedb() function
	makedb()
	# Calling makdirs() function with the swiss-prot ids file as input
	makdirs(file)
	# Closing the swiss-prot ids file
	file.close()
	print('====================================================')
	print('Your analysis is done. Thanks for using PyOmiX tool.')
	print('====================================================')
# ----------------------------------------------------------------------


if __name__ == '__main__':
	# Calling get_args() function
	args = get_args()
	# Calling main function
	main()
