from picamzero import Camera
from PIL import Image
import matplotlib.pyplot as plt

def IsUp(list_rgb,skittle):
	compteur=0
	for element in list_rgb:
		r,g,b=skittle.getpixel((element[0],element[1]))
		if ((180<=r<=255) and (0<=g<=50) and (0<=b<=50)):
			compteur+=1
	if compteur>=len(list_rgb)/2:
		return True
	else:
		return False

def analyse_skittle(path="skittles.jpg"):
	#Analyse de la photo
	skittles=Image.open(path)

	#donne les couleurs red green blue des pixel 100 250
	list_rgb1=[[360,282],[133,229],[446,342],[306,522],[140,535]]
	list_rgb2=[[1046,735],[1126,755],[1053,895],[1173,909],[1106,882]]
	list_rgb3=[[2220,709],[2086,682],[2006,722],[1993,495],[2193,469]]
	
	StateSkittle=[IsUp(list_rgb1,skittles),IsUp(list_rgb2,skittles),IsUp(list_rgb3,skittles)]
	print(StateSkittle)
	return StateSkittle
