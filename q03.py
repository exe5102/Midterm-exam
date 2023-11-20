from pkg.modu import print_json, process_data, read_json, write_json

MENU_FILE = "menu.json"  # 輸入檔案名稱
OUTPUT_FILE = "output.json"  # 輸出檔案名稱

pi_dict = read_json(MENU_FILE)
print_json(pi_dict)

pi_dict["categories"][1]["items"].append(
    {"name": "海鮮燉飯", "price": 239, "description": "西班牙的代表美食，海鮮配料豐富、色彩繽紛"}
)
discount = input("請輸入折扣率(0.0 ~ 1.0):")
process_data(pi_dict, discount)

write_json(pi_dict, OUTPUT_FILE)
print_json(pi_dict)
