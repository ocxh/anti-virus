import os
import hashlib
import sys

eicar = 'C:/Users/gksru/Documents/programming/anti-virus/eicar.txt'
dummy = 'C:/Users/gksru/Documents/programming/anti-virus/Dummy.txt'
VirusDB = [
    '67:7e8043cdf89ae1e2d54e5793f8a73a4f:EICAR Test' ,
    '65:77bff0b143e4840ae73d4582a8914a43:Dummy Test'
]
vdb=[]
vsize=[]

def MakeVirusDB():
    for pattern in VirusDB:
        t=[]
        v = pattern.split(':')
        t.append(v[1])
        t.append(v[2])
        vdb.append(t)
        
        size = int(v[0])
        if vsize.count(size) == 0:
            vsize.append(size)
        
def SearchVDB(fmd5):
    for t in vdb:
        if t[0] == fmd5:
            return True, t[1]
    return False,''
        
if __name__=='__main__':
    MakeVirusDB()
    
    if len(sys.argv) != 2:
        print 'Usage : antivirus.py [file]'
        exit(0)
        
    fname = sys.argv[1]
    
    size = os.path.getsize(fname)
    if vsize.count(size):
        fp = open(fname,'rb')
        buf = fp.read()
        fp.close()
        
        m = hashlib.md5()
        m.update(buf)
        fmd5 = m.hexdigest()
        
        ret, vname = SearchVDB(fmd5)
        if ret == True:
            print '%s %s' %(fname, vname)
        else:
            print '%s : ok' %(fname)
    else:
        print '%s : ok' %(fname)