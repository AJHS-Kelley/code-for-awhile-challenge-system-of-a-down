#Cow Language

# string = input().split(" ", 99)
# newstring = ""
# hold = ""
# for i in string:
#     test = i.lower()
#     # if test[0] == "!":
#     #     pass
#     if test[0] == "a" or test[0] == "e" or test[0] == "i" or test[0] == "o" or test[0] == "u":
#         if i[-1] == "!":
#             hold = i.replace("!", "")
#             hold = hold + "moo! "
#         else:
#             hold = i + "moo "
#     else:
#         if i[-1] == "!":
#             hold = i.replace("!", "")
#             hold = i + i[1] + "moo! "
#             hold = hold.replace(i[0], "")
#         else:
#             hold = i + i[0] + "moo "
#             hold = hold.replace(i[0], "")
#     newstring += hold
# print(newstring)


string = input().split(" ", 99)
newstring = ""
hold = ""
for i in string:
    test = i.lower()
    vowel = False
    punct = False
    if test[0] == "a" or test[0] == "e" or test[0] == "i" or test[0] == "o" or test[0] == "u":
        vowel = True
    if test[0] == "a" or test[0] == "e" or test[0] == "i" or test[0] == "o" or test[0] == "u":
        punct = True

    if test[0] == "!":
        hold = hold + ""
    elif code1 == 1:
        if i[-1] == "!":
            hold = i.replace("!", "")
            hold = hold + "moo! "
        else:
            hold = i + "moo "
    elif code1 == 0:
        if i[-1] == "!":
            hold = i.replace("!", "")
            hold = hold + i[0] + "moo! "
            hold = hold.replace(i[0], "")
        else:
            hold = i + i[0] + "moo "
            hold = hold.replace(i[0], "")
    newstring += hold
print(newstring)