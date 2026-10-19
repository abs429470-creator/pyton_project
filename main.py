import  json
def countLeters(urlTextFile):
    count = 0
    with open(urlTextFile, 'r') as f:
        for line in f:
            words = line.split()
            count += len(words)
    return count

print(countLeters('./try me.txt'))

def writeAndPrint(urlJsonFile, dictWithItems):
    with open(urlJsonFile, 'w') as f:
        json.dump(dictWithItems, f )
    with open(urlJsonFile, 'r') as f2:
       data = json.load(f2)
    print(data)

writeAndPrint('./data.json',{
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phone": "9976770500"
})