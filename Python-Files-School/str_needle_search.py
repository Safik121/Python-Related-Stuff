def search(needle, haystack):
    x = -1
    for i in range(0, len(haystack)):
        if needle == haystack[i:i + len(needle)]:
            x = i
            break
    return x

print(search("tri", "bratri"))
