import decode as d
running_disp =0
code_to_decode= 0b0101110100
p,decoded= d.EncDec_8B10B.dec_8b10b(code_to_decode,running_disp)
#decoded_value= bin(decoded)
print("Given input: ", "0101110100 - 10 bit")
print("Decoded Value: ", bin(decoded), "- 8 bit")
