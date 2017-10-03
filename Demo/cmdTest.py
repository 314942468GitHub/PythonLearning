from cmd import *
class CmdInterface(Cmd):
    def do_say_hello(self,argc):
        print "hello! " + argc

if __name__=="__main__" :
    welcome ="welcome a simple command interface demo demo"
    CmdInterface().cmdloop(welcome)