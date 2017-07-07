import sys
import random
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#Let's say there are n individuals in the population
#If theres one mutant allele, the probability of picking it
#in the first generation is  s/(2 * N - 1)

def usage():
    "Usage for this script"
    print("Usage:")
    print("\tpython3 wrightfisher.py <population size> <max # generations> <fitness value> <model>")

def plot_fixation(model, afreqs, AAs, aas, Aas):
    "Plotting happens here"
    if model == "dominant":
        output = "allelic_frequency_vs_generations_dominant.png"
    elif model == "recessive":
        output = "allelic_frequency_vs_generations_recessive.png"
    else:
        raise RuntimeError("Invalid model", model)
    Afreqs = [1 - x for x in afreqs]
    #print(Afreqs, afreqs, AAs, aas, Aas)
    plt.plot(Afreqs, range(len(Afreqs)), label = "A freq")
    plt.plot(afreqs, range(len(Afreqs)), label = "a freq")
    plt.plot(AAs, range(len(Afreqs)), "bs", label = "AA freq")
    plt.plot(aas, range(len(Afreqs)), "gs", label = "aa freq")
    plt.plot(Aas, range(len(Afreqs)), "rs", label = "Aa freq")
    plt.legend()
    #ax1 = plt.subplot()
    #ax1.set_xlim([-0.001, 1])
    #ax1.set_ylim([-0.001, 1])
    plt.savefig(output)

def run_wfmodel(N, ngen, mutant_fitness, model):
    "Run the wright-fisher model"
    gts_expanded = ["00", "01", "11"] #Expand what 0, 1 and 2 stand for
    nfixed = 0 #Number of iterations the one of the alleles fixed
    plot_fix = True #Only plot first fixation
    for i in range(100): #Run the simulation multiple times
        #print("Simulation iteration: ", i)
        gts = [0] * N #Population of homs
        fitnesses = [1] * N #Fitnesses of all hom-refs
        bio5488 = random.randrange(N) #Pick a random gamete
        gts[bio5488] = 1 #Mutation arises in one gamete, individual becomes het
        if model == "dominant":
            fitnesses[bio5488] = mutant_fitness #Mutation arises in one gamete, individual becomes het
        afreqs = [] #reference allele frequency
        aas = [] #hom-ref
        Aas = [] #het
        AAs = [] #het mutant
        afreqs.append(sum(gts)/(2*N))
        aas.append(gts.count(0)/N)
        Aas.append(gts.count(1)/N)
        AAs.append(gts.count(2)/N)
        for gen in range(ngen):
            #print("newgen", gen)
            #Normalize fitnesses to sum to 1.0
            fitness_probs = [fitness/sum(fitnesses) for fitness in fitnesses]
            gts_new = []
            fitnesses_new = []
            #Sample for next generation
            for n in range(N):
                #Pick the first allele
                #Pick the genotype of a random individual
                gt1 = gts[np.random.choice(N, p = fitness_probs)]
                #Pick an allele from that genotyp
                allele1 = random.randrange(2)
                #Get the allele, this is either 0 or 1
                allele1 = int(gts_expanded[gt1][allele1])

                #Pick the second alelel
                #Pick the genotype of a random individual
                gt2 = gts[np.random.choice(N, p = fitness_probs)]
                #Pick an allele from that genotyp
                allele2 = random.randrange(2)
                #Get the allele, this is either 0 or 1
                allele2 = int(gts_expanded[gt2][allele2])
                gt_new = allele1 + allele2 #The new gt for the next generation
                gts_new.append(gt_new) #Append to list of next generation genotypes
                if (model == "dominant" and gt_new == 1) or gt_new == 2:
                    fitnesses_new.append(mutant_fitness)
                else:
                    fitnesses_new.append(1)
            gts = gts_new
            fitnesses = fitnesses_new
            afreqs.append(sum(gts)/(2*N))
            aas.append(gts.count(0)/N)
            Aas.append(gts.count(1)/N)
            AAs.append(gts.count(2)/N)
            #print(gts, fitnesses)
            #Check if fixed to either allele
            if gts == [2] * N:
                nfixed += 1
                if plot_fix:
                    plot_fix = False
                    plot_fixation(model, afreqs, AAs, aas, Aas)
                break
            elif gts == [0] * N:
                break
    print("nfixed", nfixed)



def main():
    "Processing starts here"
    if len(sys.argv) < 5:
        return usage()
    #Number of indiv
    N = int(sys.argv[1])
    #Number of generations
    ngen = int(sys.argv[2])
    #Fitness of bio5488 allele
    fitness = float(sys.argv[3])
    #Inheritance model
    model = sys.argv[4]
    if model != "dominant" and model != "recessive":
        raise RuntimeError("Invalid model", model)
    run_wfmodel(N, ngen, fitness, model)

main()
