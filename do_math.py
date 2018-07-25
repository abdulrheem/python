import math

def isString(x):
    try:
        y = str(x)
        return True
    except ValueError:
        return False

def isInteger(x):
    try:
        y = int(x)
        return True
    except ValueError:
        return False
def isFloat(x):
    try:
        y = float(x)
        return True
    except ValueError:
        return False

cos_thita = 0
sin_thita = 0
tan_thita = 0

# Hypo part starst down here

hypo =  raw_input("is the hypotenous value known\n\tyes (Y) or (n) or (yes) or (no)")

while hypo.lower() != "n" and hypo.lower() != "y" and hypo.lower() != "yes" and hypo.lower() != "no":
    hypo = (raw_input("use y, n, yes, or no for your answer"))          # This is for user restrictment to certain choices
                                                                                                
if hypo.lower() == "y" or hypo.lower() == "yes":
    hypo = raw_input("Enter its value")
    while isFloat(hypo) == False and isInteger(hypo) == False:
        hypo = raw_input("Numbers Please!!")
    hypo = float(hypo)
else:
    hypo = "Unknown"

# Hypotenous part end up there

# Adjecant Side part down

adje_side =  raw_input("is the adjecant side value known?\n\tyse (Y) or (n) or (yes) or (no)")

while adje_side.lower() != "n" and adje_side.lower() != "y" and adje_side.lower() != "yes" and adje_side.lower() != "no":
    adje_side = (raw_input("use y, n, yes, or no for your answer"))

if adje_side.lower() == "y" or adje_side.lower() == "yes":
    adje_side = raw_input("Enter its value")
    while isFloat(adje_side) == False and isInteger(adje_side) == False:
        adje_side = raw_input("Numbers Please!!")
    adje_side = float(adje_side)
else:
    adje_side = "Unknown"

#adje_side part above

# oppo_side part down

oppo_side =  raw_input("is the opposite side value known?\n\tyse (Y) or (n) or (yes) or (no)")

while oppo_side.lower() != "n" and oppo_side.lower() != "y" and oppo_side.lower() != "yes" and oppo_side.lower() != "no":
    oppo_side = (raw_input("use y, n, yes, or no for your answer"))

if oppo_side.lower() == "y" or oppo_side.lower() == "yes":
    oppo_side = raw_input("Enter its value")
    while isFloat(oppo_side) == False and isInteger(oppo_side) == False:
        oppo_side = raw_input("Numbers Please!!!")
    oppo_side = float(oppo_side)
else:
    oppo_side = "Unknown"

if (isFloat(hypo) == True or isInteger(hypo) == True) and (isFloat(adje_side) == True or isInteger(adje_side) == True):
    cos_thita = float(adje_side/hypo)
    print "Cosine of thita is:\n" + str(cos_thita)
else:
    cos_thita = "nothing"

if(isFloat(hypo) == True or isInteger(hypo) == True) and (isFloat(oppo_side) == True or isInteger(oppo_side) == True):
    sin_thita =float(oppo_side/hypo)
    print "sine of thita is:\n" + str(sin_thita)
else:
    sin_thita = "nothing"

if (isFloat(oppo_side) == True or isInteger(oppo_side) == True) and (isFloat(adje_side) == True or isInteger(adje_side) == True):
    tan_thita = oppo_side/adje_side
    print "Tangent of thita is:\n" + str(tan_thita)
else:
    tan_thita == "nothing"

# Opposite side part is up above

thita =  raw_input("is the angle (thita) value known?\n\tuse (Y) or (n) or (yes) or (no)")

while thita.lower() != "n" and thita.lower() != "y" and thita.lower() != "yes" and thita.lower() != "no":
    thita = (raw_input("use y, n, yes, or no for your answer"))

if thita.lower() == "y" or thita.lower() == "yes":
    thita = raw_input("Enter its value max value is 90 degree")
    while isFloat(thita) == False and isInteger(thita) == False:
        thita = raw_input("Numbers Please!!!")
    while math.fabs(float(thita)) > 90:
        thita = raw_input("The absolute value of thita should be less than 90")
    thita = float(thita)

    tan_thita = math.tan(math.radians(float(thita)))
    cos_thita = math.cos(math.radians(float(thita)))
    sin_thita = math.sin(math.radians(float(thita)))

else:
  thita = 0

if(isFloat(oppo_side) == False or isInteger(oppo_side) == False) and (isFloat(hypo) == True or isInteger(hypo) == True) and 0 < math.fabs(float(thita)) < 90:
    oppo_side =  float(hypo) * math.sin(math.radians(float(thita)))

print "the opposite side is " + str(oppo_side)

if (isFloat(adje_side) == False or isInteger(adje_side) == False) and (isFloat(hypo) == True or isInteger(hypo) == True) and 0 < math.fabs(float(thita)) < 90:
    adje_side =  float(hypo) * math.cos(float(thita))

print "The adjecant side is " + str(adje_side)

if (isFloat(adje_side) == True or isInteger(adje_side) == True) and (isFloat(oppo_side) == True or isInteger(oppo_side) == True) and (isFloat(hypo) == False and isInteger(hypo) == False):
    hypo = math.sqrt(adje_side**2 + oppo_side **2)

print "The Hypotenouas is: " + str(hypo)


if thita == 0 and (isFloat(adje_side) == True or isInteger(adje_side) == True) and (isFloat(hypo) == True or isInteger(hypo) == True):
    thita = math.acos(adje_side/hypo)
    thita = math.degrees(thita)
    print "the angle is :\n" + str(thita)
    oppo_side =  math.sqrt(float(hypo**2 - adje_side**2))
    print "The opposite side is: " + str(oppo_side)


if thita == 0 and (isFloat(oppo_side) == True or isInteger(oppo_side) == True) and (isFloat(hypo) == True or isInteger(hypo) == True):
    thita = math.asin(oppo_side/hypo)
    thita = math.degrees(thita)
    print "the angle is :\n" + str(thita)
    adje_side = math.sqrt(float(hypo**2 - oppo_side**2))
    print "The adjecant side is: " + str(adje_side)

if thita == 0 and (isFloat(oppo_side) == True or isInteger(oppo_side) == True) and (isFloat(adje_side) == True or isInteger(adje_side) == True):
    thita = math.atan(oppo_side/adje_side)
    thita = math.degrees(thita)
    print "the angle is :\n" + str(thita)

tan_thita = math.tan(math.radians(float(thita)))
cos_thita = math.cos(math.radians(float(thita)))
sin_thita = math.sin(math.radians(float(thita)))
                                                                
