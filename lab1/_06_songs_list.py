violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]
time = 0
for song in violator_songs_list:
    if song[0] == 'Halo' or song[0] == 'Enjoy the Silence' or song[0] == 'Clean':
        time += song[1]
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}
time2 = 0
for song in violator_songs_dict.keys():
    if song == 'Sweetest Perfection':
        time2 += violator_songs_dict['Sweetest Perfection']
    if song == 'Policy of Truth':
        time2 += violator_songs_dict['Policy of Truth']
    if song == 'Blue Dress':
        time2 += violator_songs_dict['Blue Dress']


def answer():
    print(f'Три песни звучат {round(time, 2)} минут')
    print(f'А другие три песни звучат {round(time2, 2)} минут')


if __name__ == "__main__":
    answer()
