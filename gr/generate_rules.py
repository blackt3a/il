import json







base= ""
with open("./rules.json","r") as target:
    base = json.load(target)



_total      = 100000000000000000000000000000000000000
                #3    
_name       =  000 #5
_phone      =     00000 #3
_place      =          000 #3
_addr       =             000 #3
_door       =                000  #6
_birth      =                   000000 #2
_mail       =                         00 #3
_slang      =                           000 #4
_random     =                              0000 #1
_extra_dic  =                                  0  #4
_total_len  =                                   0000 #1
_other      =                                       0


#_name       =  000
_name_list = []
for i in range(0,1+1):  #aka
    for j in range(0,1+1): #part
        for k in range(0,1+1): #full
            tmp = f"{i*100+j*10+k:0{3}}"
            _name_list.append(tmp)
print("_name_list=>")
print(_name_list)

#_phone      =     00000
_phone_list = []
for i in range(0,1+1): #total
    #print("total=>"+str(i))
    for j in range(1,9+1): #min 1~29 ; min>=1
        #print("<=min"+str(j))
        for k in range(j,10+1): #max >=1 ; max >=min
            if k >= j:
                #print("max=>"+str(k))
                tmp = f"{i*10000+j*100+k:0{5}}"
               #print("============")
               #print(i*10000)
               #print(j*100)
               #print(k)
               #print(tmp)
                _phone_list.append(tmp)
print("_phone_list")
print(_phone_list)

#_place_list  = 000
_place_list = []
for i in range(0,1+1):  #aka
    for j in range(0,1+1): #part
        for k in range(0,1+1): #full
            tmp = f"{i*100+j*10+k:0{3}}"
            _place_list.append(tmp)
print("_place_list")
print(_place_list)

#_addr       =             000
_addr_list = []
for i in range(0,1+1):  #aka
    for j in range(0,1+1): #part
        for k in range(0,1+1): #full
            tmp = f"{i*100+j*10+k:0{3}}"
            _addr_list.append(tmp)
print("_addr_list")
print(_addr_list)

#_door       =                000
_door_list = []
for i in range(0,1+1):  #aka
    for j in range(0,1+1): #part
        for k in range(0,1+1): #full
            tmp = f"{i*100+j*10+k:0{3}}"
            _door_list.append(tmp)
print("_door_list")
print(_door_list)


#_birth      =                   000000
_birth_list = []
for i in range(0,1+1):  #Y
    for j in range(0,1+1): #M
        for k in range(0,1+1): #D
            for m in range(0,1+1):#Y_M
                for n in range(0,1+1):#M_D
                    for q in range(0,1+1):#Y_M_D
                        tmp = f"{i*100000+j*10000+k*1000+m*100+n*10+q:0{6}}"
                        #print(tmp)
                        _birth_list.append(tmp)
print("_birth_list")
print(_birth_list)





#_mail       =                         00
_mail_list = []
for i in range(0,1+1):  #aka
    for j in range(0,1+1): #part
            tmp = f"{i*10+j*1:0{2}}"
            #print(tmp)
            _mail_list.append(tmp)
print("_mail_list")
print(_mail_list)


#_slang      =                           000
_slang_list = []
for i in range(0,1+1):  #aka
    for j in range(0,1+1): #part
        for k in range(0,1+1): #full
            tmp = f"{i*100+j*10+k:0{3}}"
            #print(tmp)
            _slang_list.append(tmp)
print("_slang_list")
print(_slang_list)



#_random     =                              0000
_random_list = []
for j in range(1,9+1): #min 1~29 ; min>=1
    #print("<=min"+str(j))
    for k in range(j,10+1): #max >=1 ; max >=min
        if k >= j:
            #print("max=>"+str(k))
            tmp = f"{j*100+k:0{4}}"
           #print("============")
           #print(i*10000)
           #print(j*100)
           #print(k)
            #print(tmp)
            _random_list.append(tmp)
print("_random_list")
print(_random_list)



_other_list = ["1","0"]
_extra_dic_list = ["1","0"]
print("_other_list")
print(_other_list)

print("_extra_dic_list")
print(_extra_dic_list)

#_total_len = 0000
_total_len_list = []
for j in range(1,9+1): #min 1~29 ; min>=1
    #print("<=min"+str(j))
    for k in range(j,10+1): #max >=1 ; max >=min
        if k >= j:
            #print("max=>"+str(k))
            tmp = f"{j*100+k:0{4}}"
           #print("============")
           #print(i*10000)
           #print(j*100)
           #print(k)
            #print(tmp)
            _total_len_list.append(tmp)

print("_total_len_list")
print(_total_len_list)

#print(_name_list)


#total      = 100000000000000000000000000000000000000
#               #3    
#name       =  000 #5
#phone      =     00000 #3
#place      =          000 #3
#addr       =             000 #3
#door       =                000  #6
#birth      =                   000000 #2
#mail       =                         00 #3
#slang      =                           000 #4
#random     =                              0000 #1
#extra_dic  =                                  0  #4
#total_len  =                                   0000 #1
#other      =                                       0




file = open("test.txt","w")



num = 0
for a in _name_list: #38
    for b in _phone_list: #35
        
        for c in _place_list: #30
            
            for d in _addr_list: #27
                
                for e in _door_list: #24
                    
                    for f in _birth_list: #21
                        
                        for g in _mail_list: #15

                            for h in _slang_list: #13

                                for i in _random_list: #10

                                    for j in _extra_dic_list: #6
                                    
                                        for k in _total_len_list: #5

                                            for m in _other_list: #1
                                                num+=1
                                                #print(num)
#                                                print("===========================")
                                                #rule= int(a)*(10**37)+int(b)*(10**34)+int(c)*(10**29)+int(d)*(10**26)+int(e)*(10**23)+int(f)*(10**20)+int(g)*(10**14)+int(h)*(10**12)+int(i)*(10**9)+int(j)*100000+int(k)*10000+int(m)*1
                                                tmp=a+b+c+d+e+f+g+h+i+j+k+m
                                                file.write(tmp+"\n")
#                                                print(f"{1:0{38}}")
#                                               print(a)
#                                               print("-"*3+b)
#                                               print("-"*8+c)
#                                               print("-"*11+d)
#                                               print("-"*14+e)
#                                               print("-"*17+f)
#                                               print("-"*23+g)
#                                               print("-"*25+h)
#                                               print("-"*28+i)
#                                               print("-"*32+j)
#                                               print("-"*33+k)
#                                               print("-"*37+m)
                                                if num == 10:
                                                    exit(0)
                                                    file.close()



                                                    
