from picamzero import Camera
from PIL import Image
import matplotlib.pyplot as plt

def take_picture(path="skittles.jpg"):
	#Prendre la photo
	cam=Camera()
	#cam.start_preview()

	cam.take_photo(path)
	#cam.stop_preview()

	#Analyse de la photo
	skittles=Image.open(path)
	#donne les couleurs red green blue des pixel 100 250
