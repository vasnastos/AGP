# Required Packages

# pip3 install opencv-python qrcode numpy Image

import qrcode
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def main():
    target='https://chgogos.github.io/dituoi_agp/'
    qr_code_file_name='chgogos_AGP_QR.png'
    QRobj=qrcode.QRCode(version=1,box_size=12)
    QRobj.add_data(target)
    QRobj.make()
    QRImage=QRobj.make_image()
    QRImage.save(qr_code_file_name)

    img=mpimg.imread(qr_code_file_name)
    plt.imshow(img)
    plt.axis('off')
    plt.show()

if __name__=='__main__':
    main()

