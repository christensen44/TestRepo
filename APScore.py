filename="apSCORES.txt"
##Conversion between letter grade and AP raw score
letter_dict={(70,100):"A+", (65,70):"A", (57,65):"A-", (53,57):"B+", (48,53):"B",(42,48):"B-",
(37,42):"C+",(32,37):"C",(28,32):"C-",(23,28):"D+",(20,23):"D",(0,20):"D-"}

APGrade_dict={(70,100):5, (57,70):4, (43,57):3, (33,43):2, (0,33):1}


def findScore(a,b,c,d,e,mc):
	lanswerScores=[a,b,c,d]
	minimum=min(lanswerScores)
	minIndex=lanswerScores.index(minimum)
	diff=float(4-minimum)/2
	modScores=[]
	i=0
	while i<len(lanswerScores):
		if i!=minIndex:
			modScores.append(lanswerScores[i])
		else:
			modScores.append(lanswerScores[i]+diff)
		i+=1
	
	score=0
	score+=modScores[0]*1.875
	score+=modScores[1]*1.875
	score+=modScores[2]*1.875
	score+=modScores[3]*1.875
	score+=e*3.125
	score+=mc*1.67
	score+=1
	newScore=round(score)
	for gradeRange in letter_dict.keys():
		#print gradeRange, range(gradeRange[0],gradeRange[1])
		if (newScore>=gradeRange[0]) and (newScore<gradeRange[1]):
			letterGrade=letter_dict[gradeRange]
	for gradeRange in APGrade_dict.keys():
		if (newScore>=gradeRange[0]) and (newScore<gradeRange[1]):
			APScore=APGrade_dict[gradeRange]
		
	
	
	return (score, letterGrade,APScore)
	
def loadfile(filename):
	scores={}
	for line in file(filename):
		tempdata=line.split(None)
		name=str(tempdata[0])
		a=float(tempdata[1])
		b=float(tempdata[2])
		c=float(tempdata[3])
		d=float(tempdata[4])
		e=float(tempdata[5])
		mc=float(tempdata[6])
		scores[name]=[a,b,c,d,e,mc]
	
	return scores
	
def runScores(filename):
	scores=loadfile(filename)
	printfile=open("scoresUnweighted.txt",'w')
	for key in scores.keys():
		score=findScore(scores[key][0],scores[key][1],scores[key][2],scores[key][3],scores[key][4],scores[key][5])
		print>>printfile, key, score[0],score[1], score[2]
	printfile.close()

runScores(filename)