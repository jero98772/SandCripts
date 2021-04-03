import cv2
from numpy import asarray 
def img2asciiart(imgPath,size = 15,intensity = 255,replaceItem = 0,items = ["@"," "]):
	dataFile = cv2.imread(imgPath,cv2.IMREAD_GRAYSCALE)
	imgresized  = cv2.resize(dataFile , (size, size)) 
	imgstr = ""
	for count in range(len(imgresized)):
		for cont in range(len(imgresized[count]))  :
				if imgresized[count,cont]//intensity == replaceItem:
					imgstr += items[0]
				else:
					imgstr += items[1]
		imgstr += "\n"
	return imgstr