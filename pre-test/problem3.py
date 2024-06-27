i_idx = int(input("initial index: "))
s_chunk = input("track chunk sizes: ")
all_track = s_chunk.split(' ')
all_track = [int(i) for i in all_track]

all_idx_song = []

counter = 1
for i in range(len(all_track)):
    sub_ls = []
    for j in range(all_track[i]):
        sub_ls.append(counter)
        counter+=1
    all_idx_song.append(sub_ls)
#print(all_idx_song)

all_seq = []

state = []
for i in range(len(all_track)):
    state.append(False)
    
summer = i_idx-1
for i in range(max(all_track)):
    for j in range(len(all_track)):
        try :
            all_seq.append(all_idx_song[j][i]+summer)
        except :
            continue

for ele in all_seq:
    print(ele, end=' ')