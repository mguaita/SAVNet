#! /usr/bin/env python

from run import *
import argparse
from version import __version__

def create_parser():

    parser = argparse.ArgumentParser(prog = "savnet")

    parser.add_argument("--version", action = "version", version = "%(prog)s " + __version__)

    parser.add_argument("sample_list_file", metavar = "sample_list.txt", default = None, type = str,
                        help = "Tab-delimited file of the cohort with the followin columns (the order can be arbitrary): \
                                Sample_Name: Sample labels, \
                                Mutation_File: Path to mutation data (vcf or ANNOVAR format), \
                                SJ_File: Path to splicing junction data (generated by STAR), \
                                IR_File: Path to intron retention count file (generated by intron_retention_utils simple_count), \
                                Weight: The value used for negating the diversity of the numbers of total RNA-seq reads among samples (optional).")

    parser.add_argument("output_prefix", metavar = "output_prefix", default = None, type = str, 
                        help = "the prefix of the output")

    parser.add_argument("--grc", default = False, action = 'store_true',
                        help = "Deprecated. This is not used any more. Convert chromosome names to Genome Reference Consortium nomenclature (default: %(default)s)")

    parser.add_argument("--genome_id", choices = ["hg19", "hg38", "mm10"], default = "hg19",
                        help = "the genome id used for selecting UCSC-GRC chromosome name corresponding files (default: %(default)s)")

    parser.add_argument("--reference", metavar = "reference.fa", default = None, type = str,
                        help = "the path to the reference genome sequence")

    parser.add_argument("--sv", action='store_true',
                        help = "analysis structural variation file")

#     parser.add_argument("--branchpoint", action='store_true',
#                         help = "include branchpoint to the analysis")

    parser.add_argument("--donor_size", metavar = "donor_size", default = "3,6", type = str,
                        help = "splicing donor site size (exonic region size, intronic region size) (default: %(default)s)")

    parser.add_argument("--acceptor_size", metavar = "acceptor_size", default = "6,1", type = str,
                        help = "splicing donor site size (intronic region size, exonic region size) (default: %(default)s)")

    parser.add_argument("--SJ_pooled_control_file", default = None, type = str,
                        help = "the path to control data created by junc_utils merge_control (default: %(default)s)")

    parser.add_argument("--IR_pooled_control_file", default = None, type = str,
                        help = "the path to control data created by intron_retention_utils merge_control (default: %(default)s)")

    parser.add_argument("--chimera_pooled_control_file", default = None, type = str,
                        help = "the path to control data created by chimera_utils merge_control (default: %(default)s)")

    parser.add_argument("--SJ_num_thres", type = int, default = 2,
                        help = "extract splicing junctions whose supporting numbers are equal or more than this value \
                        at least one sample in the cohort (default: %(default)s)")

    parser.add_argument("--keep_annotated", default = False, action = 'store_true',
                        help = "do not remove annotated splicing junctions")

    parser.add_argument("--IR_num_thres", type = int, default = 3,
                        help = "extract intron retentions whose supporting numbers are equal or more than this value \
                        and the ratio is equal or more than IR_ratio_thres at least one sample in the cohort (default: %(default)s)")

    parser.add_argument("--IR_ratio_thres", type = int, default = 0.05,
                        help = "extract intron retentions whose ratios (Intron_Retention_Read_Count / Edge_Read_Count) \
                        is equal or more than this value and supporting numbers are equal or more than IR_num_thres \
                        at least one sample in the cohort (default: %(default)s)")

    parser.add_argument("--chimera_num_thres", type = int, default = 2,
                        help = "minimum required number of supporting junction read pairs (default: %(default)s)")

    parser.add_argument("--chimera_overhang_thres", type = int, default = 30,
                        help = "region size which have to be covered by aligned short reads (default: %(default)s)")

    parser.add_argument("--permutation_num", type = int, default = 100,
                        help = "the number of permutation for calculating false discovery rate")

    parser.add_argument("--alpha0", type = float, default = 1.0,
                        help = "the shape parameter of prior Gamma Distribution for inactive states")

    parser.add_argument("--beta0", type = float, default = 1.0,
                        help = "the rate parameter of prior Gamma Distribution for inactive states") 

    parser.add_argument("--alpha1", type = float, default = 1.0,
                        help = "the shape parameter of prior Gamma Distribution for active states") 

    parser.add_argument("--beta1", type = float, default = 0.01,
                        help = "the rate parameter of prior Gamma Distribution for active states") 

    parser.add_argument("--log_BF_thres", type = float, default = 3.0,
                        help = "the threshould of logaraithm of Bayes Factor (default: %(default)s)")

    parser.add_argument("--effect_size_thres", type = float, default = 3.0,
                        help = "the thresould of effect size estimator used for simple edge pruning (default: %(default)s")

    parser.add_argument("--debug", default = False, action = 'store_true', help = "keep intermediate files")
    
    
    return parser
 

