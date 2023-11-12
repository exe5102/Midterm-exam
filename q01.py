from pkg.modu import triangle_zhonxin as m  # 載入套件

Line = "------------------------------"
vertex = {}

print(f"請輸入三角形的 3 個頂點坐標\n{Line}")

#   三頂點座標輸入
for key in ["a", "b", "c"]:
    coordinates = tuple(
        int(coord) for coord in input(f"請輸入頂點 {key} 的座標:").split(","))
    vertex[key] = coordinates

#   以套件回傳值輸出
center = m(vertex["a"], vertex["b"], vertex["c"])
print(f"{Line}\n此三角形的重心為：{center}")
