"""
Cats and a MouseTwo 
cats and a mouse are at various positions on a line. You will be given their starting positions. Your task is to determine which cat will reach the mouse first, assuming the mouse does not move and the cats travel at equal speed. If the cats arrive at the same time, the mouse will be allowed to move and it will escape while they fight.You are given $q$ queries in the form of $x$, $y$, and $z$ representing the respective positions for cats $A$ and $B$, and for mouse $C$. Complete the function to return the appropriate answer to each query, which will be printed on a new line.If cat $A$ catches the mouse first, print Cat A.If cat $B$ catches the mouse first, print Cat B.   If both cats reach the mouse at the same time, print Mouse C as the two cats fight and mouse escapes.   Input Format   The first line contains a single integer, $q$, denoting the number of queries.Each of the $q$ subsequent lines contains three space-separated integers describing the respective values of $x$ (cat A's location), $y$ (cat B's location), and $z$ (mouse C's location).   Constraints   $1 \le q \le 100$$1 \le x, y, z \le 100$Output Format   For each query, return Cat A if cat $A$ catches the mouse first, Cat B if cat $B$ catches the mouse first, or Mouse C if the mouse escapes.   Sample InputPlaintext2
1 2 3
1 3 2
Sample OutputPlaintextCat B
Mouse C

"""
def catAndMouse(x, y, z):
    r=None
    if abs(z-x)==abs(z-y):
        r=('Mouse C')
    elif abs(z-x)>abs(z-y):
        r=('Cat B')
    else:
        r= ('Cat A')
    return r