#!/usr/bin/env python3


#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#
#
# Information: modified Ollama privateGPT
#
#
#---------------------------------------------------------------------------------------------------
#
#
# Autor(en): Daniel Casota (DCA)
#
# Aktuell:    20.05.2024 V0.3  DCA minor updates
# Änderungen: 15.05.2024 V0.1  DCA Copy of original Ollama privateGPT 0.1.38, langchain_community added
#             18.05.2024 V0.2  DCA ignore deprecated warnings added
#             20.05.2024 V0.3  DCA minor updates
#             06.06.2024 V0.4  DCA EMBEDDINGS_MODEL_NAME=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
#                                  model = os.environ.get("MODEL", "llama3")
#                                  replacement to 'from langchain_community.embeddings'
#                                  Using Ollama privateGPT 0.1.41
#             04.08.2024 V0.4  DCA LLM replacement with all-MiniLM-L6-v2 and llama3.1
#
#---------------------------------------------------------------------------------------------------
#
# Voraussetzungen: Windows 11 mit Windows Subsystem for Linux und C:\My Web Sites\ENSI
#
# Aufruf durch: PrivateèGT for ENSI docs start.py
#
# Inputvariablen: (keine)
# CmdLine-Parameter (keine)
#
# Outputvariablen: (keine)
# Rückgabewert: (keine)
#---------------------------------------------------------------------------------------------------
#
# Plattform: Getestet auf Windows 11 WSL2
#
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

import sys
if not sys.warnoptions:
   import warnings
   warnings.simplefilter("ignore")
   with warnings.catch_warnings():
        warnings.filterwarnings("ignore",category=DeprecationWarning)
        warnings.filterwarnings("ignore",category=FutureWarning)  

from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
import chromadb
import os
import argparse
import time

# model = os.environ.get("MODEL", "llama2-uncensored")
model = os.environ.get("MODEL", "llama3.1")
# For embeddings model, the example uses a sentence-transformers model
# https://www.sbert.net/docs/pretrained_models.html 
# "The all-mpnet-base-v2 model provides the best quality, while all-MiniLM-L6-v2 is 5 times faster and still offers good quality."
embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME", "all-MiniLM-L6-v2")
persist_directory = os.environ.get("PERSIST_DIRECTORY", "db")
target_source_chunks = int(os.environ.get('TARGET_SOURCE_CHUNKS',4))

from constants import CHROMA_SETTINGS

def main():
    # Parse the command line arguments
    args = parse_arguments()
    embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)

    db = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

    retriever = db.as_retriever(search_kwargs={"k": target_source_chunks})
    # activate/deactivate the streaming StdOut callback for LLMs
    callbacks = [] if args.mute_stream else [StreamingStdOutCallbackHandler()]

    llm = Ollama(model=model, callbacks=callbacks)

    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents= not args.hide_source)
    # Interactive questions and answers
    while True:
        query = input("\nEnter a query (type exit to quit): ")
        if query == "exit":
            break
        if query.strip() == "":
            continue

        # Get the answer from the chain
        start = time.time()
        res = qa(query)
        answer, docs = res['result'], [] if args.hide_source else res['source_documents']
        end = time.time()

        # Print the result
        print("\n\n> Question:")
        print(query)
        print(answer)

        # Print the relevant sources used for the answer
        for document in docs:
            print("\n> " + document.metadata["source"] + ":")
            print(document.page_content)

def parse_arguments():
    parser = argparse.ArgumentParser(description='privateGPT: Ask questions to your documents without an internet connection, '
                                                 'using the power of LLMs.')
    parser.add_argument("--hide-source", "-S", action='store_true',
                        help='Use this flag to disable printing of source documents used for answers.')

    parser.add_argument("--mute-stream", "-M",
                        action='store_true',
                        help='Use this flag to disable the streaming StdOut callback for LLMs.')

    return parser.parse_args()


if __name__ == "__main__":
    main()
