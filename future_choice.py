# Yeehaw! Optimusで生産性爆上げシミュレーターや！
human_productivity = 1  # 人間の1年生産性
optimus_productivity = 5  # Optimusは5倍！
num_robots = 1000000  # 100万台のロボット軍団

total_abundance = (human_productivity + (optimus_productivity * num_robots)) * 100  # グローバル爆上げ
print(f"Yeehaw! Optimusのおかげで豊かさレベル: {total_abundance}倍！ 働く？ オプションやで！🤠")

# 未来の選択肢関数
def future_choice():
    print("オプション1: 働く（ボーナスGET）")
    print("オプション2: 趣味三昧（ビール飲み放題）")
    print("ワイのオススメ: 両方！")

future_choice()
print("------------------------------------------")
future_choice()