import re 
from collections import Counter, defaultdict
from math import log

from graph import Graph, Vertex

# Path to the holled corpus
corpus = open('./mouse_corpus_holling','r') 

# JoBims with significance factor less than this would be pruned 
pruning_factor = 4.5

# ----------------------------------------------------
# This part reads the file and sanitises thcd ..e input

JoBims = []
for x in corpus.readlines():
	x = x.strip().lower()
	# x = re.sub(r'#.+\t',r"\t",x) # To Remove '#..\t'
	# x = re.sub(r'#.+\)',r')',x)  # To Remove '#..\)'
	JoBims.append(x)
# ----------------------------------------------------

# ----------------------------------------------------
# This part calculates the number of Distince Jos and Bims
Jos = []
Bims = []
for JoBim in JoBims:
	Jo, Bim = JoBim.split('\t')
	Jos.append(Jo)
	Bims.append(Bim)

TotalCount = len(JoBims)
JoBimCount = Counter(JoBims)
JoCount = Counter(Jos)
BimCount = Counter(Bims)

print("TotalCount: {}, JoBimCount:{}, JoCount:{}, BimCount:{}".format(TotalCount, len(JoBimCount), len(JoCount), len(BimCount)))
# ----------------------------------------------------

# ----------------------------------------------------
# Point-Wise Mutual Information based significance function
	# 	  ( 		Probablity(JoBim)	     )
	# log [----------------------------------] 
	# 	  ( Probablity(Jo) * Probablity(Bim) )

def significance(jb, j, b):
	pJB = JoBimCount[jb] /  TotalCount
	pJ = JoCount[j] / TotalCount  	# Total Count = Jo Count 
	pB = BimCount[b] / TotalCount 	# Total Count = Bim Count
	return log(pJB / (pJ * pB))
# ----------------------------------------------------

# ----------------------------------------------------
# This part adds edges to the graph if edge is significant 
g = Graph()

for JoBim in JoBimCount.keys():
	Jo, Bim = JoBim.split('\t')
	if significance(JoBim, Jo, Bim) > pruning_factor:
		g.addEdge(Jo, Bim)
		g.addEdge(Bim, Jo)
# ----------------------------------------------------



# ----------------------------------------------------
# This part perfomes the agregation for pairs of Jos in the graph
AggregatedJos = defaultdict(Counter)
for jo1 in JoCount:
	Jo1Vertex = g.getVertex(jo1)
	if Jo1Vertex:
		for BimVertex in Jo1Vertex.getConnections():
			for Jo2Vextex in BimVertex.getConnections():
				jo2 = Jo2Vextex.getId()
				if jo1 != jo2:
					AggregatedJos[jo1][jo2] += 1
# ----------------------------------------------------


# ----------------------------------------------------
# this part gets the N most simmilar words for a given word
# With all possible POS Tags
def GetNSimilarWords(word, N):
	posTags = ["ex","to","jjs","in","pos","cc","uh","fw","sym","rbr","jj","-rrb-","wp$","prp$","cd","wdt","rbs","pdt","prp","nn","rp","-lrb-","vb","dt","rb","wrb","md","wp","jjr"]
	retDict = {}
	for tag in posTags:
		retDict[tag] = AggregatedJos[word.lower()+"#"+tag].most_common(N)
		if not retDict[tag]:
			del retDict[tag]
	return retDict

# ----------------------------------------------------



if __name__ == '__main__':
	print(AggregatedJos)