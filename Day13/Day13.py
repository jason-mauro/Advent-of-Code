from sympy import symbols, Eq, solve
with open("../input.txt") as fin:
    lines = fin.read().splitlines()
    tokens = 0
    i = 0
    while i < len(lines):
        # Process A
        a = lines[i].split()
        ax = int(a[2][2:len(a[2])- 1])
        ay = int(a[3][2:len(a[3])])
        i += 1
        # Process B
        b = lines[i].split()
        bx = int(b[2][2:len(b[2])- 1])
        by = int(b[3][2:])
        i += 1
        #Process Prize
        p = lines[i].split()
        px = int(p[1][2:len(p[1]) -1]) + 10_000_000_000_000
        py = int(p[2][2:]) + 10_000_000_000_000
        i += 1
        # Calulate
      
        
        
        # Define integer variables for sympy
        a_sym, b_sym = symbols('a b', integer=True)
        eq1 = Eq(a_sym * ax + b_sym * bx, px)
        eq2 = Eq(a_sym * ay + b_sym * by, py)

        # Solve for integer solutions
        sol = solve((eq1, eq2), (a_sym, b_sym), dict=True)

        if sol:
            a_val, b_val = sol[0][a_sym], sol[0][b_sym]
            tokens += 3 * a_val + b_val

        i += 1
        # skip line
    print(tokens)