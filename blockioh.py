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
        print(dev)
    def get_path(self):
        global path
        return path
        print(path)

    def mount(self):
        output = self.system('mount -v ' + self.get_dev() + " " + self.get_path() )
        print(output)
        
        if "mount: mount point " + self.get_path() +" does not exist" in output: return 1
        elif output == "mount: only root can do that": return 2           
        elif 'mounted' in output: return 0
        else: 3
    def umount(self):
        output = self.system('umount -v '+  self.get_dev())
        print(output)
        if "mount: mount point " + self.get_path() + "does not exist"  in output: return 1
        elif "mount: only root can do that" in output: return 2
        elif "mounted" in output: return 0
        else: return 3
