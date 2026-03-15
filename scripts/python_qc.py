import sys # to intereact with terminal
import csv # to work with CSV files
from statistics import mean
import math 

input_fastq = sys.argv[1] # get input file path from terminal
output_csv = sys.argv[2]  # get output file path from terminal 

def mean_quality(qual):
    scores = []
    for c in qual:
        scores.append(ord(c) - 33) # convert ASCII standard to corresponding Phred quality score
    return sum(scores) / len(scores) # get the mean quality score 

def gc_content(seq):
    gc = seq.count("G") + seq.count("C") # calculate %GC bases
    return (gc / len(seq)) * 100

with open(input_fastq) as fastq, open(output_csv, "w", newline="") as out:
# open the input FASTQ in read mode and create an output CSV in write mode

    writer = csv.writer(out) # create a CSV writer object to use writing methods
    writer.writerow(["read_id", "gc_content", "read_length", "mean_quality"])

    while True:
        header = fastq.readline().strip() # read_id, if False (end of file), break the loop
        if not header:
            break
# readline() works like a pointer, moves to the next line every time

        seq = fastq.readline().strip()  # sequence
        fastq.readline() # skip the "+" line
        qual = fastq.readline().strip() # ASCII quality string

        read_id = header.split()[0] # get the only unique run_id from the header line

# calculate 3 metrics for each read
        gc = gc_content(seq) 
        length = len(seq)
        mean_q = mean_quality(qual)

# write the results to the output CSV file
        writer.writerow([read_id, gc, length, mean_q])