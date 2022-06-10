from CFD_Scoring_1 import*

def loadData(inputpath):
   
    with open(inputpath) as f:
        sgRNA_item=[]
        DNA_item=[]
        for line in f:
            ll = [i for i in line.strip().split(',')]
            sgRNA_item.append(ll[0])
            DNA_item.append(ll[1])
    return DNA_item,sgRNA_item

glove_inputpath = "output\keras_GloVeVec_5_100_10000.csv"
hek_inputpath = "output\hek293_off_Glove.txt"
K562_inputpath = "output\K562_off_Glove.txt"
DNA_item,sgRNA_item = loadData(hek_inputpath)
f=0 

while f<len(sgRNA_item):
    off =DNA_item[f]
    print(off)
    wt = sgRNA_item[f]
    print(wt)
    m_wt = re.search('[^ATCG]',str(wt))
    m_off = re.search('[^ATCG]',str(off))
    if (m_wt is None) and (m_off is None):
        
        pam = off[-2:]       
        sg = off[:-3]         
        cfd_score = calc_cfd(wt,sg,pam) 
        print("CFD score:",cfd_score)
        f=f+1