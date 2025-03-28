class FiniteField:
    def __init__(self, p):
        self.p = p

    def pf_add(self, a, b):
        """ GF(p)で要素を加算する"""
        return (a + b) % self.p

    def pf_sub(self, a, b):
        """ GF(p)で要素を減算する"""
        return (a - b) % self.p

    def pf_mul(self, a, b):
        """ GF(p)で要素を乗算する"""
        return (a * b) % self.p

    def inverse(self, a):
        """ GF(p)での乗法逆元を求める(拡張ユークリッドの互除法)"""
        t, new_t = 0, 1
        s, new_s = 1, 0
        r, new_r = self.p, a
        while new_r != 0:
            q = r // new_r
            r, new_r = new_r, r - q * new_r
            s, new_s = new_s, s - q * new_s
            t, new_t = new_t, t - q * new_t
        if t < 0:
            t += self.p
        return t if r == 1 else None  # aが逆元を持つか確認

    def pf_div(self, a, b):
        """ GF(p)で要素を除算する(bの逆元をかける)"""
        inverse_b = self.inverse(b)
        if inverse_b is None:
            return None  # 除算が定義できない場合
        return self.pf_mul(a, inverse_b)

# テーブルを生成して表示する関数
def print_operation_table(operation, p):
    print("", end="")
    for i in range(p):
        print(f"{i:4}", end="")  # 列のヘッダー
    print()

    for i in range(p):
        print(f"{i:4}", end="")  # 行のヘッダー
        for j in range(p):
            result = operation(i, j)
            if result is None:
                print("- ", end="")
            else:
                print(f"{result:4}", end="")
        print()

# GF(p)の素数
p = 11
gf = FiniteField(p)

# 加算表
print("GF(p)の加算表:")
print_operation_table(gf.pf_add, p)

# 減算表
print("\nGF(p)の減算表:")
print_operation_table(gf.pf_sub, p)

# 乗算表
print("\nGF(p)の乗算表:")
print_operation_table(gf.pf_mul, p)

# 除算表
print("\nGF(p)の除算表:")
print_operation_table(gf.pf_div, p)
