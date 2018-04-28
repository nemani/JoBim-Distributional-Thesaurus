print("Loading")
import thesaurus
print("Welcome to the DT!")
print("Pruning factor is set to 4.5")
N = int(input("Enter number of words needed:"))
while True:
	x = input("Enter word:")
	output = thesaurus.GetNSimilarWords(x, N)
	if not output:
		print("Sorry! I do not know any similar words!")
	for a in output.keys():
		print("{}#{}\n".format(x,a))
		for i in range(len(output[a])):
			print("\t{} - {} - {} times \n".format(i+1, output[a][i][0], output[a][i][1]))