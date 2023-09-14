What are Large Language Models?
-
We learn a language at home, at school and later over several years. Our speech experience is a kind of big training set that helps us to articulate with the best reaction in every situation. In computer science, a deep learning algorithm is trained to gain the ability to recognize, summarize, translate, predict, and generate text based on information from large training data sets.
Such language models use statistical methods to predict the next natural language token in a sequence and use previous words to determine what the next word should look like. Large language models pre-trained in neural networks with huge data sets ranging from hundreds of millions to over a trillion parameters can help us regain time when completing a task by leveraging answers from the LLM conversations.

Some software companies started offering LLM services early on. Often the client apps were just wrappers for communication with a LLM hosted in the backend. In 2022, the ecosystem grew very quickly and there was exciting progress news almost daily. This first LLM launch with a tremendous public success was initiated by the company OpenAI with their chat client called chatgpt, based on their hosted models GPT-3.5 and GPT-4. In 2023, Microsoft has started rolling out Copilot for Microsoft Bing. [Huggingfaces](https://huggingface.co/models) has launched its own community platform for hosting models, datasets, libraries, etc. At the VMware Explore Event in Las Vegas there was a Hackathon challenge, and one of the teams curated a [one-stop-shop guide](https://github.com/2023-VMware-Hackathon-HomeTeam/One-stop-shop-to-accelerate-learning-VMware-AI-ML) about learning AI,ML and especially about LLM.

Meta (Facebook) has released some of its LLMs for local hosting for free. The Llama2 LLM was very popular in the open source community. In mid-2023, Ollama.ai began implementing the LLM as installable console applications on MacOS. There are now corresponding setups from the source code for Linux and Windows as well as other variants of LLMs. There should be enough operational computing capacity available to enable reasonably powerful entertainment. The shift from cpu to gpu began quite a while ago, and today's most powerful AI datacenters run on Nvidia gpu hardware. Have a look to [Introduction to AI in the Data Center](https://academy.nvidia.com/en/course/intro-aidc/?cm=12076).

In this blog post you will learn how to install Ollama and use the so-called langchain-document module, which allows you to specify a PDF document as an LLM learning source.


Ollama
-
You can find the Ollama bits on https://ollama.ai with source code on https://github.com/jmorganca/ollama.

Straighforward make run from source code on Microsoft Windows
--

To make run Ollama from source code you will need to install a few tools.

1. Nvidia gpu support does not work yet. Nevertheless if you have a Nvidia gpu, you need for sure to install the drivers.
   https://www.nvidia.com/download/index.aspx

   Nvidia CUDA Toolkit
   https://developer.nvidia.com/cuda-downloads

   After the installation, run the command `nvidia-smi` to check if the gpu has been detected.
   
   <img src="https://github.com/dcasota/ollama-scripts/assets/14890243/8a0bdca4-a011-4a70-bc83-ed48e9640de6" alt="image" width="600">


   PhysX>Blast seems to become necessary for NVidia gpu support, as well.
   https://github.com/NVIDIA-Omniverse/PhysX

3. Git
   https://git-scm.com/download/win

4. Python
   https://www.python.org/downloads/windows/

5. Go
   https://go.dev/doc/install

6. Gcc
   https://sourceforge.net/projects/mingw-w64/files/mingw-w64/mingw-w64-release/

7. Winlibs
   https://winlibs.com/

8. Bazel
   https://github.com/bazelbuild/bazel/releases


In the [Ollama github discussion about Windows support](https://github.com/jmorganca/ollama/issues/188#issuecomment-1710151775), Jeffrey Morgan, initiator of Ollama, recognized the setup importance.
It is good to consult the github source from time to time to benefit from new findings.

After the installation of prerequired component, proceed with the installation of Ollama.

Simply clone the github repository and use Go to compile the source.

```
git clone https://github.com/jmorganca/ollama
cd .\ollama
mkdir ..\.ollama
go generate .\...
go build .
```

In the setup directory you can check if the executable ollama.exe has been created.

Configure the LLM
--

Ollama offers a bunch of variations of LLMs based on Llama und llama2 (open-sourced from Meta) and Falcon (open-sourced from the Technology Innovation Institute in United Arabic Emirates), see https://ollama.ai/library.

It is very important to check the RAM requirements for each LLM.

As example, the [LLM llama2](https://ollama.ai/library/llama2) is downloadable in 3 models: llama2:7b, llama2:13b and llama:70b.

Memory requirements  
7b models generally require at least 8GB of RAM  
13b models generally require at least 16GB of RAM  
70b models generally require at least 64GB of RAM  


First, start the server component of Ollama.

Powershell:
`start-process ollama.exe serve`

Batch console:
`start "Ollama server component" ollama.exe serve`

It opens a window with a similar content as below.  

<img src="https://github.com/dcasota/ollama-scripts/assets/14890243/98f81dd6-fb9a-488b-bd21-7d459a942e73" alt="image" width="800">  


Download the model chosen.

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

Those requirements.txt files are generic and can be run on Linux (and MacOS I guess) as well. However depending on your os, you might need to ensure that dependent libraries are installed as well.

Langchain-document
--

Langchain-document is included as an Ollama example. It reads a PDF document and answers to questions about the document' content.

From the provisioning perspective, it has to be said, that installing the included requirements.txt stills finishes with issues because there is a missing component (tensorflow-macos) which seems to be available on MacOS only. However, with the setup proposed below, the main.py starts flawlessly.

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

The main.py of the langchain-document example loads and processes a pdf document. We simply change the pdf weblink by changing the OnlinePDFLoader line.
The document proposed is from the [University of Applied Sciences Northwestern Switzerland](https://www.fhnw.ch/en/continuing-education/business).

```
# load the pdf and split it into chunks
loader = OnlinePDFLoader("https://www.fhnw.ch/en/continuing-education/business/cas-cybersecurity-and-information-risk-management/media/timetable_cas-cirm.pdf)https://www.fhnw.ch/en/continuing-education/business/cas-cybersecurity-and-information-risk-management/media/timetable_cas-cirm.pdf")
data = loader.load()
```


The model type is specified in the main.py as well. Change it to llama2:70b.
```
llm = Ollama(model="llama2:70b", callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))
```

Start the model with `python .\examples\langchain-document\main.py`.

You now can ask for example `When does the bootcamp 1 start?`.

<img src="https://github.com/dcasota/ollama-scripts/assets/14890243/22542c60-92f5-4acd-bb22-084e3b7c116f" alt="image" width="1000">


For further tinkering, see https://github.com/jmorganca/ollama/blob/main/docs/tutorials/langchainpy.md. 


Are LLM safe and secure?
-
The trustworthiness of LLM is a big challenge. Companies have concerns about integrating cloud-based LLM solutions in their daily work. 

AI risk management has become a hot topic. In the United States, the National Institute of Standards and Technology (NIST) initiated the
- [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

Vendors like Microsoft put themselves in charge for API transparency. See e.g. [Microsoft Trusted AI](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/innovate/best-practices/trusted-ai)

The first time I've started the langchain example `python .examples\langchain\main.py`, I received a long answer about AI and humans:  

_Hello! It's nice to meet you. Unterscheidung between humans and AIs is important for various reasons:_  

_1. Personal privacy and security: As a human, you have the right to privacy and security. AI systems, on the other hand, are designed to collect and process vast amounts of data, which can raise concerns about their potential impact on personal privacy and security._  
_2. Accountability and transparency: Humans are accountable for their actions, while AIs may be opaque in their decision-making processes. It is essential to understand how AI systems arrive at their conclusions and hold them responsible for their actions._  
_3. Ethical considerations: AI raises ethical concerns, such as bias, fairness, and transparency. Humans need to be aware of these issues and take steps to address them in the development and deployment of AI systems._  
_4. Human-centered design: AIs are designed to assist humans, not replace them. Understanding the differences between humans and AIs is crucial for designing AI systems that complement human capabilities and enhance overall well-being._  
_5. Building trust: Trust is a critical factor in any relationship, including those between humans and AIs. By recognizing and respecting the distinctions between humans and AIs, we can build more effective and trustworthy AI systems._  
_6. Improving communication: Humans and AIs communicate differently, with each having its unique language and cognitive processes. Recognizing these differences can help improve communication between humans and AIs, leading to better collaboration and decision-making._  
_7. Enhancing creativity: Humans and AIs have distinct creative abilities, with AIs exceling in certain areas like data analysis and pattern recognition. By leveraging these strengths, we can foster a more comprehensive approach to problem-solving and creativity._  
_8. Addressing societal implications: As AI becomes more integrated into various aspects of society, it is essential to understand the impact it has on different groups within society. This includes recognizing the potential for AI to exacerbate existing social inequalities or create new ones._  
_9. Promoting responsible innovation: By acknowledging and respecting the distinctions between humans and AIs, we can promote responsible innovation that takes into account both the capabilities and limitations of each._  
_10. Encouraging critical thinking: Recognizing the differences between humans and AIs can encourage critical thinking about the potential consequences of AI and how it can be used ethically and responsibly in various domains._  

_In conclusion, recognizing and respecting the distinctions between humans and AIs is essential for developing effective, ethical, and responsible AI systems that benefit society as a whole._  


A sort of ethics and transparency explanation wasn't expected as the main.py contains a simple "hello".

```
from langchain.llms import Ollama
llm = Ollama(model="llama2")
res = llm.predict("hello")
print (res)
```

So, in everyday life how can we detect "good" and "bad" LLM answers?

In 2020, early detection of fake news has been discussed at the [European Conference on Machine Learning and Principles and Practice of Knowledge Discovery in Databases](https://ecmlpkdd.org/).
Microsoft Research published an article about [Leveraging Multi-Source Weak Social Supervision for Early Detection of Fake News](https://arxiv.org/pdf/2004.01732.pdf). The [model github source](https://github.com/microsoft/MWSS) contains a security call-to-action about Microsoft's Bug Bounty Program.

Maintaining a LLM integrity must handle concerns about training data poisoning, prompt injection, supply chain vulnerabilities, sensitive information disclosure, and many more. 
The Open Worldwide Application Security Project (OWASP) is a nonprofit foundation that works to improve the security of software.
In July 2023 they published a comprehensive guide about how to secure LLMs: [OWASP-Top-10-for-LLMs-2023-v05](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-2023-v05.pdf).

A LLM-based Multiple Choice Solver - the dream of students ?
-

The beginning of a LLM journey can be full of research first. Here a [sample paper](https://arxiv.org/pdf/2308.07317.pdf) from students at the Boston University about their journey. In their work it is explained why they needed to prepare a 25K training data set to a given multiple-choice format as input for each question. The students decided to do some performance research using LLM variations of Llama2. As model dataset training hardware they had time-restricted access to an A100 NVidia GPU based environment. The students met their own expectations, created an adopted LLM called Open-Platypus from the training phase, tuned & published it to the huggingfaces platform, and made their work publicly available.
In Ollama, not the Open-Platypus LLM but the evolved [Open-Orca Platypus 13B](https://huggingface.co/Open-Orca/OpenOrca-Platypus2-13B) has been integrated.

It would be a pitty to deny LLM-based multiple choice solvers. It helps to train our brain. The human brain is the ultimate autonomous system, with a weight of 1.2 to 1.4 kg and 86x10^9 neurones. Multiple-Choice Learning means to experience the same quantization bits preference for the environment again and again, you have been trained for - with a dark side of resilience. Be aware and have fun with LLM!
