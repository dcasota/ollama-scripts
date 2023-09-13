What are Large Language Models?
-
From home, at school and later on we learn a language over several years. This said, our language experience is a sort of a large training set which helps us to articulate in each situation with the best response. In computer science, a deep learning algorithm is trained to achieve the ability to recognize, summarize, translate, predict and generate text based on information from large training data sets.
Language models use statistical methods to predict the next natural language token in a sequence, determining what the next word should look like based on previous words. Pretrained in neural networks with huge data sets ranging from hundreds of millions to over a trillion parameters, large language models can help us with reclaiming time by utilizing good responses from LLM conversations.

Manufacturers such as Microsoft offer online services for hosted LLMs. The client programs themselves are just wrappers for the user input.

The provider Meta has released some of its LLMs so that you can host them locally yourself. Sufficient operational computing capacity should be made available to enable reasonably high-performance entertainment. The Llama2 LLM became very popular in the open source community.
Ollama.ai began implementing the LLM as installable console applications on MacOS in mid-2023.
There are now corresponding setups from source code for Linux and Windows, and also more variations of LLMs.

In this blog entry I will show how to install ollama and make use of the so-called langchain-document module which allows to specify a pdf document as LLM learning source.

Ollama
-
You can find the ollama bits on https://ollama.ai with source code on https://github.com/jmorganca/ollama.

Straighforward make run from source code on Microsoft Windows
--

To make run Ollama from source code you will need to install a few tools.

1. Nvidia gpu drivers assuming an Nvidia gpu

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
<img src="https://github.com/dcasota/ollama-scripts/assets/14890243/98f81dd6-fb9a-488b-bd21-7d459a942e73" alt="image" width="800">


Download the selected model.

`.\ollama.exe pull llama2:70b`

The progress bar visualizes the model download progress.


Run the model.

`.\ollama.exe run llama2:70b`

Be aware - depending on the model, you get weired answers.

Model use cases - examples
--

Ollama comes with a bunch of examples for different use cases, see directory `examples`.

<img src="https://github.com/dcasota/ollama-scripts/assets/14890243/8f5562b1-bf5e-4321-9c54-da5a780c6a41" alt="image" width="200">


All examples are written in python. You find in each subdirectory a python file named `main.py`.

<img src="https://github.com/dcasota/ollama-scripts/assets/14890243/9720f1e2-459c-4553-960f-aec053c44a5d" alt="image" width="120">

At this point, it is good to know, that the first setup might not be enough.

Simply starting the file with `python.exe main.py` usually stops with issues because prerequired libraries are not installed.

Those libraries can be installed using the python pip installer.

`pip install -r requirements.txt`

Those requirements.txt files are generic and can be run on Linux (and MacOS I guess) as well. However depending on your os, you might need to ensure that dependent prerequired libraries are installed as well.

Langchain-document example
---

Here an example setup for langchain-document. It must to be said, that installing the requirements.txt stills finishes with issues because there is a missing component which seems to be available on MacOS only. However, with the setup proposed, the main.py starts flawlessly.

```
pip install unstructured
pip install pdf2image
pip install pdfminer
pip install pdfminer.six
pip install pyproject.toml
pip install pysqlite3
pip install gpt4all
pip install chromadb
pip install tensorflow
pip install opencv-python
pip install bazel-runfiles
pip install -r .\examples\langchain-document\requirements.txt
pip install langchain
```

The main.py of the langchain-document example loads and processes a pdf document. We can change the pdf weblink by changing the OnlinePDFLoader line.

```
# load the pdf and split it into chunks
loader = OnlinePDFLoader("https://www.fhnw.ch/en/continuing-education/business/cas-cybersecurity-and-information-risk-management/media/timetable_cas-cirm.pdf)https://www.fhnw.ch/en/continuing-education/business/cas-cybersecurity-and-information-risk-management/media/timetable_cas-cirm.pdf")
data = loader.load()
```

The model is specified in the main.py as well. Change it to use llama2:70b.
```
llm = Ollama(model="llama2:70b", callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))
```

Start the model with `python .\examples\langchain-document\main.py`.

Ask: "When does the bootcamp 1 start?"

For further tinkering, see https://github.com/jmorganca/ollama/blob/main/docs/tutorials/langchainpy.md. 


