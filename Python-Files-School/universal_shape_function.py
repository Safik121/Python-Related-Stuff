import turtle

t = turtle

def obecna_funkce(pocet_stran, delka_strany, smer, uhel):
    for i in range(pocet_stran):
        t.forward(delka_strany)
        smer(uhel)

obecna_funkce(5, 100, t.left, 72)
