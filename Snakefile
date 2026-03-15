rule all:
    input:
        "results/nanoplot",
        "results/python/python_qc.csv",
        "results/python/python_results.pdf"

rule nanoplot_qc:
    input:
        fastq="data/barcode77.fastq"
    output:
        directory("results/nanoplot")
    threads: 4
    conda:
        "envs/main_env.yaml"
    shell:
        """
        NanoPlot --fastq {input.fastq} --outdir {output}
        """

rule python_qc:
    input:
        fastq="data/barcode77.fastq"
    output:
        csv="results/python/python_qc.csv"
    conda:
        "envs/main_env.yaml"
    shell:
        """
        python scripts/python_qc.py {input.fastq} {output.csv}
        """

rule visualize_qc:
    input:
        csv="results/python/python_qc.csv"
    output:
        python_results="results/python/python_results.pdf",
    conda:
        "envs/main_env.yaml"
    shell:
        """
        python scripts/visualization.py {input.csv} {output.python_results} 
        """


