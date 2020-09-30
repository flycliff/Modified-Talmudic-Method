import math as m


def printR(R, C, E, r):
    claimants = ['Wells Fargo', ' unsecured ', '    AGA    ', "", "", ""]
    if round(sum(R[i] for i in range(len(R))), 2) != round(E, 2):
        print("\tError calculating payouts")
        print("\t", E, "vs", sum(R[i] for i in range(len(R))))
    else:
        for i in range(r):
            print("\tC" + str(i + 1), "("+ claimants[i] +")",  "receives:", '${:,.2f}'.format(round(R[i], 2)), 'of', '${:,.2f}'.format(round(C[i], 2)), 'claimed')

def PropApp(C, E, r):
    SumC = sum([C[i] for i in range(r)])
    R = [(C[i] / SumC) * E for i in range(r)]
    return R

def Talmud_Mod(C, W, E, r):
    R = [0 for _ in range(r)]

    number_of_phases = m.ceil(1 / min(W))
    E_remaining = E

    for phase in range(number_of_phases):
        print("phase", phase, end=": ")
        caps = [C[i]*W[i] if R[i] < C[i] else 0 for i in range(r)]

        if E_remaining <= 0:                # base case
            print("Base Case:\t  ", '${:,.2f}'.format(round(sum(R), 2)))
            break
        elif E_remaining >= sum(caps):      # pay out the interval, go to the next
            for i in range(r):
                R[i] += caps[i]
            E_remaining -= sum(caps)
            print("Interval cleared:", '${:,.2f}'.format(round(sum(R), 2)))
        else:                               # last interval before we run out of money
            prop = PropApp(caps, E_remaining, r)
            for i in range(r):
                R[i] += prop[i]
            E_remaining = 0
            print("Last Interval:   ", '${:,.2f}'.format(round(sum(R), 2)))
    print("\nModified Talmud Method - Weights:", [round(w, 2) for w in W])
    printR(R, C, E, r)
            

def main():
    #   ['Wells Fargo', 'unsecured debt', 'Amer. Greet. Agreement']
    C = [6675160, 8000000, 38706673]
    E = 39400000
    r = len(C)

    W = [0.15, 0.45, 0.40]
    #W = [0.25, 0.5, 0.25]
    #W = [0.2, 0.4, 0.33]
    #W = [C[i]/sum(C) for i in range(r)]
    #W = [1/r for _ in range(r)]

    assert sum(W) == 1
    Talmud_Mod(C, W, E, r)

main()
