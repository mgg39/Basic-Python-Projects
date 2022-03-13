from pycipher import Playfair

#Welcome message
print("Welcome to my decoder. \n" + "It decodes coded messages in Caesar cipher, Morse code, Public-key cryptography and Playfair cipher. \n" + "If you wish to use Caesar cipher input Caesar as code type, Morse for Morse code, Keys for Public-key cryptography and Playfair for Playfair cipher. \n" + "If you are unsure about what each type of code is/does or are just interested in coded messages input Info as the code type and I will give you a link to a fun page explaining it!")

#initial values set ups
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"

#Morse dictionary settup
morse_dictionary = {".-":"A","-...":"B","-.-.":"C"}
morse_dictionary["-.."] = "D"
morse_dictionary["."] = "E"
morse_dictionary["..-."] = "F"
morse_dictionary["--."] = "G"
morse_dictionary["...."] = "H"
morse_dictionary[".."] = "I"
morse_dictionary[".---"] = "J"
morse_dictionary["-.-"] = "K"
morse_dictionary[".-.."] = "L"
morse_dictionary["--"] = "M"
morse_dictionary["-."] = "N"
morse_dictionary["---"] = "O"
morse_dictionary[".--."] = "P"
morse_dictionary["--.-"] = "Q"
morse_dictionary[".-."] = "R"
morse_dictionary["..."] = "S"
morse_dictionary["-"] = "T"
morse_dictionary["..-"] = "U"
morse_dictionary["...-"] = "V"
morse_dictionary[".--"] = "W"
morse_dictionary["-..-"] = "X"
morse_dictionary["-.--"] = "Y"
morse_dictionary["--.."] = "Z"

punctuation = ".,?'! "
print("Type of code used:")
code_type = input("type_of_code \n").title()
decoded_message = ""

#Info
if code_type == "Info":
 print("https://www.enkivillage.org/types-of-codes.html")
 decoded_message += "None"

#Caesar cipher decoding
elif code_type == "Caesar":
  print("Input the offset by which the message in  coded within the alphabet: \n")
  x = int(input("code letter shift"))
  print("Input coded message:")
  message = input("Coded message \n")
  for letter in message:
     if not letter in punctuation:
      letter_value = letters.find(letter)
      decoded_message += letters[(letter_value + x) % len(letters)]
     else:
      decoded_message += letter

#Morse
elif code_type == "Morse":
    print("Input coded message:")
    message = input("Coded message \n")
    for sign in message.split(" "):
        if sign in morse_dictionary:
          decoded_message += morse_dictionary[sign] 
        else:
          decoded_message += " "

#Public-key cryptography
elif code_type == "Keys" :
    print("Input public_key: " )
    public_key= input("Public key \n")
    while len(public_key) != 6:
        if len(public_key) > 6:
            print ("Error! Public key's are 6 characters long!")
        else:
            print ("Error! Public key's are 6 characters long!")
        public_key= input("Public key \n")
    print("Input private key:" )
    private_key= input("Private key \n")
    while len(private_key) != 2:
      if len(private_key) > 2:
        print ("Error! Public key's are 2 characters long!")
      else:
        print ("Error! Public key's are 2 characters long!")
      private_key= input("Private key \n")

    decoded_message += str(int(private_key) * int(public_key))

#Playfair Cipher
#check out kanpurpython.wordpress.com/2017/08/22/playfair-cipher-using-python/
elif code_type == "Playfair":
    print("Input coded message:")
    message = input("Coded message \n")
    decoded_message += Playfair("cdabefhgkijlmnoprqstuvzwxy").decipher(message)

print("Decoded message: \n" + decoded_message.title())
print("You welcome.")