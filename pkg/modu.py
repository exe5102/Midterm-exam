import json  # 載入json模組


def triangle_zhonxin(a: tuple, b: tuple, c: tuple) -> tuple:  # 儲存重心座標
    """根據傳入的三個頂點坐標，計算三角形的重心坐標並回傳"""
    x = round((a[0] + b[0] + c[0]) / 3)  # 計算重心x座標
    y = round((a[1] + b[1] + c[1]) / 3)  # 計算重心y座標
    return (x, y)  # 回傳 tuple 型態


def read_json(file_name: str) -> dict:  # 將 json 檔案轉為字典後回傳
    """將 json 檔案轉為字典後回傳"""
    with open(file_name, "r", encoding="UTF-8") as f:
        # json.load() 讀取 JSON 檔案，轉換為 Python 的 dict
        return json.load(f)


def print_json(data: dict) -> None:  # 將字典轉爲 json 字串後輸出到螢幕
    """將字典轉爲 json 字串後輸出到螢幕"""
    # 生成的 JSON 字符串和文件中的內容將保留非ASCII字符和縮排
    new_pi_str = json.dumps(data, ensure_ascii=False, indent=4)
    print(new_pi_str)

# 將字典中每個菜品的價格打discount折扣


def process_data(data: dict, discount: float) -> None:
    """將字典中每個菜品的價格打discount 折數"""
    # 找出每個類別（categories）中的每個項目（items）
    for category in data["categories"]:
        for item in category["items"]:
            # 將每個項目的價格應用折扣
            item["price"] = round(item["price"] * float(discount))


def write_json(data: dict, file_name: str) -> None:
    """將字典轉為檔案"""
    with open(file_name, "w", encoding="utf-8") as f:
        # json.dump() 將 dict 轉成 JSON 格式，寫入 JSON 檔案，並且保留非ASCII字符和縮排
        json.dump(data, f, ensure_ascii=False, indent=4)
