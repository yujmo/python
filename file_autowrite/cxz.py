import sys

def readfile(fname):
    with open fname as f:
        return f.readlines()

def main(rfile, wfile):

    pattFile = readfifle(rfile)

    with open wfile as wf:
        for ee in range(40):
            res = pattFile
            res[2] = res[3].replace()
            res[6] = res[6].replace()
            wf.writelines(res)

if __name__ == "__main__":
    rfile, wfile = sys.argv[1:2]
    main(rfile, wfile)

