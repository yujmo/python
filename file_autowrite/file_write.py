import sys
def readfile(fname):
    with open(fname) as f:
        return f.readlines()

def main(rfile,wfile):
    with open(wfile,'w') as wf:
        for ee in range(2,41):
            res = readfile(rfile)[2:]
            res[0] = res[0].replace("sshd1","sshd"+str(ee))
            res[3] = res[3].replace("11001",str(11000+ee))
            wf.writelines(res)

if __name__ == "__main__":    
    rfile,wfile = sys.argv[1:]
    main(rfile,wfile)
