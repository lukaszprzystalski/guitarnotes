#try to identify what are the notes in provided Key
#ask user for note major scale

in_note = input('What noteD#: ').upper()


def notes(value):
    #notes_list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    notes_list = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    note = value.upper()

    major_scale_steps = [2,2,1,2,2,2,1]
    minor_scale_notes = [2,1,2,2,1,2,2]

    #find where provided note is located and rearrange notes_list accordingly
    ind = notes_list.index(note)
    n_tran = notes_list[ind:] + notes_list[:ind]

    #gather notes using major_scale_steps
    major_scale = [n_tran[0],n_tran[2],n_tran[4],n_tran[5],n_tran[7],n_tran[9], n_tran[11], n_tran[0]]
    minor_scale = [n_tran[0],n_tran[2],n_tran[3],n_tran[5],n_tran[7],n_tran[8], n_tran[10], n_tran[0]]

    #gather information about chords in minor/major scale
    #print chords that are available in provided scale

    print(n_tran)
    print('major scale notes: ', major_scale)
    print('minor scale notes: ', minor_scale)


notes(in_note)