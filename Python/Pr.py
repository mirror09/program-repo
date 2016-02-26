# Input:  String Text and profile matrix Profile
# Output: Pr(Text, Profile)
def Pr(Text, Profile):
    # insert your code here
	pr=1
	for i in range(len(Text)):
		pr*=Profile[Text[i]][i]
	return pr

