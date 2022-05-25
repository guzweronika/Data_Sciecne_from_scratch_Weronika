"""
EN:
When two events E and F are independent, then by definition we have:
            P(E, F) = P(E)P(F)

If they are not necessarily independent (and if probability of F is not zero) the we define the probability of E "conditional on F" as:
            P(E|F) = P(E,F)/P(F)

Probability that E happens, given that we know that F happens as:
            P(E, F) = P(E|F)P(F)

When E and F are independent
            P(E|F) = P(E)

Mathematical ay of expressing that knowuing F occurewd gives us no additional information about whether E occured


-------------------------------------------------------------
PL:
Gdy dwa zdarzenia E i F są niezależne, to z definicji mamy:
            P(E, F) = P(E) P(F)

Jeśli niekoniecznie są one niezależne (i jeśli prawdopodobieństwo F nie jest zerowe) definiujemy prawdopodobieństwo E „uwarunkowane na F” jako:
            P(E|F) = P(E,F)/P(F)

Prawdopodobieństwo, że wydarzy się E, biorąc pod uwagę, że wiemy, że F wydarza się jako:
            P(E, F) = P(E|F)P(F)

Kiedy E i F są niezależne
            P(E|F) = P(E)

Matematyczne wyrażenie, że wiedza o wystąpieniu F nie daje nam żadnych dodatkowych informacji o tym, czy wystąpiło E
"""
import random

#################### Conditional probability

def random_kid():
    return random.choice(["boy", "girl"])

both_girls = 0
older_girl = 0
either_girl = 0

random.seed(0)
for i in range(100000):
    younger = random_kid()
    older = random_kid()
    if older == "girl":
        older_girl += 1
    if older == "girl" and younger == "girl":
        both_girls += 1
    if older == "girl" or younger == "girl":
        either_girl += 1

print(f"P(both | older): {both_girls/older_girl:.2f}")      # ~0.50    ~1/2
print(f"P(both | either): {both_girls/either_girl:.2f}")    # ~0.33    ~1/3


#################### Bayes's Theorem - reverser conditional probability

"""
EN:
Bayes's Theorem - when we need to know probability of some event E conditional on some other event F occurring.

PL:
Twierdzenie Bayesa - gdy musimy znać prawdopodobieństwo pewnego zdarzenia E warunkowego podczas innego zdarzenia F.

            P(E|F) = P(E,F)/P(F) = P(E|F)P(E)/P(F)

EN:
The event F can be split into the two mutually exclusive events 'F and E' and 'F and not E'. If not E (i.e. 'E doesn't happen') then:

            P(E|F) = P(F|E)P(E)/[P(F|E)P(E)+P(F|not E)P(not E)]
"""


"""
EXAMPLE:

Certain disease that affects 1 in every 10000.
test for this disease that give the correct result ('disease' if you have the disease, 'non-disesese' if you don't) 99% ot the time.
T - positive test
D - disease
            P(D|T) = P(T|D)P(D)/[P(T|D)P(D) + P(T|not D)P(not D)]
            
P(T|D) - the probability that someone with the disease tests positive, is 0.99
P(D) - the probability that any given person has the disease is 1/10000 = 0.0001
P(T|not D) - the probability that someone without the disease test positive is 0.01
P(not D) - the probability that any given person doesn't have disease is 0.9999

        P(D|T) = 0.99 * 0.0001/ [0.99 * 0.0001 + 0.01 * 0.9999] -> 0.000099 / [0.000099 + 0.009999] -> 0.000099 / 0.010089 -> ~ 0.0098
        P(D|T) = 0.98 %   
"""
