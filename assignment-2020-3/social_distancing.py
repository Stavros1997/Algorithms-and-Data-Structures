from math import sqrt
d1={}
items=7
radius=1
rm=1
rn=1
mx=0
my=0
nx=2
ny=0 
def create_output(my_list):
	with open('your_file.txt', 'w') as f:
		for item in my_list:
			f.write(f'{item}\n')

front={(mx,my,radius):(nx,ny,radius),(nx,ny,radius):(mx,my,radius)}
circles=[(mx,my,radius),(nx,ny,radius)]
for i in range(items-2):
	#print(i)
	dx=nx-mx
	dy=ny-my
	d=sqrt(dx**2+dy**2)
	r1=rm+radius
	r2=rn+radius
	l=((r1**2)-(r2**2)+(d**2))/(2*d**2)
	e=sqrt((r1**2)/(d**2)-(l**2))
	kx=mx+l*dx-e*dy
	ky=my+l*dy+e*dx
	kx=round(kx,2)
	ky=round(ky,2)
	circles.append(tuple((kx,ky,radius)))
	front.update({(mx,my,radius):(kx,ky,radius),(kx,ky,radius):(nx,ny,radius)})
	for j in front:
		d1.update({j:round(sqrt(j[0]**2+j[1]**2),2)})
		
	
	print(d1)
	nx=kx
	ny=ky
	Cm=min(d1.items(), key=lambda x: x[1])
	#print(front)
	
	
	
#print(circles)
create_output(circles)

