def BoyamaHakkinda():
    print("renkler ve şekiller kullanarak boyama yapabilirsiniz.")
    print("Boyamayı eglenceli hale getirdik.")

#--------
def selamVer():
    print("merhaba dünyalı")

#---------
#from ... import * kullandığımız __all__ ile belirtilen moduller ortama alınır
__all__ = ["renkler", "sekiller", "yazarlar"]

#--------
if __name__ == "__main__": #biri doğrudan __init__.py dosyasını çalışıyorsak
    selamVer()
    print("Kodları direkt çalıştırdınız. Aslında bu başka bir yerden çağırılacak bir pakettir.")
