import numpy as np
from scipy import spatial
from sklearn.neighbors import NearestNeighbors
from numpy.linalg import norm
from tqdm import tqdm

def scsmote(slist,category,data_dict):
    n=len(slist)
    if n>5:
        n=5
    vectors=[]
    x=[]
    words=[]
    for i in slist:
        try:
            vectors.append(data_dict[i])
            words.append(i)
        except:
            x.append(i)
    c=[]
    error=[]
    for i in x:
        s=i.split(" ")
        for j in s:
            c.append(j)
    for i in c:
        try:
            vectors.append(data_dict[i])
            words.append(i)
        except:
            error.append(i)
    def random_sample(vectors):
        x=random.choice(vectors)
        return x
    def knn(vec):
        nbs=NearestNeighbors(n_neighbors=n,metric='euclidean',algorithm='kd_tree').fit(vec)
        euclidean,indices= nbs.kneighbors(vec)
        return indices,euclidean
    def random_number():
        return np.random.random(1)[0]

    def find_closest_embeddings(embedding):
        return sorted(data_dict.keys(), key=lambda word: spatial.distance.euclidean(data_dict[word], embedding))

    def cosine_similarity(a, b):
        nominator = np.dot(a, b)
        a_norm = np.sqrt(np.sum(a**2))
        b_norm = np.sqrt(np.sum(b**2))
        denominator = a_norm * b_norm
        cosine_similarity = nominator / denominator
        return cosine_similarity

    index,dist=knn(vectors)
    random=random_number()
    newwords=[]
    for i in tqdm(index):
        newsamp=(vectors[i[0]]-vectors[i[1]])*random
        finalsamp=vectors[i[0]]+abs(newsamp)
        l1=find_closest_embeddings(finalsamp)[0:15]
        newwords.append(l1)
    flist=[]
    for i in newwords:
        for j in i:
            if j not in flist and j not in words:
                flist.append(j)
    count=0
    a1=[]
    a2=[]
    for i in flist:
        if cosine_similarity(data_dict[category],data_dict[i])>0.5:
            a2.append(i)
    newlist=[]
    for i in a2:
        near=(find_closest_embeddings(data_dict[i])[0:15])
        newlist.append(near)
    flist=[]
    for i in newlist:
        for j in i:
            if j not in flist:
                flist.append(j)
    newlist=[]
    for i in tqdm(flist):
        near=(find_closest_embeddings(data_dict[i])[0:5])
        newlist.append(near)
    for i in newlist:
        for j in i:
            if cosine_similarity(data_dict[category],data_dict[j])>0.15:     
                if j not in flist:
                    flist.append(j)
    fflist=[]
    for i in flist:
        if cosine_similarity(data_dict[category],data_dict[i])>0.3:
            fflist.append(i)
    for i in fflist:
        if i not in slist:
            slist.append(i)
    return slist