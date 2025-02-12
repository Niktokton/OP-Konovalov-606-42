secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]


def answer():
    print(secret_message[0][3], end=' ')
    print(secret_message[1][9:13], end=' ')
    print(secret_message[2][5:15:2], end=' ')
    print(secret_message[3][12:6:-1], end=' ')
    print(secret_message[4][20:15:-1])


if __name__ == "__main__":
    answer()
