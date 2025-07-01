# ETF: An Entity Tracing Framework for Hallucination Detection in Code Summaries

This repository contains the code and dataset details for the paper: [ETF: An Entity Tracing Framework for Hallucination Detection in Code Summaries](https://arxiv.org/abs/2410.14748) 

We introduce CodeSumEval for studying hallucination detection in code summarisation, featuring 411 summaries from 7 LLMs and ∼10K entity-level samples with an explanation of causes for hallucinations as per taxonomy. This dataset is available on huggingface: [CodeSumEval](https://huggingface.co/datasets/kishanmaharaj/ETF-CodeSumEval)

## Introduction 


Recent advancements in large language models (LLMs) have significantly enhanced their ability to understand both natural language and code, driving their use in tasks like natural language-to-code (NL2Code) and code summarisation. However, LLMs are prone to hallucination—outputs that stray from intended meanings. Detecting hallucinations in code summarisation is especially difficult due to the complex interplay between programming and natural languages. We introduce a first-of-its-kind dataset, CodeSumEval, with ∼10K samples, curated specifically for hallucination detection in code summarisation. We further propose a novel Entity Tracing Framework (ETF) that a) utilises static program analysis to identify code entities from the program and b) uses LLMs to map and verify these entities and their intents within generated code summaries. Our experimental analysis demonstrates the framework’s effectiveness, leading to a 73% F1 score. The proposed approach provides a method for detecting hallucinations by tracing entities from the summary to the code, allowing us to evaluate summary accuracy and localise the error within the summary.

This diagram illustrates our end-to-end Entity Tracing Framework (ETF), which takes source code and a corresponding summary as input and returns whether the summary is hallucinated or not.
![ETF-framework-diagram](https://github.com/user-attachments/assets/04c34c9f-d239-4225-b5c9-821099f50fb4)

## Cite the work

If you make use of the dataset or the code, please cite our paper.
```
@article{maharaj2024etf,
  title={ETF: An Entity Tracing Framework for Hallucination Detection in Code Summaries},
  author={Maharaj, Kishan and Munigala, Vitobha and Tamilselvam, Srikanth G and Kumar, Prince and Sen, Sayandeep and Kodeswaran, Palani and Mishra, Abhijit and Bhattacharyya, Pushpak},
  journal={arXiv preprint arXiv:2410.14748},
  year={2024}
}
```
