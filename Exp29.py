menu_option="enter 'a' to add songs,'s' to see songs,'f' to find songs by title,'q' to quit songs :"
songs=[]
def add_songs():
    title=input('enter your song: ')
    singer=input('enter your singer: ')
    year=input('enter release year: ')
    songs.append({'Title':title,'Singer':singer,'Year':year})
def show_songs():
    for song in songs:
        print(song['Title'])
        print(song['Singer'])
        print(song['Year'])
def find_songs():
    search_title=input('Enter songs you are looking for : ')
    for song in songs:
        if song['Title']==search_title:
           print(song['Title'])
           print(song['Singer'])
           print(song['Year']) 
user_option={'a':add_songs,'s':show_songs,'f':find_songs}
def menu():
    selection=input(menu_option)
    while selection!='q':
        if selection in user_option:
            selection_function=user_option[selection]
            selection_function()
        else:
            print('you entered wrong input')
        selection=input(menu_option)
menu()        
