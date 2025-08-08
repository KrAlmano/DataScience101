

def alternating(string):
    new_string=''
    for i in range(len(string)):
        if i%2 == 0:
            new_string +=string[i].upper()
        else:
            new_string+=string[i].lower()

    return new_string


alternating('almano')

####
#Enumerate

students =['ahmet', 'mehmet', 'furkan', 'almano']

def divide_students(students):
    group=[[],[]]

    for i,student in enumerate(students):
       if i %2 ==0 :
           group[0].append(student)
       else:
           group[1].append(student)

    print(group)
    return group


divide_students(students)


#Alternating fonksiyonunu enumerate ile bastan yaziyoruz

def alternating_w_enumerate(string):
    new_string= ''
    for i,letter in enumerate(string):

        if i%2 == 0:
            new_string += letter.upper()
        else :
            new_string += letter.lower()

    print(new_string)



alternating_w_enumerate('abcdskadhfuioasdnfboiasbdnfoisadfbnoiasdb')


