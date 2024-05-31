def screwing(n):
    if n == 0:
        return
    print("Screwing")
    screwing(n-1)

screwing(3)
