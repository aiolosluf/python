word = "bottles"

for num in range(5,0,-1):
    print(num,word,"of beer on the wall.")
    print("take one down")
    if num == 1:
        print("no more beers.")
    else:
        left = num - 1
        if left == 1:
            word = "bottle"
        print(left,word,"of beer left.")

