import json
import random

# 定义一个函数来生成随机的JSON对象
def generate_random_json():
    return {
        "name": {
            "select": random.choice([True, False]),
            "aka": random.choice([True, False]),
            "part": random.choice([True, False]),
            "full": random.choice([True, False])
        },
        "phone": {
            "select": random.choice([True, False]),
            "total": str(random.choice([True, False])),
            "slice_len": {
                "select": random.choice([True, False]),
                "min": random.randint(2, 3),
                "max": random.randint(3, 6)
            }
        },
        "place": {
            "select": random.choice([True, False]),
            "aka": random.choice([True, False]),
            "part": random.choice([True, False]),
            "full": random.choice([True, False])
        },
        "addr": {
            "select": random.choice([True, False]),
            "aka": random.choice([True, False]),
            "part": random.choice([True, False]),
            "full": random.choice([True, False])
        },
        "door": {
            "select": random.choice([True, False]),
            "aka": random.choice([True, False]),
            "part": random.choice([True, False]),
            "full": random.choice([True, False])
        },
        "birth": {
            "select": random.choice([True, False]),
            "separat": {
                "Y": random.choice([True, False]),
                "M": random.choice([True, False]),
                "D": random.choice([True, False])
            },
            "combin": {
                "Y_M": random.choice([True, False]),
                "M_D": random.choice([True, False]),
                "Y_M_D": random.choice([True, False])
            }
        },
        "mail": {
            "select": random.choice([True, False]),
            "name": random.choice([True, False]),
            "domain": random.choice([True, False])
        },
        "slang": {
            "select": random.choice([True, False]),
            "aka": random.choice([True, False]),
            "part": random.choice([True, False]),
            "full": random.choice([True, False])
        },
        "random": {
            "select": random.choice([True, False]),
            "len": {
                "min": random.randint(2, 3),
                "max": random.randint(3, 6)
            }
        },
        "other": {
            "select": random.choice([True, False])
        },
        "extra_dic": {
            "select": random.choice([True, False])
        },
        "total_len": {
            "select": random.choice([True, False]),
            "range": {
                "max": random.randint(6, 10),
                "min": random.randint(10, 20)
            }
        }
    }

# 创建100个JSON文件
for i in range(1, 101):
    data = generate_random_json()
    with open(f'./rules/file_{i}.json', 'w') as f:
        json.dump(data, f, indent=4)

print("Generated 100 JSON files.")
