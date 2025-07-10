with open('Example.txt','w') as file:
    file.write("I am done with this!")
    file.write(" Can I go Out ?")
with open('Example.txt','a') as file:
    file.write("Ok maam Deepika")
with open('Example.txt','r') as file:
    data=file.read()
print(data)