ap=int(input("Enter your Actual price of the good: "))
sp=int(input("Enter your Selling price of the good: "))

if sp>ap:
    profit=sp-ap
    print(f"Profit: {profit}")
    
elif sp==ap:
   
    print("No Profit or Loss")
    
else:
    loss=ap-sp
   
    print(f"Loss: {loss}")
    
        
