from datetime import datetime
lf = "log.txt"

msg = input()
log = "{:%y-%m-%d %H:%M:%S} {}".format(datetime.today(),msg)

print("confirm the msg yes/no")
confirmation = input().strip()
while confirmation not in ("yes","no"):
    print("confirm the msg yes/no")
    confirmation = input().strip()


def addlog(log):
    with open(lf,'a',encoding="utf-8") as tf:
        tf.write(f"{log}\n")
        print("message ajouté au journal")


if confirmation == "yes":
    addlog(log)
else :
    exit(0)