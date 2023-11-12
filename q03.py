from pkg.modu import print_json, process_data, read_json, write_json

pi_dict = read_json()
print_json(pi_dict)

pi_dict["categories"][1]["items"].append({
    "name": "海鮮燉飯",
    "price": 239,
    "description": "西班牙的代表美食，海鮮配料豐富、色彩繽紛"
    })

data = process_data(pi_dict)

write_json(data)
print_json(data)
