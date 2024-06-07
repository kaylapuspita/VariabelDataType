def hitung_huruf_kapital(kata):
  
  jumlah_huruf_kapital = 0
  for huruf in kata:
    if huruf.isupper():
      jumlah_huruf_kapital += 1
    return jumlah_huruf_kapital

#Contoh penggunaan
kata = "InfOrmatIKA"
jumlah_huruf_kapital = hitung_huruf_kapital(kata)
print(f"Jumlah huruf kapital dalam kata '{kata}' adalah {jumlah_huruf_kapital}")