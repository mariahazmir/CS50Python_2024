def main():
    list=[]
    while True:
        try:
            list.append(input().upper())
        except KeyError:
            pass
        except EOFError:
            if not list:
                break
            else:
                item_count(list)
                break


def item_count(list):
    sort = sorted(list)
    count = {}
    for item in sort:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    for item in count:
        print(f"{count[item]} {item}")

main()
