#!/usr/bin/env python3

#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#
#
# Information: modified ingest.py from langchain-python-rag-privategpt
#
#
#---------------------------------------------------------------------------------------------------
#
#
# Autor(en): Daniel Casota (DCA)
#
# Aktuell:    07.06.2024 V0.4  DCA Recreation
# Änderungen:    05.2024 V0.1  DCA Copy from ingest.py from langchain-python-rag-privategpt
#             02.06.2024 V0.2  DCA header information added
#             03.06.2024 V0.3  DCA rewriting process_documents()
#             07.06.2024 V0.4  DCA Recreation from https://github.com/ollama/ollama/pull/4852
#                                  - Header re-added
#                                  - recreation of load_single_document() with protocolfile
#                                  - Simplified version of does_vectorstore_exist() re-added
#                                  - EMBEDDINGS_MODEL_NAME=sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
#                                  - replacement to 'from langchain_community.document_loaders'
#                                  - replacement to 'from langchain_community.vectorstores import Chroma'
#                                  - replacement to 'from langchain_community.embeddings'
#                                  - replacement to 'from langchain_huggingface'
#             04.08.2024 V0.4  DCA LLM replacement with all-MiniLM-L6-v2
#
#
#---------------------------------------------------------------------------------------------------
#
# Voraussetzungen: Windows 11 mit Windows Subsystem for Linux und C:\My Web Sites\ENSI
#
# Aufruf durch: PrivateGPT for ENSI docs 0.3.cmd
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

import os
import glob
from typing import List
from multiprocessing import Pool
from tqdm import tqdm

from langchain_community.document_loaders import (
    CSVLoader,
    EverNoteLoader,
    PyMuPDFLoader,
    TextLoader,
    UnstructuredEmailLoader,
    UnstructuredEPubLoader,
    UnstructuredHTMLLoader,
    UnstructuredMarkdownLoader,
    UnstructuredODTLoader,
    UnstructuredPowerPointLoader,
    UnstructuredWordDocumentLoader,
)

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.docstore.document import Document
from constants import CHROMA_SETTINGS


# Load environment variables
persist_directory = os.environ.get('PERSIST_DIRECTORY', 'db')
source_directory = os.environ.get('SOURCE_DIRECTORY', 'source_documents')
embeddings_model_name = os.environ.get('EMBEDDINGS_MODEL_NAME', 'all-MiniLM-L6-v2')
chunk_size = 500
chunk_overlap = 50

# Custom document loaders
class MyElmLoader(UnstructuredEmailLoader):
    """Wrapper to fallback to text/plain when default does not work"""

    def load(self) -> List[Document]:
        """Wrapper adding fallback for elm without html"""
        try:
            try:
                doc = UnstructuredEmailLoader.load(self)
            except ValueError as e:
                if 'text/html content not found in email' in str(e):
                    # Try plain text
                    self.unstructured_kwargs["content_source"]="text/plain"
                    doc = UnstructuredEmailLoader.load(self)
                else:
                    raise
        except Exception as e:
            # Add file_path to exception message
            raise type(e)(f"{self.file_path}: {e}") from e

        return doc


# Map file extensions to document loaders and their arguments
LOADER_MAPPING = {
    ".csv": (CSVLoader, {}),
    # ".docx": (Docx2txtLoader, {}),
    ".doc": (UnstructuredWordDocumentLoader, {}),
    ".docx": (UnstructuredWordDocumentLoader, {}),
    ".enex": (EverNoteLoader, {}),
    ".eml": (MyElmLoader, {}),
    ".epub": (UnstructuredEPubLoader, {}),
    ".html": (UnstructuredHTMLLoader, {}),
    ".md": (UnstructuredMarkdownLoader, {}),
    ".odt": (UnstructuredODTLoader, {}),
    ".pdf": (PyMuPDFLoader, {}),
    ".ppt": (UnstructuredPowerPointLoader, {}),
    ".pptx": (UnstructuredPowerPointLoader, {}),
    ".txt": (TextLoader, {"encoding": "utf8"}),
    # Add more mappings for other file extensions and loaders as needed
}


def load_single_document(file_path: str) -> List[Document]:
    from datetime import datetime
    import time
    dir_path = os.path.dirname(os.path.realpath(__file__)) 
    protocolfile = os.path.join(dir_path, "logfile.txt")
    
    # amount of zero byte files in Microsoft batch: dir *.pdf /s | find /I ".pdf" | find /I " 0 " | find /C " 0 "
    if os.path.getsize(file_path) != 0:
        filename, ext = os.path.splitext(file_path)
        if ext in LOADER_MAPPING:
            loader_class, loader_args = LOADER_MAPPING[ext]
            try:      
                loader = loader_class(file_path, **loader_args)
                if loader:
                    document = loader.load()
                    IssueID=0
                    if ext == ".html" :
                        for item in document:
                            for i in item:
                                for j in i:
                                    if "Error 404" in j:
                                        IssueID=1
                                        break
                                    if "File has moved" in j:
                                        IssueID=2
                                        break                                        
                    if IssueID == 0 :
                        return document
                    if IssueID == 1 :
                        file = open(protocolfile, "a") 
                        sttime = datetime.now().strftime('%Y%m%d_%H:%M:%S - ')
                        file.write(sttime + "Error 404 found in file "+file_path+"! Ignoring it.\n")
                        file.close()
                    if IssueID == 2 :
                        file = open(protocolfile, "a") 
                        sttime = datetime.now().strftime('%Y%m%d_%H:%M:%S - ')
                        file.write(sttime + "'Page has moved' found in file "+file_path+"! Ignoring it.\n")
                        file.close()
            except Exception as e:
                file = open(protocolfile, "a")
                sttime = datetime.now().strftime('%Y%m%d_%H:%M:%S - ')
                file.write(sttime + "Corrupt file "+file_path+" detected! Ignoring it.\n")
                file.close()
        else:
            file = open(protocolfile, "a")
            sttime = datetime.now().strftime('%Y%m%d_%H:%M:%S - ')
            file.write(sttime + "Unsupported file extension "+ext+"'! Ignoring it.\n") 
            file.close()            
    else:
        file = open(protocolfile, "a")
        sttime = datetime.now().strftime('%Y%m%d_%H:%M:%S - ')
        file.write(sttime + "Empty file "+file_path+" detected! Ignoring it.\n")
        file.close() 


def load_documents(source_dir: str, ignored_files: List[str] = []) -> List[Document]:
    """
    Loads all documents from the source documents directory, ignoring specified files
    """
    all_files = []
    all_files.extend(glob.glob(os.path.join(source_dir, f"**/*.*"), recursive=True))
    filtered_files = [file_path for file_path in all_files if file_path not in ignored_files]

    with Pool(processes=os.cpu_count()) as pool:
        results = []
        with tqdm(total=len(filtered_files), desc='Loading new documents', ncols=80) as pbar:
            for i, docs in enumerate(pool.imap_unordered(load_single_document, filtered_files)):
                if docs:
                    results.extend(docs)
                pbar.update()

    return results

def process_documents(ignored_files: List[str] = []) -> List[Document]:
    """
    Load documents and split in chunks
    """
    print(f"Loading documents from {source_directory}")
    documents = load_documents(source_directory, ignored_files)
    if not documents:
        print("No new documents to load")
        exit(0)

    dir_path = os.path.dirname(os.path.realpath(__file__)) 
    documentsfile = os.path.join(dir_path, "documents.txt")
    file = open(documentsfile, "a")
    for item in documents:
        file.write(f"{item}\n")
    file.close()  
    
    print(f"Loaded {len(documents)} new documents from {source_directory}")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    texts = text_splitter.split_documents(documents)
    
    dir_path = os.path.dirname(os.path.realpath(__file__)) 
    textsfile = os.path.join(dir_path, "texts.txt")
    file = open(textsfile, "a")
    for item in texts:
        file.write(f"{item}\n")
    file.close()      
    
    print(f"Split into {len(texts)} chunks of text (max. {chunk_size} tokens each)")
    return texts

def does_vectorstore_exist(persist_directory: str) -> bool:
    """
    Checks if vectorstore exists
    """
    if os.path.exists(os.path.join(persist_directory, 'chroma.sqlite3')):
        return True
    else:
        return False

def main():
    # Create embeddings
    embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)

    if does_vectorstore_exist(persist_directory):
        # Update and store locally vectorstore
        print(f"Appending to existing vectorstore at {persist_directory}")
        db = Chroma(persist_directory=persist_directory, embedding_function=embeddings, client_settings=CHROMA_SETTINGS)
        collection = db.get()
        texts = process_documents([metadata['source'] for metadata in collection['metadatas']])
        print(f"Creating embeddings. May take some minutes...")
        db.add_documents(texts)
    else:
        # Create and store locally vectorstore
        print("Creating new vectorstore")
        texts = process_documents()
        print(f"Creating embeddings. May take some minutes...")
        db = Chroma.from_documents(texts, embeddings, persist_directory=persist_directory)
    db.persist()
    db = None

    print(f"Ingestion complete! You can now run privateGPT.py to query your documents")


if __name__ == "__main__":
    main()
