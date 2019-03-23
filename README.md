# PyOmiX - Analysis Workflow
Analysis Workflow Course Project - Programming for Bioinformatics (Bioinformatics Professional Diploma)

#### LIST OF STUDENTS IN GROUP:
- Ahmed Omar Lamloum
- Moahmed Magdy AboelEla
- Usama Bakry
- Waleed Amer

#### OVERVIEW:
The overall purpose of theis program is to generate a simple phylogeny tree for multiple sequence alignments obtained from Clustal Omega, throughout a series of steps started by getting the fasta file for a list of swiss-prot ids then performing alignment through NCBI-Blastp then obtaining sequences for ids 

![alt text](https://github.com/ubakry/pyomix/blob/master/workflow.png "PyOmiX Workflow")

#### INPUTS:
```
python pyomix.py -i <swiss-prot ids file dir> -d <database fasta file> -o <output dir>
``` 

#### OUTPUTS:
- Output #1
- Phylogenatic Trees

#### SUBTASKS:
1. Function to make directories for swiss-prot ids. (done)
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
1. Function to make directories for swiss-prot ids. (done)
2. Function to get fasta file (sequence) using request.
3. Function to align sequence using Blast.
