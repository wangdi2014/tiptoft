'''Given a string of nucleotides and k, return all kmers'''

class KmerHit():
	def __init__(self,count, coord):
		self.count = 0
		self.coordinates = [coord]

class Kmers:
	def __init__(self, sequence, k):
		self.sequence = sequence
		self.k = k

	def get_all_kmers_counter(self):
		end = len(self.sequence) - self.k
		kmer_sequences = [ self.sequence[i:i+self.k] for i in range(0,end)]
		return { x:0 for x in kmer_sequences}

	def get_all_kmers(self):
		return self.get_all_kmers_filtered()
		
	def get_all_kmers_filtered(self):
		kmers = {}
		
		end = len(self.sequence) - self.k
		kmer_sequences = [ self.sequence[i:i+self.k] for i in range(0,end)]

		for i,k in enumerate(kmer_sequences):
			if k in kmers:
				kmers[k].count += 1
				kmers[k].coordinates.append(i)
			else:
				kmers[k] = KmerHit(1,i)

		return kmers
		
	def get_one_x_coverage_of_kmers(self):
		end = len(self.sequence) - self.k
		kmers = [ self.sequence[i:i+self.k] for i in range(0,end, self.k)]
		return kmers
