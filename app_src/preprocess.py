import json
from os import O_APPEND 
with open('./quiz_data/index.json') as f:
  data = json.load(f)

gen=[]
ind=[]
st=[]
sp=[]
mela=[]
biz=[]

for num in data.keys():
    with open(f'./quiz_data/{data[num]}') as f1:
        lo_data = json.load(f1) 
    for ques in lo_data.keys():
        if("mela" in lo_data[ques]["tags"]):  
            mela.append((num,ques))
        
        if("gen" in lo_data[ques]["tags"]):  
            gen.append((num,ques))
        
        if("ind" in lo_data[ques]["tags"]):  
            ind.append((num,ques))
        
        if("st" in lo_data[ques]["tags"]):  
            st.append((num,ques))
        
        if("sp" in lo_data[ques]["tags"]):  
            sp.append((num,ques))
        
        if("biz" in lo_data[ques]["tags"]):  
            biz.append((num,ques))
        
with open('./quiz_data/tagged/mela.json', 'w') as f:
    json.dump(mela, f)

with open('./quiz_data/tagged/gen.json', 'w') as f:
    json.dump(gen, f)

with open('./quiz_data/tagged/ind.json', 'w') as f:
    json.dump(ind, f)

with open('./quiz_data/tagged/st.json', 'w') as f:
    json.dump(st, f)

with open('./quiz_data/tagged/sp.json', 'w') as f:
    json.dump(sp, f)

with open('./quiz_data/tagged/biz.json', 'w') as f:
    json.dump(biz, f)