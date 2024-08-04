#!/usr/bin/env python3


#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#
#
# Information: Menu for various tasks
#
#
#---------------------------------------------------------------------------------------------------
#
#
# Autor(en): Daniel Casota (DCA)
#
# Aktuell:    02.08.2024 V0.51 DCA Update to Ollama 0.3.2
# Änderungen: 29.05.2024 V0.1  DCA header information added
#             02.06.2024 V0.2  DCA precleanup of directories added
#             05.06.2024 V0.3  DCA Extended menu added
#             07.06.2024 V0.4  DCA Minor updates
#             07.06.2024 V0.5  DCA Update to 0.1.43, docker-compose integrated
#             02.08.2024 V0.51 DCA Update to Ollama 0.3.3. be aware of hardocded directory paths in ScriptBlock0 and ScriptBlock1.
#
#---------------------------------------------------------------------------------------------------
#
# Voraussetzungen: Windows 11 mit Windows Subsystem for Linux und C:\My Web Sites\ENSI
#
# Aufruf durch: PrivateGPT for ENSI docs 0.5.cmd
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

def StartPrivateGPT():
    print("'Start PrivateGPT' selected.")
    with open("./run.sh", 'w+') as file:
       file.writelines(ScriptBlock0)
       file.close() 
    subprocess.run("sudo chmod a+x ./run.sh", shell=True,executable='/bin/bash')    
    subprocess.run('./run.sh', shell=True,executable='/bin/bash')    
    

def ShowImportStatistics():
    print("'Show import statistics' selected.")
    home_path=os.environ['HOME']   
    if os.path.exists(f"{home_path}/ollama/examples/langchain-python-rag-privategpt/logfile.txt") == True:
        subprocess.run('cd $HOME/ollama/examples/langchain-python-rag-privategpt; echo "All files: " `find /mnt/c/My\ Web\ Sites/ENSI -type f | wc -l`', shell=True,executable='/bin/bash')
        subprocess.run('cd $HOME/ollama/examples/langchain-python-rag-privategpt; echo "   Pdf files: " `find /mnt/c/My\ Web\ Sites/ENSI -name *.pdf -type f | wc -l`', shell=True,executable='/bin/bash')
        subprocess.run('cd $HOME/ollama/examples/langchain-python-rag-privategpt; echo "   Html files: " `find /mnt/c/My\ Web\ Sites/ENSI -name *.html -type f | wc -l`', shell=True,executable='/bin/bash')
        subprocess.run('cd $HOME/ollama/examples/langchain-python-rag-privategpt; echo "Issue files: "', shell=True,executable='/bin/bash')        
        subprocess.run('cd $HOME/ollama/examples/langchain-python-rag-privategpt; echo "   Empty (zero) files: " `cat logfile.txt | grep Empty | wc -l`', shell=True,executable='/bin/bash')
        subprocess.run('cd $HOME/ollama/examples/langchain-python-rag-privategpt; echo "   Corrupt files: " `cat logfile.txt | grep Corrupt | wc -l`', shell=True,executable='/bin/bash')
        subprocess.run('cd $HOME/ollama/examples/langchain-python-rag-privategpt; echo "   Unsupported files: " `cat logfile.txt | grep Unsupported | wc -l`', shell=True,executable='/bin/bash')
    else:
        print("No import statistic available.")   
    
def UpdateModels():
    print("'Update models' selected.")
    with open("./UpdateModels.sh", 'w+') as file:
       file.writelines(ScriptBlock3)
       file.close() 
    subprocess.run("sudo chmod a+x ./UpdateModels.sh", shell=True,executable='/bin/bash')
    import requests

    timeout = 1

    try:
        requests.head("https://ntp.org", timeout=timeout)
        # Do something
        subprocess.run('./UpdateModels.sh', shell=True,executable='/bin/bash') 
    except requests.ConnectionError:
        # Do something
        print("The internet connection is down. Please check connectivity.")
    

def ReimportENSIdocuments():
    print("'Reimport ENSI documents' selected.")
    with open("./ENSIdocsimport.sh", 'w+') as file:
       file.writelines(ScriptBlock1)
       file.close() 
    subprocess.run("sudo chmod a+x ./ENSIdocsimport.sh", shell=True,executable='/bin/bash')    
    subprocess.run('./ENSIdocsimport.sh', shell=True,executable='/bin/bash')

def Shell():
    print("'Shell' selected.")
    subprocess.run('/bin/bash --login', shell=True,executable='/bin/bash')

def Reinstall():
    print("'Reinstall' selected.")
    with open("./reinstall.sh", 'w+') as file:
       file.writelines(ScriptBlock2)
       file.close()
    subprocess.run("sudo chmod a+x ./reinstall.sh", shell=True,executable='/bin/bash')     

    import requests

    timeout = 1

    try:
        requests.head("https://ntp.org", timeout=timeout)
        # Do something
        subprocess.run("./reinstall.sh", shell=True,executable='/bin/bash')
    except requests.ConnectionError:
        # Do something
        print("The internet connection is down. Please check connectivity.")


print ("PrivateGPT for ENSI docs v0.5")
import os
import sys
import subprocess

if not sys.warnoptions:
   import warnings
   warnings.simplefilter("ignore")
   with warnings.catch_warnings():
        warnings.filterwarnings("ignore",category=DeprecationWarning)
        warnings.filterwarnings("ignore",category=FutureWarning)   

ScriptBlock0=r'''
#!/bin/bash
cd $HOME/ollama/examples/langchain-python-rag-privategpt

export PERSIST_DIRECTORY=db
export SOURCE_DIRECTORY=/mnt/c/'My Web Sites/ENSI'

cp /mnt/c/Users/dcaso/OneDrive/Persönlich/Hobbyprojekte/'PrivateGPT for ENSI docs'/'PrivateGPT for ENSI docs'/ingest.py ./ingest.py
cp /mnt/c/Users/dcaso/OneDrive/Persönlich/Hobbyprojekte/'PrivateGPT for ENSI docs'/'PrivateGPT for ENSI docs'/privateGPT.py ./privateGPT.py

export ID=`sudo ps -ef | grep "ollama serve" -m 1 | awk '{ print $2 }'`
if ! [ -n "$ID" ]; then
    ollama serve &
fi

python3 ./privateGPT.py --mute-stream --hide-source
''' 
 
ScriptBlock1=r'''
#!/bin/bash
cd $HOME/ollama/examples/langchain-python-rag-privategpt

export PERSIST_DIRECTORY=db
export SOURCE_DIRECTORY=/mnt/c/'My Web Sites/ENSI'

cp /mnt/c/Users/dcaso/OneDrive/Persönlich/Hobbyprojekte/'PrivateGPT for ENSI docs'/'PrivateGPT for ENSI docs'/ingest.py ./ingest.py
cp /mnt/c/Users/dcaso/OneDrive/Persönlich/Hobbyprojekte/'PrivateGPT for ENSI docs'/'PrivateGPT for ENSI docs'/privateGPT.py ./privateGPT.py

python3 ./ingest.py    
'''   
   
ScriptBlock3=r'''
#!/bin/bash
ollama list
# https://github.com/ollama/ollama/issues/1890#issuecomment-1885381713
ollama list | tail -n +2 | awk '{print $1}' | while read -r model; do
  ollama pull $model
done
ollama list 
'''

ScriptBlock2=r'''
#!/bin/sh

cd $HOME

# Uninstall openlit subcomponents
export ID=`sudo docker container list | grep clickhouse/clickhouse-server | awk '{ print $1 }'`
if [ -n "$ID" ]; then
    echo Uninstalling openlit components ...
    sudo docker container rm $ID --force
fi
export ID=`sudo docker container list | grep ghcr.io/openlit/openlit | awk '{ print $1 }'`
if [ -n "$ID" ]; then
    sudo docker container rm $ID --force
fi
export ID=`sudo docker container list | grep otel/opentelemetry-collector-contrib | awk '{ print $1 }'`
if [ -n "$ID" ]; then
    sudo docker container rm $ID --force
fi
if [ -d "./openlit" ]; then
    sudo rm -r -f ./openlit
fi

# Uninstall ntlk
if [ -d "./nltk_data" ]; then
    echo Uninstalling nltk_data ...
    sudo rm -r -f ./nltk_data
fi

# uninstall ollama
export ID=`sudo ps -ef | grep "ollama serve" -m 1 | awk '{ print $2 }'`
if [ -n "$ID" ]; then
    echo Finishing Ollama process ...
    sudo sudo kill -9 $ID
fi
if [ -d "./ollama" ]; then
    echo Removing existing Ollama installation ...
    sudo rm -r -f ./ollama
    sudo rm -r -f ./.ollama    
    sudo rm -r -f /usr/share/ollama    
fi

# configure Swiss German
sudo tdnf install -y glibc-lang kbd glibc-i18n
echo de_CH ISO-8859-1 | sudo tee /etc/locale-gen.conf
echo de_CH.UTF-8 UTF-8 | sudo tee -a /etc/locale-gen.conf
sudo locale-gen.sh
sudo localectl set-locale LANG="de_CH.UTF-8" LC_CTYPE="de_CH.UTF-8"
sudo localectl set-keymap de_CH-latin1
sudo loadkeys de_CH-latin1

# Configure python environment
sudo tdnf install -y python3-pip python3-devel git
pip3 install --upgrade pip

DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}
mkdir -p $DOCKER_CONFIG/cli-plugins
curl -SL https://github.com/docker/compose/releases/download/v2.27.1/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose
sudo chmod a+x $DOCKER_CONFIG/cli-plugins/docker-compose

# Own specific privateGPT python scripts
# --------------------------------------
cd $HOME

# Install with latest release
export RELEASE=0.3.3
echo Installing Ollama Release $RELEASE ...
curl -fsSL https://ollama.com/install.sh | sed "s#https://ollama.com/download#https://github.com/ollama/ollama/releases/download/v\$RELEASE#" | sh
ollama serve &

echo Installing Ollama Release $RELEASE Source ...
git clone -b v$RELEASE https://github.com/ollama/ollama.git

# Modifications for custom ingest-py and privategpt.py
cd ollama/examples/langchain-python-rag-privategpt
# python3 -m venv .venv
# source .venv/bin/activate
export PATH=$PATH:$HOME/.local/bin
pip3 install -r requirements.txt
# fix issue in Ollama 0.3.3
pip3 install torch --upgrade

# Create the `source_documents` directory (not needed anymore, but still here for documentation purposes)
mkdir -p $HOME/ollama/examples/langchain-python-rag-privategpt/source_documents
# Patch ingest.py and privateGPT.py
cp /mnt/c/Users/dcaso/OneDrive/Persönlich/Hobbyprojekte/'PrivateGPT for ENSI docs'/'PrivateGPT for ENSI docs'/ingest.py ./ingest.py
cp /mnt/c/Users/dcaso/OneDrive/Persönlich/Hobbyprojekte/'PrivateGPT for ENSI docs'/'PrivateGPT for ENSI docs'/privateGPT.py ./privateGPT.py

# fix issue 'Error with downloaded zip file'
# ingest.py prerequisite for attempts to load tokenizers/punkt/PY3/english.pickle
pip3 install nltk==3.8.1
# fix issue zipfile.BadZipFile: File is not a zip file, see https://github.com/zylon-ai/private-gpt/issues/345
python -m nltk.downloader all

# fix issue (in Ollama 0.3.3, too) : 'Cannot submit more than 5,461 embeddings at once.'
pip3 install chromadb==0.5.0

# fix issue (in Ollama 0.3.3, too) : 'ValidationError: 1 validation error for LLMChain'
#                                    llm
#                                    Can't instantiate abstract class BaseLanguageModel with abstract methods agenerate_prompt, apredict, apredict_messages, generate_prompt, invoke, predict, predict_messages (type=type_error)'
pip3 install langchain --upgrade

# Chat model
ollama pull llama3.1
'''


MenuListe = ["Start PrivateGPT", "Import/Update ENSI documents", "Show import statistics", "Settings", "Exit"]
user_input = ''
input_message = "Choose an option:\n"

for index, item in enumerate(MenuListe):
    input_message += f'{index+1}) {item}\n'
input_message += 'Choice: '

while True:
    while True:
        user_input = input(input_message)
        try:
            user_input = int(user_input)
            if 1 <= user_input <= index+1:
                break
            else:
                print(f"Invalid input. Please choose an option from menu between 1 und {index+1}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    match (MenuListe[int(user_input)-1]):
        case "Start PrivateGPT":
            StartPrivateGPT()          
        case "Import/Update ENSI documents":
            ReimportENSIdocuments()
        case "Show import statistics":
            ShowImportStatistics()
        case "Settings":
            MenuListe2 = ["Change default output language", "Update LLMs", "Reinstall", "Shell", "back"]
            user_input2 = ''
            input_message2 = "Choose an option:\n"

            for index2, item2 in enumerate(MenuListe2):
                input_message2 += f'{index2+1}) {item2}\n'
            input_message2 += 'Choice: '

            while True:
                while True:
                    user_input2 = input(input_message2)
                    try:
                        user_input2 = int(user_input2)
                        if 1 <= user_input2 <= index2+1:
                            break
                        else:
                            print(f"Invalid input. Please choose an option from menu between 1 und {index2+1}.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                match (MenuListe2[int(user_input2)-1]):
                    case "Change default output language":
                        print("Not implemented yet.")
                    case "Update LLMs":
                        UpdateModels()
                    case "Reinstall":
                        package="requests"
                        try:
                            import pip
                            try:
                                __import__(package)
                                Reinstall()
                            except:
                                pip.main(['install', '--user', package])
                                print(f"Pip package installed. Close this window and restart PrivateGPT for ENSI docs.")
                                break
                        except ImportError:
                            subprocess.run("sudo tdnf install -y python3-pip python3-devel git", shell=True,executable='/bin/bash')
                            print(f"Python packages installed. Close this window and restart PrivateGPT for ENSI docs.")
                            break                       
                    case "Shell":
                        Shell()
                    case "back":            
                        break
        case "Exit":            
            sys.exit()
