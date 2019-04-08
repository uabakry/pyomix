# PyOmiX - Analysis Workflow
Analysis Workflow Course Project - Programming for Bioinformatics (Bioinformatics Professional Diploma)

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
python pyomix.py -i <swiss-prot ids file dir> -d <database fasta file> -o <output dir>
``` 

#### OUTPUTS:
- Directory with a subdirectory for each ID from the input list.
- In each directory:
    * Sequence fasta file from UniProt.
    * Alignment file from Diamond.
    * Sequences fasta file for accessions numbers from NCBI.
    * Mulitple sequence alignment file from Clustal Omega.
    * Phylogenetic tree from Clustal Omega.

#### SUBTASKS:
1. Function to make directories for swiss-prot ids. **(done)**
   * Input: ids file.
   * Output: list of ids directories.
2. Function to get fasta file (sequence) using request from UniProt.
   * Input: swiss-prot id.
   * Output: sequence fasta file.
3. Function to align sequence using Diamond. **(done)**
   * Input: sequence fasta file and database file.
   * Output: alignment file.
4. Function to get fasta file (sequence) using request from NCBI.
   * Input: accession number.
   * Output: sequence fasta file.
5. Function to merge multiple fasta files in one fasta file.
    * Input: list of fasta files.
    * Output: fasta file.
6. Function to perform multiple sequence alignment and get a phylogenetic tree.
    * Input: fasta file.
    * Output: alignment file and phylogenetic tree file.
7. Implement python script to run it on the command line.

#### EXTERNAL MODULES AND PROGRAMMES TO BE USED:
1. Diamond Aligner.
2. Clustal Omega (clustalo.py)

#### EXPECTED DIFFICULTIES:
1. Unsuitability of the extracted phylogenetic tree from Clustal Omega, so, we will use Simple Phylogeny Tree module instead.
2. Implementation the python script to run it on command line.

#### TASKS TO BE COMPLETED BY THE 4TH OF MAY:
1. Function to make directories for swiss-prot ids. **(done)**
2. Function to get fasta file (sequence) using request from UniProt.
3. Function to align sequence using Diamond. **(done)**
4. Function to get fasta file (sequence) using request from NCBI.
