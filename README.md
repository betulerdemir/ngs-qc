NGS QC Analysis Pipeline

- How to run pipeline:
1. Set Linux OS (you can also use WSL)

2. Download Miniforge3 (Conda),
   wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh,
   bash Miniforge3-Linux-x86_64.sh

3. Install Snakemake,
   conda install -c conda-forge -c bioconda snakemake

4. Clone GitHub repository,
   git clone https://github.com/betulerdemir/ngs-qc.git,
   cd ngs-qc

5. Put FASTQ file in data/ directory

6. Run the pipeline,
   snakemake --use-conda --cores 1

Dear Professor Kılıç,

- What is done in this pipeline:
The Nanoplot program and a python script analyze the quality of long ngs data. Another python script visualize the results provided by previous python script. Snakemake and conda ensure that the pipeline works step-by-step in a consistent environment to get reproducible and reliable results.

- Data interpretation:
According to the results, a mean quality of 8.9 is not the best but acceptable especially for long-read sequencing. However, considering data is from to long-read sequencing, a mean read length of approximately 1kb is not expected (between 10-20kb is expected). In addition, median read length is even smaller: 500 bases. Also, an outlier with low quality, 700kb-length read can be clearly seen in the boxplot. Also, GC content distribution with a single peak may indicate no-contamination (reads are from one single organism).

- What would I suggest:
Before moving to further read mapping, I would like to ensure the data has a high quality to prevent potential problems later. I kindly request you to identify the source of the poor-quality data (originated from sample or sequencing machine?) and re-run the NGS again. 

Best regards,
Betül