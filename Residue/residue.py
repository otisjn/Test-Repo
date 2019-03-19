from sage.all import *




########## FUNCTION TO CHECK THE LENGTH OF TAYLOR POLYNOMIAL ############

########### POLY IS A RATIONAL FUNCTION ###########

######### h is height you are checking #########

########## POLE IS WHRE THERE IS A POLE ##########

######### VAR IS A LIST OF VARIABLES #######

def CheckLength(poly,pole,h, var):
	
	####### TAKES THE GIVEN POLYNOMIAL AND GIVEN POLE
					###### AND BUILDS THE SAGE COMMAND TO CALCULATE
								#### THE TAYLOR SERIES
			
	X='var('
	count2=0
	for s in var:
		if count2!=len(var)-1:
			X=X+'"'+s+'"'+','
		if count2==len(var)-1:
			X=X+'"'+s+'"'
		count2=count2+1
	X=X+')'
	
	L='{'
	count=0
	for s in var:
		T='"'+s+'"'+':'+'var('+'"'+s+'"'+')'
		if count!=len(var)-1:
			L=L+T+','
		if count==len(var)-1:
			L=L+T+'}'
		count=count+1
			#print(L)
	#print(sage_eval(L))
	

	
	cmd='maxima.taylor('+poly+','+X+','+str(pole)+',-'+str(h)+')'
	#print(preparse(L))
	


	C=sage_eval(cmd,locals=sage_eval(L))
	

	
	####### NOW SPLITS IT UP TO FIND OUT IF THE COEFFICENT IS ZERO
			##### BELOW NEGATIVE 1
	B=str(C).split('+')

	A=B[0].split(' ') 

	D='poop'

	for i in range(0,len(A)):
		if A[i]!='':
			D=A[i]
			
	print('D=')
	print(D)
	if D=='0':
		##### THIS IS THE HEIGHT OF THE COEFFICIENT IF NOTHING BELOW 
				#### NEGATIVE ONE
		return 2
	else:
		##### THIS IS THE HEIGHT OF THE COEFFICENT IF THERE IS SOMETHING
				#### SOMETHING BELOW THE NEGATIVE ONE
		return 3
	

	

########## FUNCTION TO GRAB THE RESIDUE #####

########### POLY IS A RATIONAL FUNCTION ###########

########## POLE IS WHRE THERE IS A POLE ##########
def Residue(poly,pole,var):
	n=CheckLength(poly,pole,2,var)
	
	X='var('
	count2=0
	for s in var:
		if count2!=len(var)-1:
			X=X+'"'+s+'"'+','
		if count2==len(var)-1:
			X=X+'"'+s+'"'
		count2=count2+1
	X=X+')'
	
	
	L='{'
	count=0
	for s in var:
		T='"'+s+'"'+':'+'var('+'"'+s+'"'+')'
		if count!=len(var)-1:
			L=L+T+','
		if count==len(var)-1:
			L=L+T+'}'
		count=count+1
	

			#print(L)
	#print(sage_eval(L))
	
	print('n=')
	print(n)
	
	if CheckLength(poly,pole,1,var) == 2:
		return 0

	else:
		cmd='maxima.taylor('+poly+','+X+','+str(pole)+',-1)'

		C=sage_eval(cmd,locals=sage_eval(L))
		
		#print(C)

		P=str(C).split('\r\n')
		
		print(P)
		
		Z=P[len(P)-2].split(' ')
		
		#print(Z[len(Z)-1])
		
		### CONDITION THAT RESIDUE IS ZERO ###
		
		if n==3 and Z[len(Z)-1]!=str(pole):
			return 0
		
		else:
			#print(P)

			Q=P[len(P)-1-int(n)].split(' ')

			return (Q[len(Q)-1])
	
	


	

	
def FindPoles(poly,var):
	Q='FractionField(CC['
	#print(
		
		
		

	
	

poly='(x^3-5*x+7)/(x-1)^2'

poly1='1/(x-1)'

poly2='1/(x-1)^2'

poly3='1/(x-1)^3'

poly4='1/((x-1)^3*(y-1))'

poly5='(1/(x-1)^3)*(y-1)*(x^2-3*y+7)'

poly6='(1/(x-1)^2)*(y^2-3*y-7)'

poly7='(1/(x-1))*(y-1)'




print(Residue(poly4,'(1,0)',['x','y']))


#print('\n')

#print('\n')


cmd='maxima.taylor('+poly4+',var("x","y"),(1,0),-1)'

C=sage_eval(cmd,locals={'x':var('x'), 'y':var('y')})

print(C)








