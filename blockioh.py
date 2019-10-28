class device():
    def system(self, command):
        from os import system
        print(command)
        system(command + " > .log.temp")
        log = open('.log.temp', 'r')
        logContents = log.read()
        log.close
        print(logContents)
        system('rm  .log.temp')
        return logContents
    def __init__(self, de,pa):
        global dev
        global path
        dev = de
        path = pa

    def get_dev(self):
        global dev
        return dev
    def get_path(self):
        global path
        return path

    def mount(self):
        output = self.system('mount -v ' + self.get_dev() + " " + self.get_path() )
        
        if "does not exist" in output: print(1) ;return 1
        elif output == "mount: only root can do that": print(1) ; return 2           
        elif 'mounted' in output: print(0);return 0
        else: print(3);return 3
    def umount(self):
        output = self.system('umount -v '+  self.get_dev())
        if "mount: mount point " + self.get_path() + "does not exist"  in output: return 1
        elif "mount: only root can do that" in output: return 2
        elif "mounted" in output: return 0
        else: return 3
    def write(self):
        output = system('dd if=' +self.get_path() + ' of=' + self.get_dev() )
    def read(self):
        output = system('dd if=' + self.get_dev() + ' of=' + self.get_path())


