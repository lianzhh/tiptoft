import re
class Gene:
	def __init__(self,name, kmers_with_coverage, kmers_without_coverage):
		self.name = name
		self.kmers_with_coverage = kmers_with_coverage
		self.kmers_without_coverage = kmers_without_coverage
		
	def __str__(self):
		return "\t".join((self.short_name(), self.completeness(), str(self.percentage_coverage()), self.accession(),'plasmidfinder', self.name))
		
	def completeness(self):
		if self.is_full_coverage():
			return "Full"
		else:
			return "Partial"
		
	def is_full_coverage(self):
		if self.kmers_without_coverage  == 0:
			return True
		else:
			return False
			
	def percentage_coverage(self):
		total_kmers = self.kmers_with_coverage + self.kmers_without_coverage
		if total_kmers > 0:
			return int((self.kmers_with_coverage*100)/total_kmers)
		else:
			return 0
			
	def short_name(self):
		regex = r"^([^_]+)_"
		
		m = re.search(regex, self.name)
		if m and m.group:
			return str(m.group(1))
		else:
			return ''
			
	def accession(self):
		regex = r"^([^_]+)_([^_]*)_(.+)$"
		
		m = re.search(regex, self.name)
		if m and m.group:
			return str(m.group(3))
		else:
			return ''