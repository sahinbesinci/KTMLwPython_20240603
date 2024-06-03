# Paket ve Bağımlılıkları Yüklemek
* Paketlerin bağımlılıklarnı listeleme
* Bağımlılıktan yükleme
* whl (wheel) dosyları ile internetsiz paket yükleme

## 1. Yöntem: `pip` aracı ile
### pip aracını kurmak:
  1. get-pip.py dosyası ile [https://bootstrap.pypa.io/get-pip.py](https://bootstrap.pypa.io/get-pip.py)
  2. komut satırından
	```shell
	# ensurepip standart kütüphanesi ile.
	> py -m ensurepip --upgrade

	#pip aracı yükselt
	> py -m pip install --upgrade pip
	```
  3. Linux paket manager ile
	```shell
	> sudo apt update
	> sudo apt install python3-venv python3-pip
	```
### pip aracı ile paket kurulumu ve paket hakkında bilgi almak
```shell
> pip install paketAdi
> pip install --upgrade paketAdi
> pip install --force-reinstall 'sqlalchemy==1.4.36'
> pip uninstall paketAdi
> pip list
> pip show paketAdi

# paketi zorla yeniden yükle
> pip install matplotlib --force-reinstall
```

#### requirement dosyası ile paket kurmak
```shell
pip install -r requirements.txt
```

#### requirement dosyası oluşturmak
1. Elle oluşturulabilir.
2. Ortamdaki mevcut paketleri requirement dosyası formatında üretir.
	```shell
	pip freeze > gereklilikler.txt
	```	
### wheel (whl) dosyası ile internet olmadan kurmak için
1. whl dosyası indir
```shell
> pip download pandas
```
2. inen whl dosyaları ile paketi yükle (offline)
```shell
> pip install numpy-1.26.4-cp311-cp311-win_amd64.whl
```

## 2. Yöntem: `pipdeptree` aracı ile
1. paketin bağımlılıklarını listeleyenler pipdeptree aracını indirelim.
```shell
> pip install pipdeptree
```
2. bağımlılıklarını listeleyelim
```
# tüm bağımlılıkları tree yapısında listeler.
> pipdeptree

# yardım
> pipdeptree -help

#sadece pandas bağımlılıklarını listeler
> pipdeptree -p pandas

# requirements formatta (freeze)
> pipdeptree -p pandas -f

# requirements formatta (freeze) txt dosyasına yazar.
> pipdeptree -p pandas -f > requirements.txt
```
	
# Virtual Environment oluşturmak
1. `venv` paketini kurmak
	```shell
	> pip install virtualenv
	```
2. Bir klasoru VirtualEnvironment olarak tanımlamak ve 	
	```shell
	> python -m venv "D:\sanalOrtam"
	```
3. VirtualEnvironmentı aktif etmek (klasordeki bat dosyası ile)
	```
	> D:\sanalOrtam\scripts\Activate.bat
	# aktif edilen ortamda çalışmak
	(sanalOrtam) > pip install emoji
	```
4. VirtualEnvironmentı deaktif etmek  (klasordeki bat dosyası ile)
	```
	> D:\sanalOrtam\scripts\deactivate.bat
	```

