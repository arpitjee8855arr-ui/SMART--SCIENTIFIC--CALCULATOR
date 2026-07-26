while True:
         print("\n---SMART SCIENTIFIC CALCULATOR---")
         print("1. Addition (+)")
         print("2. Subtraction (-)")
         print("3. Multiplication(*)")
         print("4. Division (/)")
         print("5. Square root (√)")
         print("6. Logarithm (log10)")
         print("7. Percentage(%)")
         print("8. Exit")
         choice = input("option select karo(1/2/3/4/5/6/7/8): ")
         if choice =="8":
          print(" CALCULATOR OFF HO GAYA. BYE BYE!")
          break
         elif choice =="1":
              num1 =float(input("First number:"))
              num2 =float(input("Second number:"))
              print("Result:", num1+num2)
         elif choice =="2":
              num1 =float(input("First number:"))
              num2 =float(input("Second number:"))
              print("Result:", num1-num2)
         elif choice =="3":
              num1 =float(input("First number:"))
              num2 =float(input("Second number:"))
              print("Result:", num1*num2)
         elif choice =="4":
              num1 =float(input("First number:"))
              num2 =float(input("Second number:"))
              if num2 ==0:
                print("Error:Zero(0) se divide nahi ho sakta!")
              else:
                 print("Result:",num1/num2)
         elif choice =="5":
            num1 = float(input("Number:"))
            if num1 < 0:
               print("Error:Negative number ka squareroot nhi hota!")
            else:
                 print("Result:",math.sqrt(num1))
         elif choice=="6":
             num1= float(input("Number: "))
             if num1 <=0:
                 print("Error: Logarithm non-positive numbers ke liye nahi  hota hai!")
             else:    
                 print("Result:", math.log10(num1))
         elif choice =="7":
              total =float(input("Total amount/value:"))
              percent =float(input("Percentage(%):"))
              print("Result:",(total*percent) /100)
                     
         else:
          print("Invalid choice! kripaya 1 se 8 tak select karo")               


