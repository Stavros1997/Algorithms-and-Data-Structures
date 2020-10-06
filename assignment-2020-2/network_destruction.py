import sys
import pprint
from collections import deque

use_method1=False
use_method2=False
if len(sys.argv)==4:
	if(sys.argv[1]=='-c'):
		use_method1=True
		num_nodes=int(sys.argv[2])
		input_filename=str(sys.argv[3])
elif len(sys.argv)==5:
	if(sys.argv[1]=='-r'):
		use_method2=True
		r=int(sys.argv[2])
		num_nodes=int(sys.argv[3])
		input_filename=str(sys.argv[4])

g = {}
influence={}
with open(input_filename) as graph_input:
    for line in graph_input:
        # Split line and convert line parts to integers.
        nodes = [int(x) for x in line.split()]
        if len(nodes) != 2:
            continue
        # If a node is not already in the graph
        # we must create a new empty list.
        if nodes[0] not in g:
            g[nodes[0]] = []
        if nodes[1] not in g:
            g[nodes[1]] = []
        # We need to append the "to" node
        # to the existing list for the "from" node.
        g[nodes[0]].append(nodes[1])
        # And also the other way round.
        g[nodes[1]].append(nodes[0])

if(use_method1==True):
	while(num_nodes!=0):
		degrees=[]
		for i in g:
			d=0
			for j in g[i]:
				d=d+1
				degrees.append(d)
		#if two nodes have the same degree
		y=max(g.keys())
		x=max(degrees)
		for i in g:
			if(len(g[i]))==x:
				if y>=i:
					y=i
					topop=i
        


		g.pop(topop)
    
		print(topop,x)
		
		for i in g:
			if(topop in g[i]):
				g[i].remove(topop)
		num_nodes=num_nodes-1


if(use_method2==True):
	def retr():
   		global r
   		return r


	def bfs(g, node):
		checkq=False
		r=retr()
		d=1
		sum1=0
		dictofnodes={}
		q = deque()
		q1=deque()
		visited={}
		inqueue={}
		for keys in g:
			visited.update({keys: False})
			inqueue.update({keys: False})

		q.appendleft(node)
		inqueue[node] = True
    
		while not (len(q) == 0):
			#print("Queue", q)
			c = q.pop()
			#print("Visiting", c)
			inqueue[c] = False
			visited[c] = True
			for v in g[c]:
				if not visited[v] and not inqueue[v]:
					q.appendleft(v)
					inqueue[v] = True

			if(d!=0):
				if(q):
					checkq=True
					q1=q.copy()
					x=q1.popleft()
					d=d-1
					r=r-1
					keysofdict=list(q)
            

			if(r!=0):
				if(q):
					checkq=True
					if(x not in q):
						q1=q.copy()
						x=q1.popleft()
						r=r-1
						keysofdict=list(q)
		#keysofdict=the ball
		if(checkq):
			for i in keysofdict:
				dictofnodes[i]=g[i]
			#dictofnodes=the grades of the ball
			for i in dictofnodes:
				sum1=sum1+len(dictofnodes[i])-1
		else:
			sum1=0   
		return(sum1)


	while(num_nodes!=0):
		for i in g:
			#print(i)
			sum2=bfs(g,i)
			y=(len(g[i]))
			influence.update({i:(y-1)*sum2})
		#if two nodes have the same influence
		maxin=max(influence.keys())
		max_influence=max(influence.values())
		for i in influence:
			if max_influence==(influence[i]):
				if maxin>=i:
					maxin=i
					node_topop=i
		#node_topop = max(influence, key=influence.get)
		print(node_topop,max_influence)

    

		g.pop(node_topop)
    
        
		for i in g:
			if(node_topop in g[i]):
				g[i].remove(node_topop)

		num_nodes=num_nodes-1
		influence.clear()
#pprint.pprint(g)

