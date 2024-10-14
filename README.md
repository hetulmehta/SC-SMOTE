# SCSMOTE- SEMANTIC-COSINE SYNTHETIC MINORITY OVERSAMPLING TECHNIQUE

## SMOTE Variant for Textual Data

Semantic-Cosine-based Synthetic Minority Over-sampling Technique (SC-SMOTE) is used to generate new words with semantic meaning by leveraging the concept of cosine similarity. The proposed method involves converting words to vectors using GloVe embeddings and then generating new vectors using SMOTE oversampling.  The closest GloVe embedding is then identified and considered as the new word generated. However, the key innovation of this approach lies in how it ensures the semantic relevance of the generated words. To achieve this, cosine similarity is calculated between the newly generated vector and a relevant domain-specific term.


### Installation :

```
pip install scsmote-package
```

---

## Features

- Generates synthetic textual data that is semantically relevant and contextually appropriate
- Improves the accuracy of labelled datasets compared to original SMOTE or no oversampling
- Specifically designed for handling imbalanced textual data
- Uses cosine similarity to ensure the relevance of generated words

## Usage

Here's a basic example of how to use SC-SMOTE:

```python
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

## Background

SC-SMOTE was developed to address the challenges of applying SMOTE to textual data, particularly in the context of classifying drug-related webpages on the dark web. It combines the SMOTE algorithm with cosine similarity to ensure that the generated synthetic samples are semantically meaningful and relevant to the minority class.

## Advantages

- Improves classification performance on imbalanced textual datasets
- Reduces the time and effort required for manual data labeling
- Generates contextually appropriate synthetic samples
- Helps in avoiding overfitting that can occur with traditional SMOTE

## GitHub Repository

For more detailed information, source code, and contributions, please visit our GitHub repository:

[https://github.com/hetulmehta/SC-SMOTE](https://github.com/hetulmehta/SC-SMOTE)

## Requirements

- Python 3.7+
- numpy
- pandas
- scikit-learn
- gensim

## Contributing

We welcome contributions to the SC-SMOTE project. Please feel free to submit issues and pull requests on our GitHub repository.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/hetulmehta/SC-SMOTE/blob/main/LICENSE) file in the GitHub repository for details.

## Contact

For any queries or suggestions, please open an issue on the GitHub repository.