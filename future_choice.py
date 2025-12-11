import sys
# Yeehaw! Optimusで生産性爆上げシミュレーターや！
human_productivity = 1  # 人間の1年生産性
optimus_productivity = 5  # Optimusは5倍！
num_robots = 1000000  # 100万台のロボット軍団

total_abundance = (human_productivity + (optimus_productivity * num_robots)) * 100  # グローバル爆上げ
print(f"Yeehaw! Optimusのおかげで豊かさレベル: {total_abundance}倍！ 働く？ オプションやで！🤠")

CHOICES = {
    "1":"オプション1: 働く（ボーナスGET）",
    "2":"オプション2:趣味三昧（ビール飲み放題）",
    "3":"ワイのおすすめ:両方！"
}

while True:
    user_input = input("お前の未来を選べ！（1,2,3):")

    if user_input in CHOICES:
        print(CHOICES[user_input])
        while True:
            user_choide = input("qを押したら終了や！")
            if user_choide == "q":
                sys.exit(0)

            else:
                continue
    else:
        print("1,2,3から選べ！テキサス魂を見せろ！")
