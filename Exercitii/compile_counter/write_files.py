import compileCounter 

# import the old version (as an int) from the file
oldVersion = compileCounter.previousCompileVersion
newVersion = oldVersion + 1 

print("Old version was : ", oldVersion)

def incrementVersion(input):

    fileContainer = open("compileCounter.py","w+")

    fileContainer.write("previousCompileVersion = " + str(input))

    fileContainer.close() 

# call the increment function
incrementVersion(newVersion)
print("New version is : ", newVersion)

# TODO: De facut o verificare ptr existanta fisierului, if exista e ok if nu creeaza cu default 0
# TODO: De pus totul intr-o clasa importabila in fisierul main