from datetime import datetime
import datetime


def rand_list(text, sep):
    try:
        nbr_rand = 0
        split_s = text.split(sep)
        while len(split_s) > 0:
            time = datetime.datetime.now()
            nb_b = int(time.strftime("%S"))
            nb_a = int(time.strftime("%f"))
            nbr_rand = (nb_a * nbr_rand + nb_b) % len(split_s)
            yield str(split_s[nbr_rand])
            split_s.remove(split_s[nbr_rand])
    except ValueError:
        print("ERROR")
        quit()


def unique(text, sep):
    try:
        split_s = text.split(sep)
        split_s = list(dict.fromkeys(split_s))
        i = 0
        while len(split_s) > i:
            yield split_s[i]
            i += 1
    except ValueError:
        print("ERROR")
        quit()


def ordered(text, sep):
    try:
        split_s = text.split(sep)
        split_s = sorted(split_s, key=str.upper)
        i = 0
        while i < len(split_s):
            yield split_s[i]
            i += 1
    except ValueError:
        print("ERROR")
        quit()


def default(text, sep):
    try:
        split_s = text.split(sep)
        i = 0
        while i < len(split_s):
            yield split_s[i]
            i += 1
    except ValueError:
        print("ERROR")
        quit()


def generator(text, sep=" ", option=None):
    try:
        if isinstance(option, str):
            if len(option) == 0:
                print("Error of option")
                quit()
            elif option == "shuffle":
                return rand_list(text, sep)
            elif option == "unique":
                return unique(text, sep)
            elif option == "ordered":
                return ordered(text, sep)
            else:
                print("Error of option")
                quit()
        elif option is None:
            return default(text, sep)
        else:
            print("Error of option")
            quit()
    except ValueError:
        print("ERROR")
        quit()
