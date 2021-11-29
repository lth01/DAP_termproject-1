f=open("./2021-11-16",'r')
write_ether_f=open("./2021-11-16-ether",'w')
write_axie_f=open("./2021-11-16-axie","w")


ether_list=[]
axie_list=[]
while(True):
    line=f.readline()
    if(line==''):
        break
    else:
        if line.find("이")>0:#*이더리움 문자열이 있는 경우
            line_list=line.split()
            ether_list.append(line_list[0]+" "+line_list[1]+" "+line_list[3])
            
        else:
            line_list=line.split()
            axie_list.append(line_list[0]+" "+line_list[1]+" "+line_list[3])
            
            

for element in ether_list:
    write_ether_f.write(element+'\n')

for element in axie_list:
    write_axie_f.write(element+'\n')

        
f.close()
write_ether_f.close()
write_axie_f.close()

