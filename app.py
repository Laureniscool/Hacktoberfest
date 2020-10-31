print("Title of program: Post-exam bot")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("to go find something interesting to do, there are so many new things to learn, just go surf the internet")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("to keep smiling")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("to rest early, take a break")
      counter += 1
    if each_word == "sad":
      feelings_list.append("depressed")
      encouragement_list.append("to cheer up and have fun, do the things that you enjoy")
      counter += 1
    if each_word == "depressed":
      feelings_list.append("sad")
      encouragement_list.append("to cheer up and have fun, do the things that you enjoy")
      counter += 1
    if each_word == "scared":
      feelings_list.append("scared")
      encouragement_list.append("that there's nothing to be afraid of, so relax")
      counter += 1
    if each_word == "disappointed":
      feelings_list.append("disappointed")
      encouragement_list.append("No worries. You will do better next time!")
      counter += 1
    if each_word == "lazy":
      feelings_list.append("lazy")
      encouragement_list.append("you can laze, but make sure you set aside enough time for revision and preparations for next year and do something meaningful")
      counter += 1
    if each_word == "unmotivated":
      feelings_list.append("unmotivated")
      encouragement_list.append(" Take this time to find out about your interests and talk to your friends and families about it, I am sure you will find their support and your joy in doing the things you like is a great source of motivation")
      counter += 1
    if each_word == "angry":
      feelings_list.append("angry")
      encouragement_list.append("Breathe, calm yourself, make sure that you think before you act, do not make rash decisions. It would be good to let the anger pass before making a move, or you might regret you words and actions")
      counter += 1
    if each_word == "confused":
      feelings_list.append("confused")
      encouragement_list.append("You don't have to have it all figured out to move forward")
      counter += 1
    if each_word == "lost":
      feelings_list.append("lost")
      encouragement_list.append("Sometimes, you have to stop thinking too much and just go where your heart takes you")
      counter += 1
    if each_word == "lonely":
      feelings_list.append("lonely")
      encouragement_list.append("Talk to a friend or your family and remember I'll be there for you!")
      counter += 1
    if each_word == "guilty":
      feelings_list.append("guilty")
      encouragement_list.append("Admit your mistake and try to fix it. Mistakes are inevitable.")
      counter += 1
   
   
      
     
  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". Do remember "+ encouragement_list[0] + "! Hope you feel better :)"  

  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". Do remember "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
