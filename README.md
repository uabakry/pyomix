# analysis-workflow
Analysis Workflow - Programming for Bioinformatics Course Project (Bioinformatics Professional Diploma)

#### LIST OF STUDENTS IN GROUP:
- Ahmed Omar Lamloum
- Moahmed Magdy AboelEla
- Usama Bakry
- Waleed Amer

#### OVERVIEW:
The purpose of the programme is to determine the most likely reading frame of a fragment of coding sequence and translate it to protein. It will be assumed that the most likely reading frame is the one that leads to the most similar amino acid sequence between human and macaque. Reading frames that contain a premature stop codon will not be considered.

#### INPUTS:
```
python pyomix.py -i <swiss-prot ids file dir> -d <database fasta file> -o <output dir>
``` 

#### OUTPUTS:
- Output #1
- Phylogenatic Trees

#### SUBTASKS:
1. Function to make directories for swiss-prot ids.
   * Input: ids file.
   * Output: list of ids directories.
2. Function to get fasta file (sequence) using request.
   * Input: swiss-prot id.
   * Output: sequence fasta file.
3. Function to align sequence using Blast.
   * Input: sequence fasta file.
   * Output: alignment file.
4. 

#### EXTERNAL MODULES AND PROGRAMMES TO BE USED:
1. NCBI Blast+ 
2. Clustal Omega (clustalo.py)
3. Simple Phylogeny Tree (simple_phylogeny.py)

#### EXPECTED DIFFICULTIES:
1. 
2. #2

#### TASKS TO BE COMPLETED BY THE 4TH OF MAY:
1. Function to make directories for swiss-prot ids.
2. Function to get fasta file (sequence) using request.
3. Function to align sequence using Blast.
