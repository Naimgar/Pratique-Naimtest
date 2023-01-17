ch="  salut tout le monde "


print(len(ch))
ch1=ch.strip()
print(ch1)
print(ch1.strip())
print(len(ch1))


ch2=ch.lstrip()
print(ch2)
print(len(ch2))

ch3=ch.rsplit()
print(ch3)
print(len(ch3))

ch4="***salut***tout***le***monde***"
print(ch4)
ch5=ch4.strip("*")
print(ch5)
print(len(ch5))

print(ch4.replace("*"," "))

ch6="  salut tout le monde le monde le monde"
print(ch6.count("monde"))
print(ch6.endswith("monde"))
print(ch6.startswith("monde"))
ch8="un-deux-trois-quatre-cinq-six-sept-huit-neuf-dix"
print(ch8.split("-"))

