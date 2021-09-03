import os
import hashlib

eicar = 'C:/Users/gksru/Documents/programming/anti-virus/eicar.txt' 
eicar_md5 = '44d88612fea8a8f36de82e1278abb02f' 

fp = open(eicar)
fbuf = fp.read()

m = hashlib.md5()
m.update(fbuf)
fmd5 = m.hexdigest()
print(fmd5)

if fmd5 == eicar_md5:
    print 'virus!!'
    
else:
    print 'no virus'
fp.close()