import math
import numpy as np
class vectors():
	def __init__(self,x,y):
		self.x=x
		self.y=y

	def in_one_vector(self):
		self.Vec=[self.x,self.y]
	def module(self,x0,y0):
		self.x0=x0
		self.y0=y0
		self.X=(self.Vec[0]-self.x0)**2
		self.Y=(self.Vec[1]-self.y0)**2
		print(self.X,"X")
		print(self.Y,"Y")		
		Module=math.sqrt(self.Y+self.X)
		return Module		
	def direccion(self):
		angle=math.degrees(math.atan((self.y/self.x)))
		return angle
	def sum(self,x0,y0):
		self.x0=x0
		self.y0=y0
		X0=self.Vec[0]+self.x0
		Y0=self.Vec[1]+self.y0
		V=[X0,Y0]
		return V
	def mtrixsum(self,m1,m2):
		self.m1=m1
		self.m2=m2
		self.m1=np.asarray(self.m1)
		self.m2=np.asarray(self.m2)
		
		M=self.m1+self.m2
		return M
	def mtrixmult(self,m1,m2):
		self.m1=m1
		self.m2=m2
		self.m1=np.asarray(self.m1)
		self.m2=np.asarray(self.m2)
		
		M=self.m1*self.m2
		return M
	def matrixmult(self,m1,m2):
		self.m1=m1
		self.m2=m2
		self.m1=np.asarray(self.m1)
		self.m2=np.asarray(self.m2)
		
		for k in range(len(self.m2)):
			self.m3=np.zeros((len(self.m2),len(self.m2[k])))
		if len(self.m1[0]) == len(self.m2):
			for i in range(len(self.m1)):
				for j in range(len(self.m1[i])):
					for k in range(len(self.m2[i])):
						self.m3[i][j] = m1[k][j] * m2[i][k]  

		return self.m3
	def matrixsum(self,m1,m2):
		self.m1=m1
		self.m2=m2
		self.m3=[]
		for k in range(len(self.m2)):
			self.m3=np.zeros((len(self.m2),len(self.m2[k])))
		
		if len(self.m1) == len(self.m2):
			for i in range(len(self.m2)):
				for j in range(len(self.m2[i])):
					self.m3[i,j] = (m2[i][j]+m1[i][j])
	
		return self.m3

	def inner_product(self,angle2):
		self.angle2=angle2
		
		if self.angle2<=180 and self.angle2>=0:
			self.product_scalar=self.X*self.Y*math.cos(math.radians(self.angle2))
			print(math.cos(math.radians(self.angle2)))
			print(self.X,"X")
			print(self.Y,"Y")	
			return self.product_scalar
	def transposedvec(self,vectors):
		self.vectors=vectors
		
		if type(vectors):
			self.reverse=[i for i in reversed(self.vectors)]
		return self.reverse
	def transposedmat(self,vectors):
		self.vectors=vectors
		if type(vectors):
			self.reverse=[i for i in reversed(self.vectors)]
		return self.reverse
	def transposedMatrix(self,matriz):
		self.matriz=matriz
		for k in range(len(self.matriz)):
		
			self.reverse=np.zeros((len(self.matriz),len(self.matriz[k])))

		for i in range(len(self.matriz)):
			for k  in range(len(self.matriz[i])):

				self.reverse[i][k] = self.matriz[k][i]
		
		return self.reverse

"""
interesante parace que repodruce la matris identidad
		for i in range(len(self.matriz)):
			for k  in range(len(self.matriz[i])):
				self.vectors =[j for j in reversed(self.matriz[i])]

				self.reverse[i]= self.vectors[i]
		
		self.reverse = [j for j in reversed(self.reverse)]
"""

V=vectors(4,8)
V.in_one_vector()
#print(V.module(10,11))
#print(V.direccion())
#print(larry,larry)
#print(V.mult(1,1,3,4,5))
#print(V.inner_product(60))


larry2 = [[21,4,4],[14,53,24],[21,1,21]]
larry = [[21,1,4],[1,53,1],[21,1,21]]
print("multi larry\n",V.matrixmult(larry,larry))
print("")
print("3 larrys sumados\n",V.matrixsum(larry, [[21,4,4],[14,53,24],[21,1,21]]))#,[[1,1,4],[21,3,41]]))
print("")
print("\n  larry asarray \n",np.asarray(larry))
print("")
print("\n larry transpuesto\n",np.asarray(V.transposedMatrix(larry)),"\nlarry transpuesto con numpy\n",np.asarray(larry).T)
print("")
matriz = np.array([[1,2,3,4,5,6],[2,4,5,6,7,8],[1,2,3,5,7,9],[1,2,3,5,7,9],[1,2,3,5,7,9]])
print(np.asarray(matriz))
print(transposedMatrix(matriz))