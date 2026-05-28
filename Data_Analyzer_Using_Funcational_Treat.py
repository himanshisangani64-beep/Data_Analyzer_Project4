data_store = []


def User_Data_Get():
    '''User Give Input Form Numeric Data , This Data Store on 1D Array '''

    r1 = int(input("Enter Your Range"))
    
    for i in range(0,r1):
        print(i,"Eelement Enter")
        num = int(input())
        data_store.append(num)

def Diplay_Data_Summery():
    '''Show All The Data '''
    sum1 = 0
    avg = 0
    for i in data_store:
        print(i)
        sum1+=i
        avg = sum1/len(data_store)
    print("-------------------------------")
    print(" - Maximum Number",max(data_store))
    print(" - Minimum Number",min(data_store))
    print(" - Lenght Of Data",len(data_store))
    print(" - Sum Of All Element ",sum(data_store))
    print(" - Average Value",avg)


def fact(n):
    '''Give The Fctorial Number'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * fact(n-1)    


def Filter_Data(*data):
     '''Give The For Type Of Filter Apply Odd/Even and Greter Than Or Less Than Or Between Value '''
     for i in data:
         print(i)

     while True:
         print("1) Filter Even Value")
         print("2) Filter Bteween Value")
         print("3) Filter Greter Than Value")
         print("4) Filter Less Than Value")
         print("5) Exit")

         ch1 = int(input("Enter Your Choice "))

         match ch1 :
             case 1 :
                 print("---Filter Even Value---")
                 print()

                 lmd = filter(lambda x : x%2==0,data_store)
                 print(list(lmd))
             case 2 : 
                  print("---Filter Between Value---")
                  print()

                  num1 = int(input(" First Enter Your Value"))
                  num2 = int(input(" Second Enter Your Value"))
                  lmd = filter(lambda x : x>num1 and x<num2,data_store)
                  print(list(lmd))
             case 3 : 
                  print("---Filter Greter Than Value---")
                  print()

                  num1 = int(input("Enter Your Value"))
                  lmd = filter(lambda x : x>=num1,data_store)
                  print(list(lmd))
             case 4 : 
                  print("---Filter Less Than Value---")
                  print()

                  num1 = int(input("Enter Your Value"))
                  lmd = filter(lambda x : x<=num1,data_store)
                  print(list(lmd))
             case 5 : 
                 break   

def Sort_data(*data):
    '''Two Type Of Sort Are Use Acending And Desending  '''
      
    while True:
         print("1)  Acending Value")
         print("2)  Desending Value")
         print("3) Exit")

         ch1 = int(input("Enter Your Choice "))

         match ch1 :
             case 1 : 
                 for i in data:
                    i.sort(reverse=False)

                    return i  
             case 2 :
                 for i in data:
                    i.sort(reverse=True)

                    return i 
             case 3 : 
                 break     
                 
def data_Statistics(name = "User",**kwargs):
    '''Give Information About Data '''
    
    return kwargs , name
    



while True:
    print("Welcome Data Analyzer And Transformer Program")
    print("Main Menu")
    print("1) Input Data")
    print("2) Display Data Summery")
    print("3) Calculate Fctorial")
    print("4) Filter Data")
    print("5) Sort Data")
    print("6) Data Statistics ")
    print("7) Exit")
    ch = int(input("Enter Your Choice"))

    match ch :
        case 1:
           print("---Input Data----")
           print()
           User_Data_Get()
           print("--------------------------------")
           

        case 2:
            print("---Display Data Sumery---")
            print()

            if data_store == []:
               print("Data Are Requried!   Give Proper Data.. ")
               ask = input("Are You Give Input Data ? [yes/No]").lower()

               if ask == "yes":
                   User_Data_Get()
               else:
                   print("Thank You For Give Your Answer")    
                   
            else:
                Diplay_Data_Summery()
            print("--------------------------------")  


        case 3:
            print("---Calculate Fctorial ---")
            print()
            
            num = int(input("Enter Your Number"))
            f = fact(num)
            print(num ,"Fctorial Number Is ",f)
            print("-----------------------------------")
           

        case 4:
            print("---Filter Data---") 
            print()

            if data_store == []:
               print("Data Are Requried!  Give Proper Data.. ")
               ask = input("Are You Give Input Data ? [yes/No]").lower()

               if ask == "yes":
                   User_Data_Get()
               else:
                   print("Thank You For Give Your Answer")   
            else:        
              Filter_Data(data_store)
            print("---------------------------------")


        case 5:
            print("---Sort Data---")
            print()

            if data_store == []:
               print("Data Are Requried!  Give Proper Data.. ")
               ask = input("Are You Give Input Data ? [yes/No]").lower()

               if ask == "yes":
                   User_Data_Get()
               else:
                   print("Thank You For Give Your Answer")   
            else:        
               s = Sort_data(data_store)
               print(s)
            print("---------------------------------")   

        case 6:
            print("---Data Statistics---")
            print() 
            while True:
                    print("1) Show  Perticuler Data  ")
                    print("2) Funcation Infomation")
                    print("3) Statistisc Data")
                    print("4) Exit")
                    ch2 = int(input("Enter Your Choice"))
                    match ch2 :
                        case 1 :
                            print("Data Treat In Funcation")
                    
                            keyword ,default = data_Statistics(name = "Himanshi",age = 21,Hobby = "Codding")  
                            print("Default Data   Welcome",default)  
                            print("Keyword Data",keyword)    
                            print("--------------------------------------------------------------")
                        case 2 : 
                            print("Funcation Infomation ")  
                            print()  
                            print("-",User_Data_Get.__doc__,"\n ") 
                            print("-",Diplay_Data_Summery.__doc__,"\n ") 
                            print("-",fact.__doc__,"\n ") 
                            print("-",Sort_data.__doc__,"\n ") 
                            print("-",Filter_Data.__doc__,"\n ") 
                            print("-",data_Statistics.__doc__,"\n ")  
                            print("----------------------------------")    

                        case 3 : 
                            print(" - Statistisc Data")
                            print(" - How Type Data Are Store ",type(data_store))
                            print(" - Memory Address",id(data_store))
                            print(" - Lenght Of Data",len(data_store))  
                            print()
                            if data_store == []: 
                                print("List Is Empty Add Data...")
                                User_Data_Get()
                                continue
                                print("------------------------------------")
                            else:    
                                print(" - Maximum Number",max(data_store))
                                print(" - Minimum Number",min(data_store))  

                        case 4 :
                            print()
                            break      

        case 7:

            print("-------------------------------------------------")
            print("Thank You For Use Data Analyzer And Transformer Program . GoodBye ! ")
            print()
            exit()    