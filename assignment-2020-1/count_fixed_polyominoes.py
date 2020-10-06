from pprint import pprint
import argparse
import sys
g={}


if len(sys.argv)==3:
	showg=sys.argv[1]
	n=int(sys.argv[2])
elif len(sys.argv)==2:
	n=int(sys.argv[1])	
	
for x in range(-n+2,n,1):
	for y in range(0,n,1):

		if(y>0 or(y==0 and x>=0)):
			z=abs(x)+y
			if(z<n):
				node=(x,y)

				g[node]=[]
				nright=abs(x+1)+y
				if(nright<n):
					rightneighbor=(x+1,y)
					g[node].append(rightneighbor)

				nupper=abs(x)+y+1
				if(nupper<n):
					upperneighbor=(x,y+1)
					g[node].append(upperneighbor)

				nleft=abs(x-1)+y
				if(nleft<n):
					if(y==0):
						if(x>0):
							leftneighbor=(x-1,y)
							g[node].append(leftneighbor)
					else:
						leftneighbor=(x-1,y)
						g[node].append(leftneighbor)


				nlower=abs(x)+y-1
				if(nlower<n):
					if(x<0):
						if(y>1):
							lowerneighbor=(x,y-1)
							g[node].append(lowerneighbor)
					else:
						if(y>0):
							lowerneighbor=(x,y-1)
							g[node].append(lowerneighbor)


def Neighbors_of_p(g,p,u):
	neighborsofp=[]
	for i in p:
		if i!=u:
			for j in g[i]:
				neighborsofp.append(j)

	return neighborsofp
c=0
def AddOne():
	global c
	c=c+1
	return c

def ValueofC():
	global c
	return c




#pprint(g[key])
untried=[(0,0)]
p=[]

def count_fixed_polyominos(g,untried,n,p,c):
	while len(untried):
		u=untried.pop()
		p.append(u)
		if len(p)==n:
			AddOne()
			#print(c)
		else:
			new_neighbors=set()
			for i in g[u]:
				if i not in untried and i not in p and i not in Neighbors_of_p(g,p,u):
					new_neighbors.add(i)
			new_untried=new_neighbors.union(untried)
			count_fixed_polyominos(g,new_untried,n,p,c)
		p.remove(u)
	return ValueofC()

if len(sys.argv)==3:
	if showg=='-p':
		pprint(g)
print(count_fixed_polyominos(g,untried,n,p,ValueofC()))
