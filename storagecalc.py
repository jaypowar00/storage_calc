istr = input("Enter Operation : ")
values=[]
operations=[]
for i in range(len(istr)):
    if istr[i]=='+':
        operations.append((i,'+'))
    elif istr[i]=='-':
        operations.append((i,'-'))
    else:
        continue
operations
for i in range(len(operations)+1):
    if i==0:
        values.append(istr[:operations[i][0]].split()[0])
    elif i<=len(operations)-1:
        values.append(istr[operations[i-1][0]+1:operations[i][0]].split()[0])
    else:
        values.append(istr[operations[i-1][0]+1:].split()[0])
values
for i in range(len(values)):
    values[i]=int(values[i].split('tb')[0])*1024*1024*1024*1024 if 'tb' in values[i] else int(values[i].split('gb')[0])*1024*1024*1024 if 'gb' in values[i] else int(values[i].split('mb')[0])*1024*1024 if 'mb' in values[i] else int(values[i].split('kb')[0])*1024 if 'kb' in values[i] else int(values[i].split('b')[0]) if 'b' in values[i] else int(values[i].split('TB')[0])*1024*1024*1024*1024 if 'TB' in values[i] else int(values[i].split('GB')[0])*1024*1024*1024 if 'GB' in values[i] else int(values[i].split('MB')[0])*1024*1024 if 'MB' in values[i] else int(values[i].split('KB')[0])*1024 if 'KB' in values[i] else int(values[i].split('B')[0])
total=0.0
for i in range(len(values)):
    if i>0 and operations[i-1][1]=="+":
        total+=float(values[i])
    elif i>0 and operations[i-1][1]=='-':
        total-=float(values[i])
    else:
        total=float(values[i])
print("_"*50)
if int(total/(1024*1024*1024*1024))>0:
    print(f'Total space : {total/(1024*1024*1024*1024)} TB')
elif int(total/(1024*1024*1024))>0:
    print(f'Total space : {total/(1024*1024*1024)} GB')
elif int(total/(1024*1024))>0:
    print(f'Total space : {total/(1024*1024)} MB')
elif int(total/(1024))>0:
    print(f'Total space : {total/1024} KB')
else:
    print(f'Total space : {total} Bytes')