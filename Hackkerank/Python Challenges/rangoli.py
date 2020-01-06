alph = 'abcdefghijklmnopqrstuvwxyz'
def rangoli_V3(N):
    width = 4*(N - 1) + 1
    A = list(alph[:N])
    rA = list(reversed(A))
    all_rows = []
    for i in range(N):
        thisrow = rA[:i+1] + A[N-i:]
        all_rows.append("-".join(thisrow).center(width,"-"))
    all_rows =  all_rows + list(reversed(all_rows[:-1]))
    complete_string = "\n".join(all_rows)
    print(complete_string)

rangoli_V3(26)
