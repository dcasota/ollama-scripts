What are Large Language Models?
-
Human language is very extensive and we humans learn a language over several years. A deep learning algorithm has the ability to recognize, summarize, translate, predict and generate text and other content based on information from large training data sets.
Language models use statistical methods to predict the next natural language token in a sequence, determining what the next word should look like based on previous words. In neural networks, language models are trained on huge data sets ranging from hundreds of millions to over a trillion parameters. The result of the parameterization and the many runs is a so-called Large Language Model.

Manufacturers such as Microsoft offer online services for hosted LLMs. The client programs themselves are just wrappers for the user input.

The provider Meta has released some of its LLMs so that you can host them locally yourself. Sufficient operational computing capacity should be made available to enable reasonably high-performance entertainment. The Llama2 LLM became very popular in the open source community.
Ollama.ai began implementing the LLM as installable console applications on MacOS in mid-2023.
There are now corresponding setups from source code for Linux and Windows, and also more variations of LLMs.

In this blog entry I will show how to install ollama and make use of the so-called langchain module which allows to specify a pdf document as LLM learning source.

Ollama
-
You can find the ollama bits on https://ollama.ai with source code on https://github.com/jmorganca/ollama.

