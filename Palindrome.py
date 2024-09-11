text = str(input("Write some text "))
no = int(input("Provide a number "))
reverse_text = text[::-1]
reverse_no = 0
reverse_no = reverse_no*10 + no%10
no//=10
if (reverse_text == text and str(reverse_no == no)):
 print("The given text " + text + " and number " + str(no) + " is palindrome ")
 
