# f = open("demofile.txt", "r")
# print(f.read())
# print(f.read(5))
# print(f.readline())

f = open("demofile.txt", "a")
f.write("Now the file has one more line!")

# for x in f:
  # print(x)


f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")

f = open("myfile.txt", "w")
f.write("Woops! I have deleted the content!")