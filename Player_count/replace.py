f=open("./2021-11-16",'r')
write_f=open("./2021-11-16-2",'w')

while(True):
    line=f.readline()
    if(line==''):
        break
    else:
        line_list=line.split()
        new_line=line_list[2].replace(",","")
        st=line_list[0]+" "+line_list[1]+" "+new_line+'\n'
        write_f.write(st)
        
        
        
f.close()
write_f.close()

