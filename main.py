from DidHeShot import TheBallPasses
from SignalSending import GPIO_communication
import time

if __name__ == "__main__":
	j=0 # number of turn
	tot=0 # number of points
	res=[0,0,0] # handle case for strike and spare
	while j<5:
		
		print("You can play!")
		point=TheBallPasses()
		print(point)
		if point[1]==1 or point[1]==2:
			res[0]=point[0]
			res[1]=j
			res[2]=point[1]

		match res[2]:
			case 0:
				print(' ')
			case 1: 
				if j==res[1]+1:
					tot=tot+res[0]+point[0]
					res=[0,0,0]
			case 2:
				if j==res[1]+1 or j==res[1]+2:
					tot=tot+res[0]+point[0] 
					res=[0,0,0]
		tot+=point[0]
		j+=1
		print(f'Vous avez {tot} points')
		print("Next party")
		time.sleep(1)
		GPIO_communication()
		
