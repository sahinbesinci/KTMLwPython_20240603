
#%%writefile ile hücre içeriğini dosya basıyoruz.
#python sysIleArgumanYakala.py elma, karpuz, kiraz
import sys

print("Arguman listesinin eleman sayısı",len(sys.argv))
print("Programın adı:",sys.argv[0])
print("Programın argumanları", sys.argv[1:]) #slicer ile diğer elemanları alalım.
