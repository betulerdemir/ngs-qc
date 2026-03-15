import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

input_csv = sys.argv[1] # get input file path from terminal
python_results = sys.argv[2]  # get output file path from terminal 

df = pd.read_csv(input_csv)

with PdfPages(python_results) as pdf:

    sum_stat = df[["read_length", "gc_content", "mean_quality"]].describe().round(2)
    fig, ax = plt.subplots()
    ax.axis("off")

    ax.table(
        cellText=sum_stat.values,
        colLabels=sum_stat.columns,
        rowLabels=sum_stat.index,
        loc="center"
        )

    pdf.savefig(fig)
    plt.clf()

# Read length distribution
    plt.boxplot(df["read_length"])
    plt.title("Read Length Distribution")
    plt.xlabel("Reads")
    plt.ylabel("Read Length (bp)")
    pdf.savefig()
    plt.clf()

# GC distribution
    plt.hist(df["gc_content"], bins = 50)
    plt.title("GC Content Distribution")
    plt.xlabel("GC %")
    plt.ylabel("Count")
    pdf.savefig()
    plt.clf()

# Quality distribution
    plt.hist(df["mean_quality"], bins= 50)
    plt.title("Mean Read Quality Distribution")
    plt.xlabel("Mean Quality")
    plt.ylabel("Count")
    pdf.savefig()
    plt.clf()

