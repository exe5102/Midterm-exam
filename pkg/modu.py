import json  # 載入json模組


MENU_FILE = "menu.json"  # 輸入檔案名稱
OUTPUT_FILE = "output.json"  # 輸出檔案名稱


def triangle_zhonxin(a, b, c):  # 儲存重心座標
    x = round((a[0] + b[0] + c[0]) / 3)  # 計算重心x座標
    y = round((a[1] + b[1] + c[1]) / 3)  # 計算重心y座標
    return (x, y)  # 回傳 tuple 型態


def print_json(pi_dict):  # 將字典轉爲 json 字串後輸出到螢幕
    # 生成的 JSON 字符串和文件中的內容將保留非ASCII字符和縮排
    new_pi_str = json.dumps(pi_dict, ensure_ascii=False, indent=4)
    print(new_pi_str)
    return 0


def process_data(pi_dict):  # 將字典中每個菜品的價格打discount折扣
    discount = input("請輸入折扣率(0.0 ~ 1.0):")
    # 找出每個類別（categories）中的每個項目（items）
    for category in pi_dict["categories"]:
        for item in category["items"]:
            # 將每個項目的價格應用折扣
            item["price"] = int(item["price"] * float(discount))
    return pi_dict


def read_json():  # 將 json 檔案轉為字典後回傳
    with open(MENU_FILE, "r", encoding="UTF-8") as f:
        # json.load() 讀取 JSON 檔案，轉換為 Python 的 dict
        pi_dict = json.load(f)
    return pi_dict


def write_json(pi_dict):  # 將字典轉為檔案
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        # json.dump() 將 dict 轉成 JSON 格式，寫入 JSON 檔案，並且保留非ASCII字符和縮排
        json.dump(pi_dict, f, ensure_ascii=False, indent=4)
    return 0
