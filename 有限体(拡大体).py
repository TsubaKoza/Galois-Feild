def generate_p2v(p, primitive_polynomial, m):
    vec = [1] + [0] * m  # 初期ベクトル（仮に [1, 0, ..., 0] とする）
    max_exponent = p ** m - 1  # 最大の指数（p^m - 1）

    # p2v の初期化：インデックスの数だけリストを用意
    p2v = [-1] * (max_exponent + 1)  # 初期値を -1 に設定（未定義のため）

    # ベクトルを生成してp2vの値を埋める
    for exponent in range(max_exponent + 1):
        # 現在のベクトルを用いて10進数値を計算
        decimal_value = sum(vec[i] * (p ** i) for i in range(m))
        
        # p2v の対応するインデックスに値を設定
        if p2v[decimal_value] == -1:  # 初めて出る値のときに設定
            p2v[decimal_value] = exponent

        # 次のべきに進むためベクトルを更新
        vec = [0] + vec[:-1]  # 右に1ビットシフト

        # 原始多項式を使って修正
        if vec[-1] != 0:
            multiplier = vec[-1]
            vec = [(vec[i] - multiplier * primitive_polynomial[i]) % p for i in range(m + 1)]

    return p2v

def generate_v2p(p2v):
    # v2p は p2v の逆を取る
    v2p = [-1] * len(p2v)  # 初期化
    for exponent, value in enumerate(p2v):
        if value != -1:
            v2p[value] = exponent
    return v2p

def generate_primitive_table(p, primitive_polynomial, m):
    vec = [1] + [0] * m  # 初期ベクトル（仮に [1, 0, ..., 0] とする）
    table = []

    # ベクトルを生成して表を埋める
    for exponent in range(p ** m):
        # 現在のベクトルを用いて10進数値を計算
        decimal_value = sum(vec[i] * (p ** i) for i in range(m))

        # べき表現、対応する多項式係数、10進数表現を計算
        # 多項式係数を上位3ビットのみ表示
        polynomial_coefficients = vec[:3]  # 上位3ビットの係数を使用
        table.append({
            '指数表現': exponent,
            'べき表現': f"α^{exponent}",
            '多項式係数': ''.join(map(str, polynomial_coefficients)),
            '10進数表現': decimal_value
        })

        # 次のべきに進むためベクトルを更新
        vec = [0] + vec[:-1]  # 右に1ビットシフト

        # 原始多項式を使って修正
        if vec[-1] != 0:
            multiplier = vec[-1]
            vec = [(vec[i] - multiplier * primitive_polynomial[i]) % p for i in range(m + 1)]

    return table

# ユーザー入力
p = int(input("Enter a prime number (p): "))
primitive_polynomial_input = input("Enter the coefficients of the primitive polynomial (from highest degree to lowest, space-separated): ")
primitive_polynomial = list(map(int, primitive_polynomial_input.split()))
m = len(primitive_polynomial) - 1

# 原始多項式のテーブルを生成
table = generate_primitive_table(p, primitive_polynomial, m)

# p2vを生成
p2v = generate_p2v(p, primitive_polynomial, m)

# v2pを生成
v2p = generate_v2p(p2v)

# 原始多項式表の出力
print("\n指数表現    べき表現      多項式係数               10進数表現")
print("------------------------------------------------------------")
for row in table:
    print(f"{row['指数表現']: <8} {row['べき表現']: <14} {row['多項式係数']: <15} {row['10進数表現']}")

# p2v と v2p の表の出力
print("\n指数表現   ", " ".join(str(i) for i in range(len(p2v))))
print("p2v        ", " ".join(str(v2p[i]) for i in range(len(v2p))))
print("v2p        ", " ".join(str(p2v[i]) if p2v[i] != -1 else "-" for i in range(len(p2v))))