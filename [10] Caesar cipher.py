logo = """           
 ██████╗ █████╗ ███████╗███████╗███████╗██████╗ 
██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗
██║     ███████║█████╗  ███████╗█████╗  ██████╔╝
██║     ██╔══██║██╔══╝  ╚════██║██╔══╝  ██╔══██╗
╚██████╗██║  ██║███████╗███████║███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
                                                
 ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗      
██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗     
██║     ██║██████╔╝███████║█████╗  ██████╔╝     
██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗     
╚██████╗██║██║     ██║  ██║███████╗██║  ██║     
 ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝          
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Caesar cipher start
def caesar(start_text, shift_amount, cipher_direction):
  shift_amount %= 26
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    numsym = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '\\', '/', '@', '$', '%', '^', '&', '*', '.']
    if char in numsym:
      end_text += char
    elif char == " ":
      end_text += " "
    else:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}\n")

#Function for repeating the cipher
def caesar_repeat():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

print(logo)
print("Instructions: Caesar cipher is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.\n")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

#Looping the cipher until the user says no
stop_game = False
while not stop_game:
  run_again = input("Type 'yes' if you want to go again. Otherwise type 'no' : ").lower()

  if run_again == "yes":
    caesar_repeat()
  else:
    stop_game = True
    print("goodbye")
