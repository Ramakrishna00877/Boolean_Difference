#Finding Consensus function, Smoothing function and Boolean difference

#Sorting each term in the list
def sort_list_terms(temp):
    sort=list(temp.split("+"))
    for i in range(0,len(sort)):
        sort[i]=''.join(sorted(sort[i]))
    return sort

#Applying a+ab=a and a+Ab=a+b rules on a boolean function
def redundant_theorem(red):
    sort=sort_list_terms(red)
    red="+".join(sort)
    out=list(red.split("+"))
    for i in range(len(out)-1):
        if out[i].find(out[i+1])!=-1:
            out[i]=out[i+1]
        elif out[i+1].find(out[i])!=-1:
            out[i+1]=out[i]
        elif out[i].find(out[i+1])==-1:
            if len(out[i])<len(out[i+1]):
                if out[i].islower():
                    if out[i].upper() in list(out[i+1]):
                        out[i+1]=out[i+1].replace(out[i].upper(),'')
                elif out[i].isupper():
                    if out[i].lower() in list(out[i+1]):
                        out[i+1]=out[i+1].replace(out[i].lower(),'')
            elif len(out[i+1])<len(out[i]):
                if out[i+1].islower():
                    if out[i+1].upper() in list(out[i]):
                        out[i]=out[i].replace(out[i+1].upper(),'')
                elif out[i+1].isupper():
                    if out[i+1].lower() in list(out[i]):
                        out[i]=out[i].replace(out[i+1].lower(),'')
    fin_output=out
    fin_output=list(dict.fromkeys(fin_output))
    fin_output="+".join(fin_output)
    
    return fin_output

#Applying Ab+ab=b rule on a boolean function
def redundant_theorem2(red2):
    terms = red2.split("+") 
    temp = []

    for term in terms:
        term = term.strip()
        if term:
            temp.append(term)  
    i = 0
    while i < len(temp) - 1:
        term1 = temp[i]
        term2 = temp[i + 1]
        common_chars = set(term1).intersection(set(term2))
        for char in common_chars:
            temp1 = term1.replace(char, '', 1)
            temp2 = term2.replace(char, '', 1)
            if temp1.lower() == temp2.lower():
                temp[i] = char
                temp[i + 1] = char
                break
        i += 1
    unique_terms = list(dict.fromkeys(temp))
    fin_output = "+".join(unique_terms)
    return fin_output

#Applying complementary theorem on a boolean function a.A=0
def complementary_theorem(comp):
    sort=sort_list_terms(comp)
    comp="+".join(sort)
    rev_term=comp.split("+")
    con_final=''
    for rev in rev_term:
        if len(rev)!=1:
            temp=list(rev)
            for i in range(0,len(temp)):
                if temp[i].isupper():
                    l=temp[i].lower()
                else:
                    l=temp[i].upper()
                if l.find(rev)==-1 and i==len(temp)-1:
                    con_final=rev+"+"+con_final
                elif rev.find(l)!=-1:
                    break
        else:
            con_final=rev+"+"+con_final
    con_final=con_final[:-1]
    return con_final

#applying a+A=1 and A+1=1 rules on a boolean function
def complementary_theorem2(bool_expr):
    sort=sort_list_terms(bool_expr)
    (sort)
    if str(1) not in sort:
        for i in range(len(sort)-1):
            if sort[i].islower() and sort[i]!=sort[i+1]:
                if sort[i]==sort[i+1].lower():
                    sort[i]=1
                    sort[i+1]=1
                    break
            elif sort[i].isupper() and sort[i]!=sort[i+1]:
                if sort[i]==sort[i+1].upper():
                    sort[i]=1
                    sort[i+1]=1
                    break
        if 1 in sort:
            return str(1)
        else:
            return bool_expr
    elif str(1) in sort:
        return str(1)
    else:
        return bool_expr

#applying a+0=a rule on a boolean function
def complementary_theorem3(bool_expr):
    sort=sort_list_terms(bool_expr)
    sort=list(dict.fromkeys(sort))
    if str(0) in sort:
        temp=sort.index(str(0))
        sort.remove(sort[temp])
    bool_expr='+'.join(sort)
    if len(sort)==0:
        return str(0)
    else:
        return bool_expr

#Multiplying two boolean functions
def mul_boolean_fun(bool1,bool2):
    if f[0]!=str(0) and f[1]!=str(0):
        f1=list(f[0].split("+"))
        f2=list(f[1].split("+"))
        con_fin=''
        for i in range(0,len(f1)):
            for j in range(0,len(f2)):
                con_out=''
                if f1[i]==f2[j]:
                    con_out=f1[i]
                elif f1[i].find(f2[j])!=-1 or f2[j].find(f1[i])!=-1:
                    if len(f1[i])>len(f2[j]):
                        con_out=f1[i]
                    elif len(f1[i])<len(f2[j]):
                        con_out=f2[j]
                elif f1[i]!=f2[j] :
                    if f1[i]!=str(1) and f2[j]!=str(1):
                        con_out=f1[i]+f2[j]
                    elif f1[i]==str(1):
                        con_out=f2[j]
                    elif f2[j]==str(1):
                        con_out=f1[i]
                con_out=list(con_out)
                con_out=list(dict.fromkeys(con_out))
                con_out=''.join(con_out)
                con_fin=con_out+"+"+con_fin
        con_fin=con_fin[:-1]
        for i in range(2):
            con0=str(complementary_theorem(con_fin))
            con1=str(redundant_theorem(con0))
            con3=str(redundant_theorem2(con1))
            con4=str(complementary_theorem2(con3))
            con2=str(complementary_theorem3(con4))
            con_fin=con2
        if len(con2)!=0:
            return con2
        else:
            con2=str(0)
            return con2
    elif f[0]==str(1) and f[1]==str(1):
        con2=str(1)
        return con2
    elif f[0]==str(0) or f[1]==str(0):
        con2=str(0)
        return con2

#Giving inputs boolean function and cofactor varibale
bool_expr = input("Enter boolean expression f:")#Enter boolean expression.
sort=sort_list_terms(bool_expr)
for i in range(len(sort)):
    sort[i]=''.join(list(dict.fromkeys(list(sort[i]))))
                       
bool_expr="+".join(sort)
dup_bool_expr =bool_expr.replace("+",'')
var_in = input("Enter variable or cube:") #Enter the variable to find cofactor.
dup_var_in=var_in.isalpha()
var_in=sorted(var_in)#Sorting the var_in if we give cube as input.
inv=[]
temp=''
f=[]
#finding cofactor and cofactor bar for the variable
#Loop will be executed only if all inputs are not empty and and contains only alphabets and "+".
if len(bool_expr)!=0 and len(var_in)!=0 and dup_var_in==1 and dup_bool_expr.isalpha()==1 :
    #Finding inverse of variable.
    for rev in var_in:
        if rev.isupper()==True:
            temp=rev.lower()
            inv.append(temp)
        else:
            temp=rev.upper()
            inv.append(temp)
    for rt in range(0,2):
        #Removing duplicate terms in boolean expression.
        list_minterms = list(bool_expr.split("+"))
        list_minterms=list(dict.fromkeys(list_minterms))
        cofactor=""
        #Finding cofactor for each varaiable.
        for i in range(0,len(inv)):
            cofactor=""
            for z in list_minterms:
                x=z.find(inv[i])
                w=z.find(var_in[i])
                if var_in[i]==z:
                    cofactor="1+"
                    break
                elif inv[i]==z:
                    cofactor="0+"
                elif x==-1 and w==-1:
                    cofactor=z+"+"+cofactor
                elif x==-1 and w!=-1:
                    v=z.replace(var_in[i],'')
                    cofactor=v+"+"+cofactor       
            cofactor=cofactor[:-1]
            list_minterms=list(cofactor.split("+"))
        if len(cofactor)!=0:
            cofactor=cofactor
        else:
            cofactor=str(0)
        f.append(cofactor)
        temp=inv
        inv=var_in
        var_in=temp
        list_minterms=list(bool_expr.split("+"))
else:
    print("Required inputs are not given")
for i in range(len(f)):
    smf0=str(complementary_theorem(f[i]))
    smf1=str(redundant_theorem(smf0))
    smf3=str(redundant_theorem2(smf1))
    smf4=str(complementary_theorem2(smf3))
    smf2=str(complementary_theorem3(smf4))
    f[i]=smf2
print("Cofactor of f: "+f[0])
print("Cofactor of fbar: "+f[1])

#finding smoothing of a function f
if f[0]!=str(0) and f[0]!=str(1):
    smf=f[0]+"+"+f[1]
    smf_minterms = list(smf.split("+"))
    smf_minterms=list(dict.fromkeys(smf_minterms))
    smf_minterms='+'.join(smf_minterms)
    for i in range(2):
        smf0=str(complementary_theorem(smf_minterms))
        smf1=str(redundant_theorem(smf0))
        smf3=str(redundant_theorem2(smf1))
        smf4=str(complementary_theorem2(smf3))
        smf2=str(complementary_theorem3(smf4))
        smf_minterms=smf2
    print("Smoothing function: "+smf2)
else:
    smf2=str(1)
    print("Smoothing function: ",smf2)

#finding consensus of a function f
consensus_out=str(mul_boolean_fun(f[0],f[1]))
print("Consensus function: ",consensus_out)

#finding boolean difference
#finding consensus function bar
temp=[]
consensus_out=list(consensus_out.split("+"))
for i in consensus_out:
    temp1=list(i)
    temp2=[]
    for j in temp1:
        if j.isupper():
            temp2.append(j.lower())
        else:
            temp2.append(j.upper())
    temp.append('+'.join(temp2))
#multipling each term after evaluating consensus function bar
if (''.join(temp))!=str(0) and (''.join(temp))!=str(1):
    if len(temp)>1:
        for i in range(0,len(temp)-1):
            temp1=list(temp[i].split("+"))
            temp2=list(temp[i+1].split("+"))
            temp4=''
            for j in range(0,len(temp1)):
                temp3=''
                for k in range(0,len(temp2)):
                    if temp1[j]==temp2[k]:
                        temp3=temp1[j]+"+"+temp3
                    else:
                        temp3=temp1[j]+temp2[k]+"+"+temp3
                temp3=temp3[:-1]
                temp4=temp3+"+"+temp4
            temp[i+1]=temp4[:-1]
    else:
        temp4="".join(temp)+"+"
    temp4=temp4[:-1]
    sort=sort_list_terms(temp4)
    temp4="+".join(sort)
    for i in range(3):
            con0=str(complementary_theorem(temp4))
            con1=str(redundant_theorem(con0))
            con3=str(redundant_theorem2(con1))
            con4=str(complementary_theorem2(con3))
            con2=str(complementary_theorem3(con4))
            temp4=con2
    con_out=list(con2.split("+"))
    con_out=list(dict.fromkeys(con_out))
    con_out='+'.join(con_out)
elif (''.join(temp))==str(0):
    con_out=str(1)
elif (''.join(temp))==str(1):
    con_out=str(0)
print("consensus function bar: ",str(con_out))

#multiplying consensus funcation bar with smoothing
f[0]=con_out
f[1]=smf2
bool_diff=mul_boolean_fun(f[0],f[1])
print("Boolean difference: "+bool_diff)

