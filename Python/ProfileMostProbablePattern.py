# Insert your Pr(Text, Profile) function here from Motifs.py.

# Input:  String Text, an integer k, and profile matrix Profile
# Output: ProfileMostProbablePattern(Text, k, Profile)
def ProfileMostProbablePattern(Text, k, Profile):
    # insert your code here. Make sure to use Pr(Text, Profile) as a subroutine!
	matchmax=0
	ProbablePattern=""
	for i in range(len(Text)-k+1):
		Pattern = Text[i:i+k]
		if Pr(Pattern, Profile) > matchmax:
			matchmax=Pr(Pattern, Profile)
			ProbablePattern=Pattern
	return ProbablePattern
		

def Pr(Text, Profile):
    # insert your code here
	pr=1
	for i in range(len(Text)):
		pr*=Profile[Text[i]][i]
	return pr


