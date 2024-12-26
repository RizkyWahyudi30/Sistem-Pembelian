data_product = {
    1:"ASUS VIVOBOOK",
    2:"Macbook",
    3:"Lenovo slimpad",
    4:"Mouse   ",
    5:"Mousepad",
    6:"Monitor",
    7:"SSD dan HDD",
    8:"Charger",
    9:"Processor",
    10:"Keyboard",
}
#  menggunakan metode "same key"
#  antara barang dan harga akan bersangkutan dengan "key" yang diatas, sebagai primary key
data_harga = {
    1: 14500000,
    2: 29000000,
    3: 12000000,
    4: 300000,
    5: 700000,
    6: 6000000,
    7: 750000,
    8: 900000,
    9: 14000000,
    10: 3000000,
}
dict_trx = {} ## data transaksi dikosongkan
daftar_metode_pembayaran = {
    1:"Transaksi bank",
    2:"Virtual account",
    3:"Cash on Delivery",
    4:"Kartu kredit",
}
print("============ List Produk ============")
#  pengulangan
for i in data_product:
    print("Id produk : ", i, "\t Nama produk : ", data_product[i], "\t Harga produk : ", data_harga[i])
pilih_id = int(input("Pilih id produk : "))
#  algoritma pengkondisian
if pilih_id in data_product :
    pilih_beli = input("Ingin beli ? (Y/N) : ")
    if pilih_beli == "y" or pilih_beli  == "Y":
        nama_penerima       = input("Nama penerima      : ")
        alamat_penerima     = input("Alamat penerima    : ")
        nomer_penerima      = input("No HP penerima     : ")
        kurir_pengiriman    = input("Kurir pengiriman   : ")
        dict_trx = {
            "Nama penerima": nama_penerima,
            "Alamat penerima": alamat_penerima,
            "Nomer penerima": nomer_penerima,
            "Kurir pengiriman": kurir_pengiriman,   
            "Produk id": data_product,
        }
    else:
        pass
    if len (dict_trx) > 0 :
        print("============ Metode Pembayaran ============")
    for i in daftar_metode_pembayaran:
        print("Id : ", i, "\t Metode pembayaran : ", daftar_metode_pembayaran[i])
    pilih_metode = int(input("Pilih Id metode pembayaran : "))
    if pilih_metode in daftar_metode_pembayaran:
        print("Nama penerima : ", dict_trx["Nama penerima"])
        print("Alamat penerima : ", dict_trx["Alamat penerima"])
        print("Nomer penerima : ", dict_trx["Nomer penerima"])
        print("Kurir pengiriman : ", dict_trx["Kurir pengiriman"])
        print("Produk : ", data_product[pilih_id])
        print("Harga : ", data_harga[pilih_id])
        print("Metode pembayaran : ", daftar_metode_pembayaran[pilih_metode])
        konfirmasi = input("Apakah sudah yakin ingin melakukan pembayaran ? (Y/N) : ")
        if konfirmasi == "y" or konfirmasi == "Y":
            print("Anda sudah berhasil melakukan pembayaran!")
        else :
            pass
    else :
        print("Metode pembayaran tidak tersedia!")
else :
    print("Id produk tidak tersedia!")