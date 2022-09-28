f = open("/Users/domenic/Desktop/softwaredev/githubstuff/trivia-refactoring/python3/Golden_Master.md", 'r')
g = open("/Users/domenic/Desktop/softwaredev/githubstuff/trivia-refactoring/python3/Output.md", 'r')

Golden_Master = f.readlines()
Output = g.readlines()
errors = []

for i in range(112):
    if Golden_Master[i] != Output[i]:
        errors.append("Error on Line: "+str(i)+"\nOutput: "+Output[i]+"Golden: "+Golden_Master[i])
if len(errors) == 0:
    print("No Errors")
else:
    for each in errors:
        print(each)