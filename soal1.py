def reverseHuruf(a):
    abjad = [b for b in a if b.isalpha()]
    angka = [b for b in a if b.isdigit()]
    return ''.join(reversed(abjad)) + ''.join(angka)

input_string = "NEGIE1"
hasil = reverseHuruf(input_string)
print(hasil)
