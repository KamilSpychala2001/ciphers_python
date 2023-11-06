# 08/2022

def bruteforce_decoding(msg_in_func):
    for i in range(1,26):
        print("i: {}".format(i))
        print(decoding(msg_in_func, i))

def decoding(msg_in_func, offset):
    decr = []

    for i in msg_in_func:
        if not i.isalpha():
            decr.append(i)
            continue

        a = ord(i)

        a = a + offset

        if a > 122:
            dist_from_a = a % 123
            a = 97 + dist_from_a

        decr.append(chr(a))

    msg_back = ''.join(decr)
    return msg_back


def encoding(msg, offset):
    decr = []

    for i in msg:
        if not i.isalpha():
            decr.append(i)
            continue

        a = ord(i)
        a = a - offset

        if a < 97:
            dist_from_z = 96 % a
            a = 122 - dist_from_z

        decr.append(chr(a))

    msg_back = ''.join(decr)
    return msg_back

msg = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu " \
      "rqsa myjx jxu iqcu evviuj! "
msg_2 = "i like potato!"

msg_4 = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm " \
        "mh dxxi hnk fxlltzxl ltyx. "


print(decoding(msg, 10))
print(encoding(msg_2, 10))
print(decoding("jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.", 10))
print(decoding("bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!", 14))
#bruteforce_decoding(msg_4)
