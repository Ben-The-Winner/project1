def songify(notes):
    import random
    n = random.randint(0,16)
    NotesList=notes.copy()
    sub_list=[NotesList[0],NotesList[2],NotesList[5],NotesList[7]]
    sub_list2=[NotesList[0],NotesList[3],NotesList[5],NotesList[7]]
    sub_list3=[NotesList[0],NotesList[4],NotesList[5],NotesList[7]]
    sub_list4=[NotesList[0],NotesList[10],NotesList[5],NotesList[7]]
    sub_list5=[NotesList[0],NotesList[5],NotesList[8],NotesList[10]]
    sub_list6=[NotesList[0],NotesList[3],NotesList[8],NotesList[7]]
    sub_list7=[NotesList[0],NotesList[7],NotesList[5],NotesList[8]]
    sub_list8=[NotesList[0],NotesList[5],NotesList[2],NotesList[7]]
    sub_list9=[NotesList[5],NotesList[0],NotesList[4],NotesList[9]]
    sub_list10=[NotesList[0],NotesList[9],NotesList[2],NotesList[5]]
    sub_list11=[NotesList[0],NotesList[3],NotesList[5],NotesList[10]]
    sub_list12=[NotesList[0],NotesList[7],NotesList[4],NotesList[9]]
    sub_list13=[NotesList[0],NotesList[7],NotesList[4],NotesList[9]]
    sub_list14=[NotesList[0],NotesList[10],NotesList[3],NotesList[5]]
    sub_list15=[NotesList[0],NotesList[8],NotesList[7],NotesList[5]]
    sub_list16=[NotesList[0],NotesList[4],NotesList[9],NotesList[11]]
    if n==1:
        return sub_list
    elif n==2:
        return sub_list2
    elif n==3:
        return sub_list3
    elif n==4:
        return sub_list4    
    elif n==5:
        return sub_list5
    elif n==6:
        return sub_list6    
    elif n==7:
        return sub_list7 
    elif n==8:
        return sub_list8
    elif n==9:
        return sub_list9 
    elif n==10:
        return sub_list10             
    elif n==11:
        return sub_list11             
    elif n==12:
        return sub_list12
    elif n==13:
        return sub_list13
    elif n==14:
        return sub_list14
    elif n==15:
        return sub_list15
    elif n==16:
        return sub_list16