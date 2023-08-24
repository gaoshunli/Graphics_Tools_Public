#!/usr/bin/env python3
import subprocess
import argparse
import sys
def trace(args):
    processName=args.appname
    prePath=args.path
    print('The processName is ',processName)
    subprocess.run('adb shell chmod 777 /data/ ',shell=True)
    subprocess.run('adb shell chmod 777 /data/data/ ',shell=True)
    subprocess.run('adb shell chmod 777 /data/data/'+ processName+'/',shell=True)
    print('adb shell chmod 777 /data/data/'+ processName+'/')
    subprocess.run('adb shell settings put global enable_gpu_debug_layers 1 ',shell=True)
    subprocess.run('adb shell settings put global gpu_debug_layers_gles egltrace.so',shell=True)
    subprocess.run('adb shell settings put global gpu_debug_app '+processName,shell=True)
    appInstalledPath=subprocess.check_output('adb shell find /data/app/ -iname "*'+processName+'*"  -type d ',shell=True).decode('utf-8')
    print('The appInstalledPath is ',appInstalledPath)
    appArch=subprocess.check_output('adb shell ls '+appInstalledPath.strip()+'/lib',shell=True).decode('utf-8').strip()
    print('The appArch is ',appArch)
    libPath=appInstalledPath.strip()+'/lib/'+appArch.strip()+'/'
    print('The libPath is ',libPath)

    subprocess.run('adb shell mkdir -p /data/local/debug/gles/ ',shell=True)

    prebuiltPath=prePath
    if prebuiltPath != 'prebuilt':
        subprocess.run('adb shell setprop persist.this.is.lgsdbg.process '+processName,shell=True)
    if appArch == 'x86':
        subprocess.run('adb push '+prebuiltPath+'/x86/egltrace.so /data/local/debug/gles/ ',shell=True)
        subprocess.run('adb push '+prebuiltPath+'/x86/egltrace.so '+libPath,shell=True)
    elif appArch == 'x86_64':
        subprocess.run('adb push '+prebuiltPath+'/x86_64/egltrace.so /data/local/debug/gles/ ',shell=True)
        subprocess.run('adb push '+prebuiltPath+'/x86/egltrace.so '+libPath,shell=True)
    elif appArch == 'arm':
        subprocess.run('adb push '+prebuiltPath+'/x86/egltrace.so /data/local/debug/gles/ ',shell=True)
        subprocess.run('adb push '+prebuiltPath+'/x86/egltrace.so '+libPath,shell=True)
    elif appArch == 'arm64':
        subprocess.run('adb push '+prebuiltPath+'/x86_64/egltrace.so /data/local/debug/gles/ ',shell=True)
        subprocess.run('adb push '+prebuiltPath+'/x86_64/egltrace.so '+libPath,shell=True)
    else :
        print('start trace failed ')
    print('start trace ', processName)

def endtrace(args):
    subprocess.run('adb shell settings put global enable_gpu_debug_layers 0 ',shell=True)
    subprocess.run('adb shell settings put global gpu_debug_layers_gles null',shell=True)
    subprocess.run('adb shell settings put global gpu_debug_app null ',shell=True)
    subprocess.run('adb shell setprop persist.this.is.lgsdbg.process null',shell=True)
    print('ended all trace')
def status(args):
    statusoutput=subprocess.check_output('adb shell settings list global|grep gpu ',shell=True).decode('utf-8')
    print(statusoutput)
    statusoutput=subprocess.check_output('adb shell getprop persist.this.is.lgsdbg.process ',shell=True).decode('utf-8')
    print('persist.this.is.lgsdbg.process ',statusoutput)

parser = argparse.ArgumentParser(prog='PROG')
subparsers = parser.add_subparsers(help='sub-command help')
#add subcommand
parser_a = subparsers.add_parser('trace', help='add help')
parser_a.add_argument('--appname','-n',help='the App process name')
parser_a.add_argument('--path','-p',help='the egltrace.so path',nargs='?', default='prebuilt')
#set default command
parser_a.set_defaults(func=trace)
parser_b = subparsers.add_parser('endtrace', help='end help')
parser_b.set_defaults(func=endtrace)
parser_c = subparsers.add_parser('status', help='help')
parser_c.set_defaults(func=status)
args = parser.parse_args()
args.func(args)

