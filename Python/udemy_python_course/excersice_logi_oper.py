is_magician = input("are you a magician? Type True or False\n")
                # Q1 check if magician AND expert: " you are a master magician"
                # Q2 check if magician but not expert: "at least you're getting there"
		        # Q3 if you're not a magician: "you need magic powers"
if is_magician == "True":             
				#If conditional to check if the user is a magician in the first place.
    is_expert = input("are you an expert magician? Type True or False\n")               
				#Takes a true or false input from the user in order to determine if he is an expert in the next step
    magician = "you are a master magician" if is_expert == "True" else "at least you're getting there"                
				#One liner if-else statement.
    print (magician)                
				#prints the output of magician.
else:               
				#else conditional
    print ("you need magic powers")             
				#prints the output if the user is not a magician.