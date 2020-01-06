file1='C:\\Users\\ZSNR1KJ_II\\Documents\\Python Scripts\\belki.txt'
file2='C:\\Users\\ZSNR1KJ_II\\Documents\\Python Scripts\\tri3.txt'
file3='C:\\Users\\ZSNR1KJ_II\\Documents\\Python Scripts\\cos.txt'
file4='C:\\Users\\ZSNR1KJ_II\Documents\\Python Scripts\\beta.txt'
file5='C:\\Users\\ZSNR1KJ_II\Documents\\Python Scripts\\free_cos.txt'


#w pliku beta sa kąty do wprowadzenia w GSA. 
#Można to zrobić kopiując tabelę Elements do Excela i używajac funkcji =JEŻELI.BŁĄD(WYSZUKAJ.PIONOWO(A2;beta;2;FAŁSZ);0)

import math

B = {}
T = {}
Cos={}
with open(file1) as f:
    for line in f:
        (key, val1,val2)= line.split()
        #print key, val1, val2
        B[int(key)] = (int(val1),int(val2))

with open(file2) as f:
    for line in f:
        (key, val1,val2,val3)= line.split()
        #print key, val1, val2
        T[int(key)] = (int(val1),int(val2),int(val3)) 

with open(file3) as f:
    for line in f:
        (key, val1,val2,val3)= line.split()
        #print key, val1, val2
        Cos[int(key)] = (float(val1),float(val2),float(val3))        
#print B
#print T

#print Cos

import itertools

tri3_vertices={}

for edge in T:
    tri3_vertices[edge]=list(itertools.permutations(T[edge], 2))
    
tri3_edges={}

for tri3 in tri3_vertices: 
    beams=[]
    for each1 in tri3_vertices[tri3]:
        for each2 in B:
            if each1==B[each2]:
                beams.append(each2)
            tri3_edges[tri3]=beams
#print tri3_edges

neighbours={}

for each1 in tri3_edges:
    pairs=[]
    for each2 in tri3_edges:
        a=set(tri3_edges[each1])&set(tri3_edges[each2])
        b=set(tri3_edges[each1]).intersection(tri3_edges[each2])
        if len(a)==1&len(b)==1: 
            pairs=[each1,each2]
            neighbours[list(b)[0]]=pairs
#print neighbours

cos_zz={}

for each in Cos:
    #print cos[each][0]
    length=(Cos[each][0]**2+Cos[each][1]**2+Cos[each][2]**2)**0.5
    cos_zz[each]=(Cos[each][0]/length,Cos[each][1]/length,Cos[each][2]/length)
    
#print "cos_zz= ",cos_zz

beta={}
#suma={}

def vect_sum(a,b):
    return (a[0]+b[0],a[1]+b[1],a[2]+b[2])

def vect_direct_cos(a):
    length=(a[0]**2+a[1]**2+a[2]**2)**0.5
    return (a[0]/length,a[1]/length,a[2]/length)

for each1 in neighbours:
    #print neighbours[each1]
    #k,l=cos_zz.get(neighbours[each1][0]),cos_zz.get(neighbours[each1][1])
    suma=vect_sum(Cos.get(neighbours[each1][0]),Cos.get(neighbours[each1][1]))
    #suma[each1]=vect_sum(Cos.get(neighbours[each1][0]),Cos.get(neighbours[each1][1]))
    beta[each1]=180-float(math.acos(vect_direct_cos(suma)[2]))*180/math.pi

#print "beta =", beta
    #beta[each1]=[(k+l)/(k**2+l**2)**0.5]
        
f=open(file4,'w')
for (k,v) in beta.items():
    temp=str(k)+' '+str(v)+'\n'
    f.write(temp)
f.close()

free_edge={}

for each1 in tri3_edges:
    beams=[]
    for i in range(2):
        for each2 in neighbours:
            #print tri3_edges[each1][i],each2
            if tri3_edges[each1][i]!=each2:
                beams.append(tri3_edges[each1][i])
            free_edge[each1]=beams
#print free_edge
            
edges=[]
for each in tri3_edges:
    #edges.append(tri3_edges[each])
    edges=edges+tri3_edges[each]
    #set(edges)
edges=list(set(edges))
#print edges

com_edges=[]
for each in neighbours:
    com_edges.append(each)
#print com_edges

free_edges=list(set(edges) - set(com_edges))
#print free_edges

free={}
for each1 in tri3_edges:
    beams=[]
    for i in range(3):
        for each2 in free_edges:
            #print tri3_edges[each1][i]  
            if each2 == tri3_edges[each1][i]:
                               
                beams.append(each2)
            #print beams
    free[each1]=beams
#print free



#with open(file3) as f:
    #for line in f:
        #(key, val1,val2,val3)= line.split()
        ##print key, val1, val2
        #Cos[int(key)] = (float(val1),float(val2),float(val3))        
#print Cos

free_cos={}
for each1 in free:
    for each2 in Cos:
        if each1==each2:
            if len(free[each1])==2: 
                #print free[each1][0],free[each1][1],Cos[each2][2]
                free_cos[free[each1][0]]=Cos[each2][2]
                free_cos[free[each1][1]]=Cos[each2][2]
            if len(free[each1])==1:
                free_cos[free[each1][0]]=Cos[each2][2]
        
#print free_cos

f=open(file5,'w')
for (k,v) in free_cos.items():
    temp=str(k)+' '+str(v)+'\n'
    f.write(temp)
f.close()