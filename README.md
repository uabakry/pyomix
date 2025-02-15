# PyOmiX - Analysis Workflow
Analysis Workflow Course Project - Programming for Bioinformatics (Bioinformatics Professional Diploma at Nile University)

#### GROUP MEMBERS:
- Ahmed Omar Lamloum
- Mohamed Magdy AboelEla **(Team Leader)**
- Usama Bakry
- Waleed Faheem Amer

#### OVERVIEW:
The overall purpose of PyOmiX is to create an analysis workflow that generate a simple phylogeny trees from multiple sequence alignment files for a list of SWISS-Prot ids using Clustal Omega, throughout a series of steps as described in the following flowchart.

<p align="center">
  <img src="https://github.com/ubakry/pyomix/blob/master/workflow.png"  width="50%" height="50%">
</p>

#### INPUTS:
```
python3 pyomix.py -i <swiss-prot ids file dir> -d <database fasta file> -o <output dir>
``` 

#### OUTPUTS:
- Directory with a subdirectory for each ID from the input list.
- In each directory:
    * Sequence fasta file from UniProt.
    * Alignment file from Diamond.
    * Sequences fasta file for accessions numbers from NCBI.
    * Mulitple sequence alignment file and phylogenetic tree from Clustal Omega.

#### SUBTASKS:
01. Function to make directories for swiss-prot ids. **(done)**
    * Input: ids file.
    * Output: list of ids directories.
02. Function to get fasta file (sequence) using request from UniProt and NCBI. **(done)**
    * Input: swiss-prot id or NCBI accession number.
    * Output: sequence fasta file.
03. Function to align sequence using Diamond. **(done)**
    * Input: sequence fasta file and database file.
    * Output: alignment file.
04. Function to merge multiple fasta files in one fasta file. **(done)**
    * Input: list of fasta files.
    * Output: fasta file.
05. Function to perform multiple sequence alignment and create phylogenetic tree. **(done)**
    * Input: fasta file.
    * Output: multiple sequence alignment file and phylogenetic tree..
06. Implement python script to run it on the command line. **(done)**

#### EXTERNAL MODULES AND PROGRAMMES TO BE USED:
01. Diamond Aligner.
02. Clustal Omega (clustalo.py)

#### EXPECTED DIFFICULTIES:
01. Implementation the python script to run it on command line.

#### TASKS TO BE COMPLETED BY THE 4TH OF MAY:
01. Function to make directories for swiss-prot ids. **(done)**
02. Function to get fasta file (sequence) using request from UniProt and NCBI. **(done)**
03. Function to align sequence using Diamond. **(done)**
