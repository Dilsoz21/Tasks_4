#Task_1
word = input("Enter the word:")

def first_and_last(word):
    first = list(word)
    first.sort()
    first.reverse()
    natija = ''.join(first)
    print(f"unorder word:", natija)


first_and_last(word)



#Task_2
lst = [1, 2, 3]
result1 = 0
result = 0
i = 0



def index_multiplier(lst, result, i, result1):
    while i < len(lst):
        x = lst[i]
        i += 1
        index = lst.index(i)
        result+= index
        result1 += index*x
        print(result1)


index_multiplier(lst, result, i, result1)



#Task_3
num = int(input("Enter the numer:"))
result = []
i = 1


def amplify(num, result, i):
    while i <= num:
        if i % 4 ==0:
            amplify = 10*i
            result.append(amplify)
        else:
            result.append(i)
        i += 1
    print("Result:", result)

amplify(num, result, i)


#Task_4
lst = [1, 2, 1, 1, 1, 1, 1]
i = 0


def unique(lst, i):
    while i < len(lst):
        x = lst[i]
        i += 1
        if lst.count(x) == 1:
            return x


print(unique(lst, i))



#Task_5_8
name = ["Google", "Apple", "Microsoft"]
i = 0


def sort(name, i):
    while i < len(name):
        j = i + 1
        while j < len(name):
            if len(name[i]) > len(name[j]):
                name[i], name[j] = name[j], name[i]
            j += 1
        i += 1

    print(name)


sort(name, i)


#Task_6
x = input("Enter the letter:")
lst1 = []
lst = [
  ["D", "E", "Y", "H", "A", "D"],
  ["C", "B", "Z", "Y", "J", "K"],
  ["D", "B", "C", "A", "M", "N"],
  ["F", "G", "G", "R", "S", "R"],
  ["V", "X", "H", "A", "S", "S"]
]
i = 0

def counter(x, lst1, lst, i):
    while i < len(lst):
        j = 0
        while j < len(lst[i]):
            if x == lst[i][j]:
                lst1.append(lst[i][j])
            j += 1
        i += 1


print(counter(x, lst1, lst, i))



#Task_7
lst = [1, 2, 3, 5, 2]

def remove_smallest(lst):
    lst.remove(min(lst))
    return lst
print(remove_smallest(lst))



#Task_9
list = [3,4]

i = 0
result = 0
def find_vektor(lst, index, result):
    while index < len(lst):
        x = list[index]
        result += x**2
        index += 1

    return int(result ** 0.5)


print(find_vektor(list, i, result))




#Task_10
name_dub = input("enter name:")
name = ["Firdavs", "Shuhrat", "Sardor"]
i = 0


def removing(name_dub, name, i):
    while i < len(name):
        x = name[i]
        i += 1
        if x == name_dub:
            name.remove(x)
            print(name)


removing(name_dub, name, i)




