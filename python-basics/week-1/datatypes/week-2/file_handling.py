# Week 2 - Day 6 (File Handling)

# WRITE (file banana + data likhna)
file = open("data.txt", "w")
file.write("Hello Bhai!\n")
file.write("Ye meri pehli file hai")
file.close()


# READ (file ka data dekhna)
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()


# APPEND (data add karna)
file = open("data.txt", "a")
file.write("\nNew line add ki")
file.close()
