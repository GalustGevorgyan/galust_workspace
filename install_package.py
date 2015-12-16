#!/usr/bin/python

import os
import sys
import platform
import argparse
import webbrowser
import subprocess


def determination_of_operating_systems():
    current_os = platform.system()
    operation_sysytem_list = ['Linux','Darwin']
    if not (current_os in operation_sysytem_list):
        print 'Unsupported platform' +  determination_of_operating_systems
        sys.exit()
    return current_os

##INSTALL JYTHON
def jython_exist():
    try:
        subprocess.check_output(['which,' 'jython'])
        return True
    except subprocess.CalledProcessError, e:
        return False
    except OSError, e:
        return False

def install_jython(current_os):
    current_os = determination_of_operating_systems()
    home_directory = os.environ['HOME']
    parent_directory = os.getcwd()
    if (jython_exist()):
        print "Jython is already installed on the platform."
        return
    install_jython = ('wget https://repo1.maven.org/maven2/org/python/jython-installer/2.7.0/jython-installer-2.7.0.jar')
    os.system(install_jython)
    run_jython_jar = 'java -jar jython-installer-2.7.0.jar -s -d '+parent_directory+'/jython2.7.0'
    os.system(run_jython_jar)
    export_path = 'export jythonHome='+parent_directory+'/jython2.7.0'
    print "MY EXPORT PATH + " +export_path
    os.system(export_path)
    export_jython_home = 'export PATH=$jythonHome/bin:$PATH'
    print "MY EXPORT JYTHON PATH + " +export_jython_home
    os.system(export_jython_home)
    jython_version = 'jython --version'
    os.system(jython_version)

##Install robot
def install_robot(current_os):
    install_robot = 'git clone https://github.com/robotframework/robotframework.git'
    print install_robot
    os.system(install_robot)
    user = os.getenv('USER')
    chown_woking_copy= 'sudo chown   -R '+user+' robotframework'
    os.system(chown_woking_copy)
    parent_directory_ = os.getcwd()
    cd_working_copy= parent_directory_+'/robotframework'
    os.chdir(cd_working_copy)
    build_setup = 'jython setup.py build'
    os.system(build_setup)
    install_setup = 'jython setup.py install'
    os.system(install_setup)

## Cucumber instalation 
def install_cucumber_on_mac():
    install_cucumber = 'sudo gem install cucumber'
    os.system(install_cucumber)

def install_cucumber_on_linux():
    install_cucumber = 'sudo apt-get install cucumber'
    os.system(install_cucumber)

def cucumber_exist():
    try: 
        subprocess.check_output(['which', 'cucumber'])
        return True 
    except subprocess.CalledProcessError, e:
        return False
    
def install_cucumber(os):
    current_os = determination_of_operating_systems()
    if (cucumber_exist):
        print "Cucumber is already installed on the platform."
        return 
    if current_os == 'Darwin':
        install_cucumber_on_mac()
    elif current_os == 'Linux':
        install_cucumber_on_linux

# Argument parser defination
def arg_parser():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-r', '--robot',
            action='store_true',
            help ='Run script withouth specific tag name.')
    arg_parser.add_argument('-c', '--cucumber',
            action='store_true',
            help='Run script withouth specific tag name.')
    args=arg_parser.parse_args()
    return args

# Opened install directory
def open_install_directory():
    install_directory = 'install_automation'
    parent_directory = os.getcwd()
    if not os.path.exists(install_directory):
        os.makedirs(install_directory)
    go_install_dir = parent_directory+'/'+install_directory+''
    os.chdir(go_install_dir)

#Run Script
def run():
    current_os = determination_of_operating_systems()
    args = arg_parser()
    open_install_directory()
    print "Running on " + current_os
    if args.robot:
        print "Intsalling Robot an Jython in current OS ..."
        install_jython(current_os)
        install_robot(current_os)
    if args.cucumber:
        print "Intsalling Cucumber in current OS ..."
        install_cucumber(current_os)

if __name__ == '__main__':
    run()
