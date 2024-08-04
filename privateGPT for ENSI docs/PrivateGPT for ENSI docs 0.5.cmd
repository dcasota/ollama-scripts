::---------------------------------------------------------------------------------------------------
::---------------------------------------------------------------------------------------------------
::---------------------------------------------------------------------------------------------------
::
::
:: Information: Dieses Skript startet PrivateGPT for ENSI docs
::
::
::---------------------------------------------------------------------------------------------------
::
::
:: Autor(en): Daniel Casota (DCA)
::::
:: Aktuell:    02.08.2024 V0.5  DCA Update
:: Änderungen: 15.05.2024 V0.1  DCA Ersterstellung
::             18.05.2024 V0.2  DCA Update
::             20.05.2024 V0.3  DCA Update
::             31.05.2024 V0.4  DCA Update
::             02.08.2024 V0.5  DCA Update
::
::---------------------------------------------------------------------------------------------------
::
:: Voraussetzungen: Windows 11 mit Windows Subsystem for Linux und C:\My Web Sites\ENSI
::
:: Aufruf durch: manuell im Kommandozeilenkonsolenfenster DOS
::
:: Inputvariablen: (keine)
:: CmdLine-Parameter (keine)
::
:: Outputvariablen: (keine)
:: Rückgabewert: (keine)
::---------------------------------------------------------------------------------------------------
::
:: Plattform: Getestet auf Windows 11
::
::---------------------------------------------------------------------------------------------------
::---------------------------------------------------------------------------------------------------
::---------------------------------------------------------------------------------------------------

@echo off
title "PrivateGPT for ENSI docs Starter v0.5"
echo PrivateGPT for ENSI docs Starter v0.5
echo.

net session >NUL 2>&1
    if %errorLevel% == 0 (
       echo Script has been started with administrative rights.
    ) else (
       echo Failure: Current permissions inadequate. Run the script with administrative privileges.
       pause >nul
       goto exit
    )

if not exist "C:\My Web Sites\ENSI\nul" (
      echo ENSI docs found.
   ) else (
       echo Failure: ENSI docs not found. Please check installation.
       pause >nul
       goto exit
   )

powershell -Command "$env:WSL_UTF8 = 1; wsl --list | select-string -Pattern Ph5" | find /I "Ph5" >NUL 2>&1
if errorlevel 1 (
       echo Failure: Windows Subsystem for Linux installation with Helper Distribution Photon OS is not available. Please check installation.
       pause >nul
       goto exit
   ) else (
      echo Windows Subsystem for Linux installation with Helper Distribution Photon OS found.
   )


:: Starting directly start.py from a long directory path does not work. Hence copy the file to %public%.
set source=c:\Users\dcaso\OneDrive\Pers�nlich\Hobbyprojekte\PrivateGPT for ENSI docs\PrivateGPT for ENSI docs\start.py
set destination=%PUBLIC%\start.py
set destinationLinux=/mnt/%destination:\=/%
set destinationLinux=%destinationLinux::=%
set destinationLinux=%destinationLinux:/C/=/c/%
COPY /V /Y "%source%" "%destination%" 1>NUL 2>&1
wsl --distribution Ph5 -u dcaso -e /bin/bash -c "python %destinationLinux%"
del %destination%

pause
:exit



