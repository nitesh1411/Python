import math

global1=[]
zipgroup=[[[] for i in range(100)] for k in range(100)]
doc=open('onlyPhoenixZip.txt','r')
for li in doc:
    li=li.strip()
    entry=li.split('\t')
    global1.append(entry)
doc.close()

doc_out=open('zipgroup.txt','w')
doc_out.write("Zipcode\tZipcode2\n")


for i in range(1,len(global1),1):
    for k in range(1,len(global1),1):
        dist1=math.pow((float(global1[i][1])-float(global1[k][1])),2)+math.pow((float(global1[i][2])-float(global1[k][2])),2)
        zipgroup[i-1][0].append(global1[i][0])
        zipgroup[i-1][1].append(global1[k][0])
        zipgroup[i-1][2].append(dist1)
     
    sorted_lists=sorted(zip(zipgroup[i-1][0],zipgroup[i-1][1],zipgroup[i-1][2]),key=lambda x: x[2])
    zipgroup[i-1][0],zipgroup[i-1][1],zipgroup[i-1][2]= [[x[i] for x in sorted_lists] for i in range(3)]
    
    doc_out.write(str(zipgroup[i-1][0][0])+"\t"+str(zipgroup[i-1][1][0])+"\t"+str(zipgroup[i-1][1][1])+"\t"+str(zipgroup[i-1][1][2])+"\t"+str(zipgroup[i-1][1][3])+"\t"+str(zipgroup[i-1][1][4])+"\t"+str(zipgroup[i-1][1][5])+"\t"+str(zipgroup[i-1][1][6])+"\n")

    
    
doc_out.close()
