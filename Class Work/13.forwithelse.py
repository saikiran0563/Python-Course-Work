products=['laptop','mouse','keypad','speaker','watch']
search=input("Enter the product:").strip()

for i in products:
    if i==search:
        print("Product is available in the store! Shop now")
        break
    print(i)
else:
    print("End of the products.The Product you search for is not available in the store!")
