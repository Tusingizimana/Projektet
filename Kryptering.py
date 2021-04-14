# coding: utf-8
#inlämningsuppgiften 1b
# coding: utf-8
def encrypt (text, key):
 '''to encrypt I convert the plain text using the given key into unreadable text
    with the help of cipher method.
    For example if the key is 11, I substitute every letter in the plain text with another letter,
    which is 11 letters behind that particular letter in the alphabetical order.
    For each encrypted letter I simply add the key to that particular letter in the plain text.'''
 
 encrypted = ""
## kod för att krypterar text med hjäp av key och lögga den krypterade texten i variable encrypted 
 ''' If the key given is bigger than 28 which is the total number of alphabets I was using.
     that key is divided with 28 and the remainder becomes the new key.
     For each new encrypted letter, I add the new key to the letter in plain text'''
 
 if key > 28:
    key =key%28
 for tecken in text : 
    '''In ASCII Table each alphabet has a correspondering numnber, 
      therefore I choose to use numbers instead of letters. For each letter in plain text plus key
      is equal to new letter, 
      that is to say for each correspondering number plus key equals a new number 
      equivalent to encrypted letter''' 
  
    tal= ord(tecken)
    nyttal= tal + key
    nyttecken=chr(nyttal)
    encrypted += nyttecken
 return encrypted

def decrypt (text, key):
   '''With decrypting, I convert the encrypted text into plain text using the given key. 
       However, I don´t replace the letter in the encrypted text by adding the key,
       instead I substract it from that letter. 
       Which means that I go backward in the alphabetical order.
       for each decrypted letter is equivalent to encrypted letter minus key'''
   decrypted = ""
    ## kod för att decrypterar text med hjälp av key och lögga den decrypterade tetxten i variable decrypted
   '''As with encrypting so it is with decrypting, the only differnce is that the new key which is 
      the remainder of the bigger key divided by 28 total number of alphabets, 
      is subtracted from the encrypted letter.
      for each decrypted letter is equal to encrypted letter minus new key.'''
   if key >28:
     key= key%28
   for tecken in text :
     '''In ASCII Table each alphabet has a correspondering number, 
        I replace letters in encrypted text with 
        their correspondering numbers. For each decrypted letter is same as 
        the correspondering number minus the key.'''
     
     tal= ord(tecken)
     nyttal= tal - key
     nyttecken=chr(nyttal)
     decrypted += nyttecken
     
   return decrypted
     
def runtestcode (text, key):
   print ("-"*50)
   print ("klartext!", text, "key ",key )
   etext =encrypt (text, key)
   print ("krypterat! ", etext)
   dtext = decrypt (etext, key)
   print ("Avkodat :",dtext)
     
# Huvudpragrammet (Testkod)
runtestcode ("knas",7)
runtestcode ( "knasBoll",27)
runtestcode ("'knas' i äpplet, säger Sara",67)

