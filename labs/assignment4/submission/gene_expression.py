#!/usr/bin/env python3
"""
This script reads in raw expression counts and performs
a couple of normalizations on them and visualizes the
result.
Usage: python3 gene_expression.py raw_counts.txt
"""

import sys
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

#Print out the doc string and exit if the number of input parameters is not correct
if (len(sys.argv) != 2):
    sys.exit(__doc__)

#######################
##Part 0 -- Functions##
#######################

# CPM counts per million
# Convert raw counts to counts per million (cpm)
# Raw count x[i,j] (from sample i, gene j)
# Total counts N[i] (from sample i)
# cpm[i,j] = (10^6)*x[i,j]/N[i]
def counts_per_million(dictionary, list_of_samples):
    # Initialize output dictionary cpm_dict
    cpm_dict = {}
    # Find N, the list of each sample's library size
    N = library_sizes(dictionary, list_of_samples)
    # Calculate cpm one gene at a time using list comprehension
    for k,v in dictionary.items():
        # Note: do NOT use 10^6, which equals 12
        # Use either 10**6 or 1000000 for 1 million
        # k is the key (gene name)
        # v is the value (raw counts of gene k)
        cpm_dict[k] = [(10**6)*x/n for x,n in zip(v,N)]
    return(cpm_dict)
# End of CPM function #

# Library size
# Calculate library size of each sample (e.g. sum of RNA-seq counts)
def library_sizes(dictionary, list_of_samples):
    # Get the total number of samples
    num_samples = len(list_of_samples)
    # Initialize N, a list to hold the total counts from each sample
    N = []
    # For loop to iterate over each sample 
    for i in range(num_samples):
        # Append a new float zero value for each sample (goes to index i)
        N.append(0.0)
        # For loop to iterate over each value in our dictionary
        for v in dictionary.values():
            # Get the count from the i index of this gene and add it to the total for sample i
            N[i] += v[i]
    # Return the list containing each sample's library size
    return(N)
# End of lbirary sizes function #

# Translate dictionary
# Function to translate a dictionary from {gene:[list of counts by sample]} to {sample:[list of counts by gene]}
# The new dictionary will have one key for each sample and the value of each key will be a list of counts associated with that sample
# This function is used in another function called upper_quartile_norm()
# Each comment below should correspond to one line of code
def translate_dictionary(dictionary, list_of_samples):
    # Initialize a new dictionary called translated_dictionary with empty curly brackets
    translated_dictionary = {}
    # Sort the keys of the input dictionary and save it in a list called 'genes'
    genes = list(dictionary.keys())
    genes = sorted(genes)

    # Use a for loop to iterate over each sample (using a numbered index, not sample names)
    for index, sample in enumerate(list_of_samples):
        # Get the current sample name from list_of_samples
        # Initialize a new key in translated_dictionary using the current sample name. Let the value be an empty list.
        translated_dictionary[sample] = []
        # Use a for loop to iterate over each gene in your list of genes
        for gene in genes:
            # Find the RNA-seq count associated with this gene for this sample
            count = dictionary[gene][index]
            # Append the count to the list of counts for this sample in translated_dictionary
            translated_dictionary[sample].append(count)

    # Return translated_dictionary
    return(translated_dictionary)
# End of translate dictionary function #

# Upper quartile normalization
# Compute the upper quartile normalization of raw counts
# Raw count x[i,j] (from sample i, gene j)
# D[i] value corresponding to 75th percentile of raw counts (from sample i)
# Mean of D, or the mean of all upper quartile means
# Upper quartile normalized count for sample i and gene j is (Mean of D)*x[i,j]/D[i]
def upper_quartile_norm(dictionary, list_of_samples):
    #Create dictionary to store upper quartile normalization
    upper_quartile_norm_dictionary = {}
    #Get the number of samples
    num_samples = len(list_of_samples)
    #Translate the dictionary from {gene:[list of counts by sample]} to {sample:[list of counts by gene]}
    translated_dict_for_D = translate_dictionary(dictionary, list_of_samples)
    #Empty list of upper quantile values for each sample
    D = []
    #iterate through each sample index
    for i in range(num_samples):
        #Get the sample name for sample_i
        sample_name = list_of_samples[i]
        #Get the upper quartile for this sample using counts of all genes for this sample
        D.append(np.percentile(translated_dict_for_D[sample_name],75))
    #Compute the mean of upper quartiles across all samples
    meanD = np.mean(D)
    #Iterate through all genes and counts of that gene in all samples
    for k,v in dictionary.items():
        #Compute normalized upper quartile for each gene in each sample
        #key is gene, value is normalized count in each sample
        upper_quartile_norm_dictionary[k] = [meanD*x/d for x,d in zip(v,D)]
    #Return the normalized upper quartile dictionary
    return(upper_quartile_norm_dictionary)
# End of upper quartile normalization function #

#Function to calculate Fisher's Linear Discriminant (add comments, too!) for all genes in your count dictionary. Call your function fishers_linear_discriminant. Remember that functions should be able to work using different data sets, so make sure that your function would work with data from a different experiment with different numbers of before and after samples. 
# Return the top ten genes according to the highest FLD values
# Input to this function should be a count dictionary and two lists letting the function know which index values go with each group
# You will need to iterate over each gene in the dictionary and calculate the FLD of each gene
# FLD of a gene = ((m1-m2)^2)/((s1)^2 + (s2)^2)
# m1 = mean of the first group
# m2 = mean of the second group
# s1 = standard deviation of the first group
# s2 = standard deviation of the second group

#Function to calculate Fisher's linear discriminant
def fisher_linear_discriminant(count_dictionary, group1_index, group2_index):
    #Dictionary to store FLD values
    fld_dictionary = {}
    #Create a list to store top ten FLD genes
    top_ten_fld_genes = []
    #Iterate through each gene and raw count
    for gene, values  in count_dictionary.items():
        group1_values = [values[i] for i in group1_index]
        group2_values = [values[i] for i in group2_index]
        m1 = np.mean(group1_values)
        m2 = np.mean(group2_values)
        s1 = np.std(group1_values)
        s2 = np.std(group2_values)
        fld1 = (m1 - m2) ** 2 / ((s1 ** 2) + (s2 ** 2))
        fld_dictionary[gene] = fld1
    #Identify top ten FLDs
    top_ten_flds = fld_dictionary.values()
    top_ten_flds = sorted(top_ten_flds, reverse = True)
    top_ten_flds = top_ten_flds[0:10]
    #Print the top ten fld values
    print("Top 10 FLD: ", top_ten_flds)
    for fld in top_ten_flds:
        for gene, fld1 in fld_dictionary.items():
            if fld == fld1:
                top_ten_fld_genes.append(gene)
    #Return the top ten fld genes
    return top_ten_fld_genes

####################
##End of functions##
####################

# These first lines of code will get the data imported and in the right format for the rest of the homework
# You need to do the rest of the work starting from Part 1 -- Data filtering

#open the data file
data_file = open(sys.argv[1],"r")
#first line of data file contains sample names -- store in a list
sample_list = data_file.readline().strip().split()[1:]
#initialize raw count dictionary
raw_counts_dict = {}
#add each gene and expression values to dictionary
for line in data_file:
    line_list = line.strip().split() #split line into list at whitespace, strip removes leading and trailing whitespace
    gene = line_list[0] #name of gene is the first thing in the list
    expression_values = [int(float(v)) for v in line_list[1:]] #values of gene expression follow the gene name
    raw_counts_dict[gene] = expression_values #add keys and values to the dictionary {gene:expression}
#close the data file
data_file.close()

############################
##Part 1 -- Data filtering##
############################

print("Initial number of genes, ", len(raw_counts_dict))

# Filter out genes with zero expression in all samples
remove_genes = [] #List of genes to be removed
for gene, counts in raw_counts_dict.items():
    sum1 = 0
    for count in counts:
        #Sum count across all samples for a gene
        sum1 += count
    #Add zero count genes to a list
    if sum1 == 0:
        remove_genes.append(gene)

#Remove the genes where count is zero
for gene in remove_genes:
    del raw_counts_dict[gene]

#Number of genes after raw counts filter
print("After raw counts filter, ", len(raw_counts_dict))

#Filter out genes with 6 or more samples with cpm < 1
cpm_dict = counts_per_million(raw_counts_dict, sample_list)
cpm_remove = [] #Genes with 6 or more samples cpm < 1
for gene, cpms in cpm_dict.items():
    less_than_one = 0
    for cpm in cpms:
        if float(cpm) < 1:
            less_than_one += 1
    #Add CPM less than 6 genes to a list
    if less_than_one >= 6:
        cpm_remove.append(gene)

#Filter out genes with 6 or more samples with cpm < 1
for gene in cpm_remove:
    del raw_counts_dict[gene]

print("After CPM filter, ", len(raw_counts_dict))

################################
##Part 2 -- Data visualization##
################################

# Plot library sizes (save file as library_size.png)
sample_counts = {}
for gene, counts in raw_counts_dict.items():
    for index, count in enumerate(counts):
        if index not in sample_counts:
            sample_counts[index] = 0
        #Accumulate counts per subject
        sample_counts[index] += count

print("Raw counts")
counts_in_millions = [] #Store the counts in millions
for index, count in sample_counts.items():
    #Get the counts in millions
    counts_in_millions.append(count/10**6)
    print(index, sample_counts[index])

#Number of samples
index = np.arange(len(sample_counts))

#Plot the results
fig, ax = plt.subplots()
ax.set_xlabel('Sample')
ax.set_title('Library sizes')
ax.set_ylabel('Raw library-size in millions')
plt.bar(index, counts_in_millions)
plt.savefig('library_size.png')
################################
##Part 3 -- Data normalization##
################################

# Normalize count data left after filtering steps
normalized_counts = upper_quartile_norm(raw_counts_dict, sample_list)

#Get the normalized counts by sample
normalized_sample_counts = {}
for gene, counts in normalized_counts.items():
    for index, count in enumerate(counts):
        if index not in normalized_sample_counts:
            normalized_sample_counts[index] = 0
        #Accumulate normalized sample count by subject
        normalized_sample_counts[index] += count

print("Normalized counts")
#Get the normalized count in millions
normalized_counts_in_millions = [] #Store the counts in millions
for index, count in normalized_sample_counts.items():
    #Get the normalized sample count in millions
    normalized_counts_in_millions.append(count/10**6)
    print(index, normalized_sample_counts[index])

# Plot normalized library sizes (save file as library_size_normalzied.png)
index = np.arange(len(normalized_sample_counts))
fig, ax = plt.subplots()
ax.set_xlabel('Sample')
ax.set_title('Library sizes')
ax.set_ylabel('Normalized library-size in millions')
plt.bar(index, normalized_counts_in_millions)
plt.savefig('library_size_normalized.png')

##############################
##Part 4 -- Data exploration##
##############################

# Calculate Fisher's Linear Discriminant for each gene basd on the normalized count data
#Indexes for the before group
before_indices = [0, 1, 2, 3, 4, 5]
#Indexes for the after group
after_indices = [6, 7, 8, 9, 10, 11]
#Get the top ten FLD genes
top_ten_fld_genes = fisher_linear_discriminant(normalized_counts,
                                         before_indices,
                                         after_indices)
print("Top 10 FLD genes: ", top_ten_fld_genes)

# Pick a gene to explore further and plot the mean expression level for the before and after groups (save file as mean_expression.png)
gene1_counts = normalized_counts['ENSG00000181163']
gene1_counts_before = gene1_counts[0:6]
gene1_counts_after = gene1_counts[8:12]
fig, ax = plt.subplots()
ax.set_title('NPM1 normalized counts - Before(1)/After(2)')
ax.set_ylabel('Normalized library-size in millions')
plt.xticks([1, 2], ['Before', 'After'])
plt.boxplot([gene1_counts_before, gene1_counts_after])
plt.savefig('mean_expression.png')

######################################
##Extra credit -- Going the distance##
######################################

#Write the normalized results to a file, compute euclidean distances using R
of = open("normalized_matrix.tsv", "w")
for gene, counts in normalized_counts.items():
    of.write(gene + "\t" + "\t".join([str(x) for x in counts]) + "\n")
