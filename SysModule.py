import sys# Sys module
sys.stderr.write("This is stderr text\n")
#otherwise it will print with lines next to each other
sys.stderr.flush()
sys.stdout.write("This is stdout text")


#-------------------------------------- Test 0
print(sys.argv)#This will print you the file path. We can pass arguments to this
#to communicate back and forth b/w other languages and python.
#sys.argv will display all of the arguments.

### PAST HERE WE USUALLY RUN ON CMD
# also you need to comment all the other tests while doing one test.

#https://www.youtube.com/watch?v=rLG7Tz6db0w&list=PLQVvvaa0QuDe8XSftW-RAxdo6OmaeL85M&index=36

#--------------------------------------------------- Test 1
if len(sys.argv) > 1: 
#before referencing arguments you should check if that amount of arguments is right.
    print(sys.argv[1])
    
#-------------------------------------------------------- Test 2
if len(sys.argv) > 1: 
    print(floast(sys.argv[1])+5)
    #print the float version of the second argument
    #You can use this yto pass arguments from anything.
    #Like if you're writing somethin in php you can use it
    #to communicate b/w php and python

#---------------------------------------------------------------- Test3
def main (arg):
    print(arg)

main(sys.argv[1])
#We just passed sys.argv[1] through the function.
#You can use it in classes as well. 


