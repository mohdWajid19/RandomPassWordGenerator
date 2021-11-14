import random as r
n = int(input("enter the number of digits : "))


# if you want comletely random comment code from line 12 to end 
password = ''
password_characters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','(',')','*','&','^']
for i in range(n):
    # password += password_characters[r.randint(0,len(password_characters)-1)]
    password += r.choice(password_characters)
print(password)


# if you want to specify number of digts and characters then use below code
password_list = []
characters = int(input("enter the number of Special characters : "))
numbers = int(input("enter the number of numbers : "))
alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers_list = ['1','2','3','4','5','6','7','8','9','0']
special_chars = ['!','@','#','$','%','(',')','*','&','^']
for i in range(n-characters-numbers):
    # password_list.append(alphabets[r.randint(0,len(alphabets)-1)])
    password_list.append(r.choice(alphabets))

for i in range(characters):
    # password_list.append(special_chars[r.randint(0,len(special_chars)-1)])
    password_list.append(r.choice(special_chars))

for i in range(numbers):
    # password_list.append(numbers_list[r.randint(0,len(numbers_list)-1)])
    password_list.append(r.choice(numbers_list))

r.shuffle(password_list)
password = ""
print(password.join(password_list))