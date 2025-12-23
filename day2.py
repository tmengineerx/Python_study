#顧客名と受注確立(%)のリスト
customers = [["A社",80],["B社",30],["C社",100],["D社",10]]

for customer in customers:
    name = customer[0]
    chance = customer[1]
    if chance >= 50:
        print (f"{name}様：至急アプローチ！")
    else:
        print(f"{name}様：時期尚早")

        # リストの長さを測る len 関数を使ってみる
print(f"本日のアプローチ件数：{len(customers)}件")