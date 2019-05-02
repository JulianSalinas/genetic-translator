#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tablas basadas en http://www.cbs.dtu.dk/courses/27619/codon.html

complement_table = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

amin_to_codon_tab = {
    'I': ['ATT', 'ATC', 'ATA'],
    'L': ['CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG'],
    'V': ['GTT', 'GTC', 'GTA', 'GTG'],
    'F': ['TTT', 'TTC'],
    'M': ['ATG'],
    'C': ['TGT', 'TGC'],
    'A': ['GCT', 'GCC', 'GCA', 'GCG'],
    'G': ['GGT', 'GGC', 'GGA', 'GGG'],
    'P': ['CCT', 'CCC', 'CCA', 'CCG'],
    'T': ['ACT', 'ACC', 'ACA', 'ACG'],
    'S': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'Y': ['TAT', 'TAC'],
    'W': ['TGG'],
    'Q': ['CAA', 'CAG'],
    'N': ['AAT', 'AAC'],
    'H': ['CAT', 'CAC'],
    'E': ['GAA', 'GAG'],
    'D': ['GAT', 'GAC'],
    'K': ['AAA', 'AAG'],
    'R': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    '_': ['TAA', 'TAG', 'TGA']
}

codon_to_amin_tab = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M', 'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K', 'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L', 'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E', 'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S', 'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TGG': 'W', 'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TAA': '_', 'TAG': '_'}

amin_format_tab = {
    'I': ('ILE', 'ISOLEUCINE'), 'L': ('LEU', 'LEUCINE'), 'V': ('VAL', 'VALINE'), 'F': ('PHE', 'PHENYLALANINE'),
    'M': ('MET', 'METHIONINE'), 'C': ('CYS', 'CYSTEINE'), 'A': ('ALA', 'ALANINE'), 'G': ('GLY', 'GLYCINE'),
    'P': ('PRO', 'PROLOLINE'), 'T': ('THR', 'THREONINE'), 'S': ('SER', 'SERINE'), 'Y': ('TYR', 'TYROSINE'),
    'W': ('TRY', 'TRYPTOPHAN'), 'Q': ('GLN', 'GLUTAMINE'), 'N': ('ASN', 'ASPARAGINE'), 'H': ('HIS', 'HISTIDINE'),
    'E': ('GLU', 'GLUTAMIC_ACID'), 'D': ('ASP', 'ASPARTIC_ACID'), 'K': ('LYS', 'LYSINE'), 'R': ('ARG', 'ARGININE'),
    '_': ('STP', 'STOP')
}