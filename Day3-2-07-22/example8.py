
isWifeTiered = (input('is wife tiered ? '))
isGasAvailable = True
if isWifeTiered == "1" or isWifeTiered == "yes" or isWifeTiered == "y":
    print("Bread Jam")
else:
    isGasAvailable = input("Gas A rahe ha ? ")
    if isGasAvailable == "1" or isGasAvailable == "yes" or isGasAvailable == "y":
        print("Anda Paratha")
    else:
        print("Sabar Karo")
