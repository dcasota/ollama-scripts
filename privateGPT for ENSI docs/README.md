PrivateGPT for ENSI docs
-

The Swiss Federal Nuclear Safety Inspectorate (ENSI) is the national regulatory body responsible for overseeing the safety and security of nuclear facilities in Switzerland. Established on January 1, 2009, ENSI took over from its predecessor, HSK1.

ENSI’s responsibilities include:
- Supervision of Nuclear Facilities: This covers the entire lifecycle of nuclear facilities, from initial planning and operation to decommissioning and waste disposal.
- Safety and Security: Ensuring the safety of staff, the public, and the environment from radiation, sabotage, and terrorism.
- Transport of Radioactive Materials: Overseeing the safe transport of radioactive materials to and from nuclear facilities.
Research and International Collaboration: Supporting research into nuclear safety and participating in over 70 international commissions and specialist groups.
ENSI operates independently under public law and is supervised by the ENSI Board, which reports directly to the Swiss Federal Council1. The organization is headquartered in Brugg, in the canton of Aargau.

On their website, ENSI published a large amount of documents. PrivateGPT for ENSI docs is a tiny side project to make run GPT for ENSI docs.

Prerequisites:
- Windows 11 with Windows Subsystem for Linux
- Go through the installation steps in [PrivateGPT on VMware Photon OS on WSL2](https://github.com/dcasota/ollama-scripts/wiki/PrivateGPT-on-Photon-OS-on-WSL2)
- Stored ENSI docs in a directory `C:\My Web Sites\ENSI`. Download and configure [HTTrack Copier](https://www.httrack.com/) to download the website content.  
- Copy the files into a local directory.  
  In `PrivateGPT for ENSI docs 0.5.cmd`, modify source variable.  
  In `start.py`, modify alls entries with  
    `cp /mnt/c/Users/dcaso/OneDrive/Persönlich/Hobbyprojekte/'PrivateGPT for ENSI docs'/'PrivateGPT for ENSI docs'/ingest.py ./ingest.py`  
    `cp /mnt/c/Users/dcaso/OneDrive/Persönlich/Hobbyprojekte/'PrivateGPT for ENSI docs'/'PrivateGPT for ENSI docs'/privateGPT.py ./privateGPT.py`
  - Start `PrivateGPT for ENSI docs 0.5.cmd` as Administrator. The scripts starts a menu dialog.
     - Run 'Import/Update ENSI documents'
     - Run 'show import statistics'
     - After those steps, run 'Start PrivateGPT'.

## Start
Start `PrivateGPT for ENSI docs 0.5.cmd` as Administrator.

![image](https://github.com/user-attachments/assets/d33ceeb9-a488-4214-9cba-809973faa76e)

## (Re-)Installation
In the menu, press "4" for Settings, and then "3" for (re-)install.

![image](https://github.com/user-attachments/assets/c2c99d48-3250-4ab3-815a-90a5db76aefb)

## Import/Update ENSI documents
After the installation, press "5"(back) and then "2" to Import/Update ENSI documents. Be aware that this step may take an hour(!).

## Statistics information
Have a look to the statistics information, press "3".

![image](https://github.com/user-attachments/assets/609f312c-20db-4584-8547-8e43c3b9844b)

Mass of corrupt files may occur as HTTRack Copier detects if a webpage as been moved or wasn't downloaded correctly. It stores the html information in a file ending with pdf.

Here an example:
```
<HTML>
<!-- Created by HTTrack Website Copier/3.49-2 [XR&CO'2014] -->

<!-- Mirrored from www.wenra.org/media/filer_public/2013/08/29/wenra_media_release_on_flaw_indications.pdf by HTTrack Website Copier/3.x [XR&CO'2014], Thu, 30 May 2024 06:52:02 GMT -->
<HEAD>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html;charset=UTF-8"><META HTTP-EQUIV="Refresh" CONTENT="0; URL=https://serp.co/reviews/"><TITLE>Page has moved</TITLE>
</HEAD>
<BODY>
<A HREF="https://serp.co/reviews/"><h3>Click here...</h3></A>
</BODY>
<!-- Created by HTTrack Website Copier/3.49-2 [XR&CO'2014] -->

<!-- Mirrored from www.wenra.org/media/filer_public/2013/08/29/wenra_media_release_on_flaw_indications.pdf by HTTrack Website Copier/3.x [XR&CO'2014], Thu, 30 May 2024 06:52:02 GMT -->
</HTML>
```

Data quality is important for PrivateGPT. Hence filter all unnecessary files out before proceeding.

## Update LLMs
With option "2" you can update LLMs.

![image](https://github.com/user-attachments/assets/412c9635-9471-4797-8c62-c0350dc179a9)

## Start privateGPT
Press "1" to start privateGPT.

![image](https://github.com/user-attachments/assets/96720456-4b12-48b4-87dc-6d037cb2262a)
