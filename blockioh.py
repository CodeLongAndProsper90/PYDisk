"""
def system(command, ar1):
    import subprocess

    proc = subprocess.Popen([command, ar1], stdout=subprocess.PIPE, shell=True)
    out = (proc.communicate()[0]).decode()
    print(out.upper())
    return out.upper()
def system2(command, ar1, ar2, ar3):
    import subprocess

    proc = subprocess.Popen([command, ar1, ar2, ar3], stdout=subprocess.PIPE)
    out = (proc.communicate()[0]).decode()
    print(out.upper())
    return out.upper()
    """
from subprocess import check_output
class device():
    class permissionError(Exception):
        pass
    class notFoundError(Exception):
        pass
    class unknownError(Exception):
        pass
    class done(Exception):
        pass

    def __init__(self, de,pa):
        global dev
        global path
        dev = de
        path = pa

    def update_dev(self, de):
        global dev
        dev = de
        print("dev updated "+ dev)
    def update_path(self,pa):
        global path
        path = pa
        print("path updated " + path)
    def get_dev(self):
        return dev
    def get_path(self):
        return path

    def mount(self):
        output = check_output(['mount ','-v ', self.get_dev() + ' ', self.get_path()])
        print(output)
        
        if "mount: mount point " + self.get_path() +" does not exist" in output:
            raise self.notFoundError
        elif output == "mount: only root can do that":
            
            raise self.permissionError
        elif 'mounted' in output:
            raise done
        else:
            raise self.unknownError 
    def umount(self):
        output = system('mount',  self.dev + ' ' + self.path)
        if "No such file or directory" in output:
            raise self.notFoundError
        elif "only root can do that" in output:
            raise self.permissionError
        else:
            raise self.unknownError
