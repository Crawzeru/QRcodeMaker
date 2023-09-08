import pyqrcode

url=str(input("Write the url: "))
qr_name=str(input("Choose name for your qr code: "))
uzanti=".svg"
final_name=qr_name+uzanti

qr_code=pyqrcode.create(url)
qr_code.svg(final_name,scale=5)