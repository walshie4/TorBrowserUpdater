#!/usr/bin/env python
#Written by: Adam Walsh
#Written on 4/2/14

from BeautifulSoup import BeautifulSoup
import requests
import sys
import os
import platform

class TBBUpdater:
    currentVersion = None
    installedVersion = None
    lang = None

    def detectLocalInstall(self):
        print("Detecting local install...")
#look in default location to find install, if not found ask user if a custom
#location install exists

    def getInstalledVersion(self, path):    #The looking for an installed version may
        if path == None:                    #be thrown out for additional security to
            print ("No local install found.")#prevent accidental use of a tampered
        print("Gathering version info for local install")#version of TBB on your local
                                                         #machine

    def getCurrentVersion(self):
        res = requests.get("https://www.torproject.org/dist/torbrowser/")
        soup = BeautifulSoup(res.text)
        versions = list()
        versionsNext = False
        for link in soup.findAll('a'):
            name = link.get('href')
            if versionsNext:
                versions.append(name)
            elif name == '/dist/':
                versionsNext = True
        mostRecent = versions[0]
        print "Current available versions are:"
        index = 0
        for version in versions:                            #This choice system may
            print str(index) + " ~ " + version              #be replaced with an
            index += 1                                      #automatic choice to use
                                                            #the newest available
        selection = int(raw_input("Please select which build you would like to run: "))
        print("Selected version: " + versions[selection])
        self.currentVersion = versions[selection]

    def upToDate(self):
        if self.currentVersion == None or self.installedVersion == None:
            print("Either current version or installed version variable is null.\n"
                    + "This means either a local install has not been found or\n"
                    + "checks are being made before getting both the current and\n"
                    + "installed version numbers of the TBB.")
        elif self.currentVersion == self.installedVersion:
            return True
        else:
            return False

    def getLanguage(self):
        supported = {'Arabic' : 'ar',
                     'German' : 'de',
               'English (US)' : 'en-US',
        'Spanish (Castilian)' : 'es-ES',
                    'Farsi'   : 'fa',
                    'French'  : 'fr',
                    'Italian' : 'it',
                    'Korean'  : 'ko',
                    'Dutch'   : 'nl',
                    'Polish'  : 'pl',
      'Portuguese (Portugal)' : 'pt-Pt',
                   'Russian'  : 'ru',
                 'Vietnamese' : 'vi',
                'Chinese (S)' : 'zh-CN'}
        index = 0
        for lang in supported:
            print str(index) + ' ~ ' + lang
            index += 1
        selected = int(raw_input("Please select which language pack you "
            + "would like to use: "))
        keys = supported.keys()
        self.lang = supported[keys[selected]]
        print self.lang

    def getOS(self):
        name = platform.system().lower()
        if name == 'windows':
            return 'win'
        elif name == 'darwin':
            return 'mac'
        elif name.lower().find('linux') > -1:
            return 'linux'
        else:
            return None

    def getArch(self):#A bug exists that affects this (http://bugs.python.org/issue7860)
        archs = {'AMD64' : 64, 'x86_64': 64, 'i386': 32, 'x86': 32}
        machine = platform.machine()
        return archs.get(machine, None)

if __name__=="__main__":
    updater = TBBUpdater()
    updater.getCurrentVersion()
    print updater.getOS()
    print updater.getArch()
    if updater.upToDate():
        print("Installed version is up-to-date")
        #no need to update, launch bundle
    #else:
        #updater.update()
    #updater.launchTBB()
    updater.getLanguage()