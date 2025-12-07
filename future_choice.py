# Yeehaw! Optimusで生産性爆上げシミュレーターや！
human_productivity = 1  # 人間の1年生産性
optimus_productivity = 5  # Optimusは5倍！
num_robots = 1000000  # 100万台のロボット軍団

total_abundance = (human_productivity + (optimus_productivity * num_robots)) * 100  # グローバル爆上げ
print(f"Yeehaw! Optimusのおかげで豊かさレベル: {total_abundance}倍！ 働く？ オプションやで！🤠")

# 未来の選択肢関数
def future_map_one():
    return ("オプション1: 働く（ボーナスGET）")

def future_map_two():
    return ("オプション2:趣味三昧（ビール飲み放題）")

def future_map_three():
    return ("ワイのおすすめ:両方！")

future_choice = {
    "1":future_map_one,
    "2":future_map_two,
    "3":future_map_three
}
user_input = input("お前の未来を選べ！(1,2,3):")

result = future_choice.get(user_input)

print(result())