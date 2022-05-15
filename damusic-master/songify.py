def songify(dbcol):
    import random
    n = random.randint(0,18)
    NotesList = dbcol.find_one()
    sub_list=[
        [NotesList["0"],NotesList["2"],NotesList["5"],NotesList["7"]],
        [NotesList["0"],NotesList["3"],NotesList["5"],NotesList["7"]],
        [NotesList["0"],NotesList["4"],NotesList["5"],NotesList["7"]],
        [NotesList["0"],NotesList["10"],NotesList["5"],NotesList["7"]],
        [NotesList["0"],NotesList["5"],NotesList["8"],NotesList["10"]],
        [NotesList["0"],NotesList["3"],NotesList["8"],NotesList["7"]],
        [NotesList["0"],NotesList["7"],NotesList["5"],NotesList["8"]],
        [NotesList["0"],NotesList["5"],NotesList["2"],NotesList["7"]],
        [NotesList["5"],NotesList["0"],NotesList["4"],NotesList["9"]],
        [NotesList["0"],NotesList["9"],NotesList["2"],NotesList["5"]],
        [NotesList["0"],NotesList["3"],NotesList["5"],NotesList["10"]],
        [NotesList["0"],NotesList["7"],NotesList["4"],NotesList["9"]],
        [NotesList["0"],NotesList["7"],NotesList["4"],NotesList["9"]],
        [NotesList["0"],NotesList["10"],NotesList["3"],NotesList["5"]],
        [NotesList["0"],NotesList["8"],NotesList["7"],NotesList["5"]],
        [NotesList["0"],NotesList["4"],NotesList["9"],NotesList["11"]],
        [NotesList["0"],NotesList["10"],NotesList["8"],NotesList["7"]],
        [NotesList["0"],NotesList["8"],NotesList["3"],NotesList["5"]],
        [NotesList["0"],NotesList["2"],NotesList["3"],NotesList["5"]]]
     
    return sub_list[n]
    