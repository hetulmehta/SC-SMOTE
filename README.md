# SCSMOTE- SEMANTIC-COSINE SYNTHETIC MINORITY OVERSAMPLING TECHNIQUE

## SMOTE Variant for textual data

Semantic-Cosine-based Synthetic Minority Over-sampling Technique (SC-SMOTE) is used to generate new words with semantic meaning by leveraging the concept of cosine similarity. The proposed method involves converting words to vectors using GloVe embeddings and then generating new vectors using SMOTE oversampling.  The closest GloVe embedding is then identified and considered as the new word generated. However, the key innovation of this approach lies in how it ensures the semantic relevance of the generated words. To achieve this, cosine similarity is calculated between the newly generated vector and a relevant domain-specific term.

## Features

- Works on textual data
- Maintains the semantic meaning of synthetic data
- Easy to implement

### Installation :

```
pip install scsmote-package
```

---

### Example for using

```
from scsmote_package import scsmote
import numpy as np

with open("glove/glove.6B.200d.txt", encoding="utf8") as file:
    data = file.readlines()
for i in range(len(data)):
    data[i] = data[i][:-1]
data_dict = dict()
for i in range(len(data)):
    split_data = data[i].split()
    data_dict[split_data[0]] = np.array(split_data[1:]).astype('float64')

print(scsmote(['happy','sad','angry','mad','upset'],'emotions',data_dict))
```

---

<h3 align="center"><b>Developed with :heart: by <a href="https://github.com/hetulmehta">Hetul Mehta, Siddhi Mule, Dhruv Mistry</a>
