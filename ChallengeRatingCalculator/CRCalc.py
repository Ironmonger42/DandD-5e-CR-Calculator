import sqlite3


def find_cr_from_hp(hit_points):

    db = sqlite3.connect("CRTable.sqlite")
    cursor = db.cursor()

    found = False
    challenge_rating = 0
    min_num = 0
    max_num = 1

    while found is False and challenge_rating <= 30:
        execute_statement = "select HitPointMin, HitPointMax from CRTable where CR={}".format(challenge_rating)
        cursor.execute(execute_statement)
        for HitPointMin, HitPointMax in cursor:
            min_num = HitPointMin
            max_num = HitPointMax
        if min_num - 1 < hit_points < max_num + 1:
            found = True
        elif challenge_rating is 0:
            challenge_rating = 0.125
        elif challenge_rating is 0.125:
            challenge_rating = 0.25
        elif challenge_rating is 0.25:
            challenge_rating = 0.5
        elif challenge_rating is 0.5:
            challenge_rating = 1
        else:
            challenge_rating = challenge_rating + 1

    cursor.connection.close()
    db.close()

    return challenge_rating


def adjust_cr_from_ac(challenge_rating, effective_ac):

    db = sqlite3.connect("CRTable.sqlite")
    cursor = db.cursor()

    cursor.execute("select AC from CRTable where CR={}".format(challenge_rating))

    armor = 0

    for AC in cursor:
        armor = AC

    if armor[0] < effective_ac:
        adjust_val = ((effective_ac - armor[0]) // 2)
    elif armor[0] > effective_ac:
        adjust_val = ((armor[0] - effective_ac) // 2)
    else:
        adjust_val = 0

    while adjust_val > 0:
        if effective_ac > armor[0]:  # challenge rating is increasing
            if challenge_rating >= 1:
                challenge_rating = challenge_rating + 1
            elif challenge_rating == 0.5:
                challenge_rating = 1
            elif challenge_rating == 0.25:
                challenge_rating = 0.5
            elif challenge_rating == 0.125:
                challenge_rating = 0.25
            else:
                challenge_rating = 0.125
        if armor[0] > effective_ac:  # challenge rating is decreasing
            if challenge_rating > 1:
                challenge_rating = challenge_rating - 1
            elif challenge_rating == 1:
                challenge_rating = 0.5
            elif challenge_rating == 0.5:
                challenge_rating = 0.25
            elif challenge_rating == 0.25:
                challenge_rating = 0.125
            elif challenge_rating == 0.125:
                challenge_rating = 0
            else:
                challenge_rating = 0
        adjust_val = adjust_val - 1

    cursor.connection.close()
    db.close()

    return challenge_rating


def find_cr_from_dmg(avg_dmg):

    db = sqlite3.connect("CRTable.sqlite")
    cursor = db.cursor()

    found = False
    challenge_rating = 0
    min_num = 0
    max_num = 1

    while found is False and challenge_rating <= 30:
        execute_statement = "select AvgDmgMin, AvgDmgMax from CRTable where CR={}".format(challenge_rating)
        cursor.execute(execute_statement)
        for AvgDmgMin, AvgDmgMax in cursor:
            min_num = AvgDmgMin
            max_num = AvgDmgMax
        if min_num - 1 < avg_dmg < max_num + 1:
            found = True
        elif challenge_rating is 0:
            challenge_rating = 0.125
        elif challenge_rating is 0.125:
            challenge_rating = 0.25
        elif challenge_rating is 0.25:
            challenge_rating = 0.5
        elif challenge_rating is 0.5:
            challenge_rating = 1
        else:
            challenge_rating = challenge_rating + 1

    cursor.connection.close()
    db.close()

    return challenge_rating


def adjust_cr_from_atk(challenge_rating, effective_atk):

    db = sqlite3.connect("CRTable.sqlite")
    cursor = db.cursor()

    cursor.execute("select ATKbonu from CRTable where CR={}".format(challenge_rating))

    atk = 0

    for ATKbonu in cursor:
        atk = ATKbonu

    if atk[0] < effective_atk:
        adjust_val = ((effective_atk - atk[0]) // 2)
    elif atk[0] > effective_atk:
        adjust_val = ((atk[0] - effective_atk) // 2)
    else:
        adjust_val = 0

    while adjust_val > 0:
        if effective_atk > atk[0]:  # challenge rating is increasing
            if challenge_rating >= 1:
                challenge_rating = challenge_rating + 1
            elif challenge_rating == 0.5:
                challenge_rating = 1
            elif challenge_rating == 0.25:
                challenge_rating = 0.5
            elif challenge_rating == 0.125:
                challenge_rating = 0.25
            else:
                challenge_rating = 0.125
        if atk[0] > effective_atk:  # challenge rating is decreasing
            if challenge_rating > 1:
                challenge_rating = challenge_rating - 1
            elif challenge_rating == 1:
                challenge_rating = 0.5
            elif challenge_rating == 0.5:
                challenge_rating = 0.25
            elif challenge_rating == 0.25:
                challenge_rating = 0.125
            elif challenge_rating == 0.125:
                challenge_rating = 0
            else:
                challenge_rating = 0
        adjust_val = adjust_val - 1

    cursor.connection.close()
    db.close()

    return challenge_rating


def calc_cr(avg_hp, eff_ac, avg_dmg, eff_atk):
    cr_from_hp = find_cr_from_hp(avg_hp)
    def_cr = adjust_cr_from_ac(cr_from_hp, eff_ac)
    cr_from_dmg = find_cr_from_dmg(avg_dmg)
    off_cr = adjust_cr_from_atk(cr_from_dmg, eff_atk)
    final_cr = (def_cr + off_cr + (def_cr % off_cr)) // 2
    return final_cr


hp = float(input("HP: "))

while hp < 0 or hp > 850:
    hp = float(input("HP must be an integer between 0 and 850: "))

ac = float(input("AC: "))

while ac < 0 or ac > 30:
    ac = float(input("AC must be an integer between 0 and 30: "))

dmg = float(input("DMG: "))

while dmg < 0 or dmg > 320:
    dmg = float(input("DMG must be an integer between 0 and 320: "))

hit = float(input("Hit: "))

while hit < 0 or hit > 30:
    hit = float(input("Hit must be an integer between 0 and 30: "))


cr = int(calc_cr(hp, ac, dmg, hit))
print("CR: {}".format(cr))
