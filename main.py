print("Math Game!!!")

num=int(input("Pick a number of your choice!: "))
print("Try answering the correct multiples of this number: ",num,"\n you will get a point for correct answers only")

score = 0


for i in range(1,11):
  
  print(i," X ",num," = ??")
  ans = int(input("Type your answer! "))
  if ans == i*num:
    print("Great work!!!")
    score+=1
  else:
    print("Wrong! Answer was: ",i*num)



if score==10:
  print("You got all the 10 correct 🥳")
else:
  print("You scored ",score," out of 10")
  
  


  
  
  

