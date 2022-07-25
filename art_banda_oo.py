from class_art_banda import Art_banda, Playlist

conta1 = Art_banda('Baden', 'MPB', 'Solo', 697414, 78604, 760000.00)
conta2 = Art_banda('Guns Rush', 'Rock', 'Banda', 6064393, 847965, 7905301.00)
conta3 = Art_banda('Alcione Cristina', 'Samba', 'Solo', 2470071, 76821, 2495148.34)
conta4 = Art_banda('Lil Z Notorious', 'Hip hop', 'Solo', 3801168, 553690, 8227147.52)
conta5 = Art_banda('Luísa', 'Pop', 'Solo', 11581978, 1430464, 6229245.57)
conta6 = Art_banda('Scorpions', 'Rock', 'Banda', 9909243, 944481, 3876921.97)
conta7 = Art_banda('Lil Lil Sabotage', 'Hip hop', 'Solo', 8004184, 613817, 1029655.49)
conta8 = Art_banda('Lipa Ariana', 'Pop', 'Solo', 12779590, 376521, 8301531.80)
conta9 = Art_banda('Orange John', 'Indie', 'Solo', 918835, 198124, 1607389.37)
conta10 = Art_banda('Akon Jay', 'Hip hop', 'Solo', 1674022, 881508, 9841351.47)
conta11 = Art_banda('Selena', 'Pop', 'Solo', 1572943, 1082097, 11755367.58)
conta12 = Art_banda('Leci Lara', 'Samba', 'Solo', 2756880, 227962, 2300020.09)
conta13 = Art_banda('The Police', 'Rock', 'Banda', 15546122, 1208054, 12274035.58)
conta14 = Art_banda('Bambo Chainsmoker', 'Eletrônica', 'Solo', 2206112, 87073, 3136718.18)
conta15 = Art_banda('Ariana Selena', 'Pop', 'Solo', 9198171, 129738, 9736476.13)
conta16 = Art_banda('MC x9', 'Funk', 'Solo', 3048445, 375965, 3668836.35)
conta17 = Art_banda('DJ Walk', 'Eletrônica', 'Solo', 3445709, 67971, 673823.63)
conta18 = Art_banda('Book Sean', 'Hip hop', 'Solo', 5156167, 700955, 5791401.86)
conta19 = Art_banda('Noel Washington', 'Samba', 'Solo', 799459, 206211, 2478700.50)
conta20 = Art_banda('Rex Johnes', 'Indie', 'Solo', 2166481, 237271, 1450743.42)


playlist = [conta1, conta2, conta3, conta4, conta5, conta6, conta7, conta8, conta9, conta10, conta11, conta12, conta13,
conta14, conta15, conta16, conta17, conta18, conta19, conta20]
playlist_geral = Playlist(playlist)

for contas in playlist_geral:
    print(contas.sortear())

# print(len(playlist_geral))

# for artista_banda in playlist_geral:
#     print(artista_banda)