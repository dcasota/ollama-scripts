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

Straighforward make run from source code on Microsoft Windows
--

To make run Ollama from source code you will need to install a few tools.

1. Nvidia gpu drivers

2. Git

3. Python

4. Go

5. Gcc

6. Winlibs

7. Bazel


Accordingly to the Ollama reference, the setup is straightforward.

```
git clone https://github.com/jmorganca/ollama
cd .\ollama
mkdir ..\.ollama
go generate .\...
go build .
```

In the setup directory, you can check if the executable ollama.exe has been created.

Configure the LLM
--

Ollama offers a few LLMs, see https://ollama.ai/library.

It is very important to check the RAM requirements for each LLM.

As example, the [LLM llama2](https://ollama.ai/library/llama2) is downloadable in 3 models: llama2:7b, llama2:13b and llama:70b, hence choose wisely.

Memory requirements
7b models generally require at least 8GB of RAM
13b models generally require at least 16GB of RAM
70b models generally require at least 64GB of RAM


First, start the server component of ollama.

Powershell:
`start-process ollama.exe serve`

Batch console:
`start "Ollama server component" ollama.exe serve`

It opens a window with a similar content as below.
![image](https://github.com/dcasota/ollama-scripts/assets/14890243/98f81dd6-fb9a-488b-bd21-7d459a942e73)


Download the selected model.

`.\ollama.exe pull llama2:70b`

The progress bar visualizes the model download progress.


Run the model.

`.\ollama.exe run llama2:70b`

Examples
--

Ollama comes with a bunch of examples for different use cases, see directory `examples`.

![image](https://github.com/dcasota/ollama-scripts/assets/14890243/8f5562b1-bf5e-4321-9c54-da5a780c6a41)

All examples are written in python.

At this point, it is good to know, that the first setup might not be enough. The python examples have additional prerequisites. The requirements


