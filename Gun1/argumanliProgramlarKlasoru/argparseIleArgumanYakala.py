
#%%writefile ile hücre içeriğini dosya basıyoruz.
#python argparseIleArgumanYakala.py 1.3, "C:\\sonuc.txt"
#python argparseIleArgumanYakala.py a_lambda=1.3, a_yol"C:\\sonuc.txt" --> parametre adını kullandı. metavar olarak ifade edilr.
import argparse

my_parser = argparse.ArgumentParser(description="Argumanları yakalama programı ....")

#argumanları tanımlayalım.
my_parser.add_argument('--a_yol',  #metaver. dışarıdan arguman girerken kullanılacak isim.
                        type=str, 
                        help='Yol bilgisi',
                        required=True)  #required=True zorunlu olmasını sağlar.
my_parser.add_argument('--a_lambda', type=float, help='Lambda değeri')

#
#argumanları okuyalım.
my_argumans = my_parser.parse_args()# argumanları python nesnelrine parse etmemizi dönüştürmemizi sağlıyor

#
print(my_argumans)
print(f"Giriş yapılan yol {my_argumans.a_yol} ve Lambda değeri {my_argumans.a_lambda}") #arguman değerlerine ulaşabiliriz.
