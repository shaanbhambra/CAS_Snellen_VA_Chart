# -*- coding: utf-8 -*-

import math, random
from string import ascii_uppercase, Template

# 1 meter in inches.
meter = 39.37008

# Now convert to points (using 1 in = 72 pt).
meter *= 72

# 5 arc minutes in radians.
theta = (2 * math.pi / 360 / 60) * 5

# Standard distances (in m).
# distances = [60, 36, 30, 24, 18, 12, 6, 5, 4]
distances = [60,30.48,21.336,15.24,12.192,9.144,7.62,6.096,4.572,3.9624,3.048]

# Optotypes to use.
# optotypes = list(ascii_uppercase)
# optotypes = list("CDEFHKLNOPRTUVZ") # standard Snellen optotypes
#optotypes = list("CDEFHKNPRUVZ") # standard Snellen optotypes
# optotypes=list("CDEFLOPTZ")
optotypes = list("ᐱᑎᑭᒧᒋᒥᑯᒧᔨ") # standard Snellen optotypes


# Number of optotypes for each distance.
glyphs = [1,2,3,4,5,6,7,8,8,8,9]

# TeX code templates.
t1 = Template(r"\deflen{$name}{$length$unit} % $dist m")
t2 = Template(r"\acuity{20/$feet}{6/$dist} & \optotype{\factor\$name}{$string} \\")

def randstring(length=1):
    """Return a random string of given length with no repeated letters."""
    random.shuffle(optotypes)
    return "".join(optotypes[:length])

print("\n% Length definitions")
for i, d in enumerate(distances):
    print(
        t1.substitute(
            name="Set" + ascii_uppercase[i],
            length=round(2 * d * math.tan(theta / 2) * meter, 0),
            unit="pt",
            dist=d
        )
    )

print("\n% Tables\n")
print(r"""\pagebreak
\begin{center}
\renewcommand*{\arraystretch}{3.5}
\begin{longtable}{rc}""")
for i, d in enumerate(distances):
    print(
        t2.substitute(
            dist=d,
            feet=int(d/6*20),
            name="Set" + ascii_uppercase[i],
            string=randstring(glyphs[i])
        )
    )
    if i == 4:
        print(r"& \colorrule{cyan}{0.65cm} \\")
    elif i == 6:
        print(r"& \colorrule{red}{0.65cm} \\")
print(r"""\end{longtable}
\end{center}""")
