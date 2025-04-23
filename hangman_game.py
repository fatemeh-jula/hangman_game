from random import choice

list1 = ["banana" , "apple" , "watermelon" , "orange" , "cherry" , "mango" , "blueberry" , "kiwi" , "lemon" , "avokado"]

fruite =list(choice(list1))

len_fruite = list("-" * len(fruite))

while True :
    u="".join(len_fruite)
    print(u)
    hads = input("hadse harf: ")

    if not hads.isalpha() or len(hads) != 1 :
        print("lotfan harf vared kon!")
        continue

    len_fruite = list(u)
    
    for j in range (len(fruite)) :
        if hads == fruite[j] :
            len_fruite[j]=hads
        elif hads != len(fruite) :
            continue
    if fruite == len_fruite :
         print ("".join(fruite))
         print("huuura")
         break