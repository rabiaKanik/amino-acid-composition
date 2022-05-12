#if not satir:
 #   break  # satir olmadigi zaman dongu sonlandiriliyor
#print("'R' harfi sayısı: ", satir.count("R"))
 #       print("'N' harfi sayısı: ", satir.count("N"))
  #      print("'D' harfi sayısı: ",satir.count("D"))
   #     print("'C' harfi sayısı: ",satir.count("C"))
    #    print("'E' harfi sayısı: ",satir.count("E"))
     #   print("'Q' harfi sayısı: ",satir.count("Q"))
      #  print("'G' harfi sayısı: ",satir.count("G"))
       # print("'H' harfi sayısı: ",satir.count("H"))
        #print("'I' harfi sayısı: ",satir.count("I"))
        #print("'L' harfi sayısı: ",satir.count("L"))
        #print("'K' harfi sayısı: ",satir.count("K"))
        #print("'F' harfi sayısı: ",satir.count("F"))
#countLetter = satir.count("A")
#value = (100 * countLetter) / length
#dosya2.write(str(value))
#dosya2.write("\n")
import numpy as np

dosya = open('Noneff_Validation.txt', 'r')
dosya2 = open("Noneff_Validation_aac.txt", "a", encoding="utf-8")

toplam = 0
while True:
    satir = dosya.readline()

    if (satir.startswith(">")):
        dosya2.write("\n")
        aminoArr = np.array(
            [['A', 'R', 'N', 'D', 'C', 'E', 'Q', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V'],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
        #dosya2.write(satir)
        i = 0
        toplam = 0

    elif(satir.startswith(">") == False & satir.startswith(" ") == False) :
        #dosya2.write("{ ")
        length = len(satir)
        #print(length -1)
        for i in range(20):
            aminoArr[1][i] = satir.count(aminoArr[0][i]) / (length -1)
            toplam = float(aminoArr[1][i])+ toplam
            dosya2.write(aminoArr[1][i])
            dosya2.write(",")
        dosya2.write("noneff")
        print(aminoArr)
        print(toplam)
    if not satir:
        break
dosya.closed
dosya2.closed