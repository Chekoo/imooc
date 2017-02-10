# valid = False
# count = 3
# while count > 0:
#     input = raw_input('Enter password')
#     # check for valid passwd
#     for eachPasswd in passwdList:
#         if input == eachPasswd:
#             valit = True
#             break
#     if not valid:
#         print 'invalid input'
#         count -= 1
#         continue
#     else:
#         break


#
# legends = { ('Poe', 'author'):(1809, 1849, 1976), ('Gaudi', 'architect'):(1852,1906,1987),
#             ('Freud', 'psychoanalyst'):(1856, 1939, 1990)}
#
# for each in legends:
#     print 'Name: %s\tOccupation: %s' % each
#     print 'Birth: %s\tDeath: %s\tAlbum: %s\n' % legends[each]


# myFile = open('note.txt')
# for each in myFile:
#     print each


f = open('/etc/motd', 'r')
longest = 0
alllines = f.readline()
f.close()
for line in alllines:
    linelen = len(line.strip())
    if linelen > longest:
        longest = linelen
    return longest

f = open('/etc/motd', 'r')
allLinesLens = [len(x.strip()) for x in f]
f.close()
return max(allLinesLens)

f = open('/etc/motd', 'r')
longest = max(len(x.strip()) for x in f)
f.close()
return longest
