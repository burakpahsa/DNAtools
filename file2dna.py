import os
import sys


def file2dna(file_name):
	file_object = open(file_name)
	# read the dna
	dna = ''
	for line in file_object:
		dna = dna + line.strip("\n")
	file_object.close()
	return(dna)

dna = file2dna('dna')

n = 0
for i in range(len(dna)+1):
	print (dna[dna.find('>',i):dna.find('>',i)+12])
	


def reverse_join_reversed_iter(s):
    s1 = ''.join(reversed(s))
    return s1

dna = 'TCTTCACTGAGAAGCTAGCAGCGTGGATTGTGCAACTGGTGCACAGCCTCTACTCGTACAGGGAAACGAGCCAGGACTGGGTCAGCACTCTACGTAGGCATGGGCAGGTCCGGTAGGGCCTAGCAGATAAACAACCCCCGAGGACGTTTCCCGCGTTCGCGGTCCTAGACCGGTTTTCCCTCATATCAGTTCGTCTACCAACGGAACGATTGGATCTGAAAGTAGCGTCTGGCAAATCATAATGAGGGCTTTTTTCTACTAGTCGAGTAGTCTCCCACTAAGCGTGCGTCTCGCATCGCGAATGCTGCACGGCCCGAGAGCAGAAATGGCGCGTGAAAATACCCACCTGCCATGCGTTGCCGTCGAATTATCTCCGGAACTTAATGTCCCTAGGATGCAGAAGCGTCATCTAACGTCAAGCAGGTGCATAGATCGAGACTGGTTCCATTGCAGCTTTTCGACCGCAACGGCTCCCCATCCACCTAGAAGACTGACTTACGCCATAACCGCATTAGGTATTTGCGGGTGGCTACCAATTTTGCACCTTCCATGATGAACCTACGGTATAACCTTCCATAGGCTCAAGACGAATACTTTTCACCTGGTGAATGGCCCGGATGCGGCGTGCTAGTAAGTGATTGAAGTTTCAATCGAACTATAGGACCTCTATCTTTCACTGCACTGGGGGAGTACATACTAGCTCACTGGCCTGGGTGATTAATGAGCTCGCCCGCGAATGTCTCATGCTGTTTCCACCGTAGCACAAATAGTCCCTAGGCATAGATGTCGGTTTTATAACCCTGTAAAATCTTTCAATTCCATACCGGATAATCACTGATTAAAGAATGA'
for i in 'ACGT':
    k = dna.count(i);
    print (k);

#print (dna.replace('T','U'));
stre = reverse_join_reversed_iter(dna)
s = stre.replace('A','1')
s = s.replace('T','2')
s = s.replace('G','3')
s = s.replace('C','4')
s = s.replace('1','T')
s = s.replace('2','A')
s = s.replace('3','C')
s = s.replace('4','G')

print (s)

dna = 'CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'
# count bases
a_count = dna.count("A")
c_count = dna.count("C")
g_count = dna.count("G")
t_count = dna.count("T")
tot = a_count+t_count+c_count+g_count
# print reuslts
print("bases in genome: " + str(tot))
print("A: " + str(a_count))
print("C: " + str(c_count))
print("G: " + str(g_count))
print("T: " + str(t_count))

# calculate percentages
a_percent = a_count*100.0/tot
c_percent = c_count*100.0/tot
g_percent = g_count*100.0/tot
t_percent = t_count*100.0/tot
gc_percent = (g_count+c_count)*100.0/tot
# print percentages after rounding to one digit after the decimal point
print("A%: " + str(round(a_percent,1)))
print("C%: " + str(round(c_percent,1)))
print("G%: " + str(round(g_percent,1)))
print("T%: " + str(round(t_percent,1)))
print("gc%: " + str(round(gc_percent,6)))
#print("total:" + str(round(a_percent+c_percent+g_percent+t_percent,1)))