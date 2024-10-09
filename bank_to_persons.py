


def parse_bank_data(file_content):
    # 初始化一个空的列表来存储所有员工的信息
    employees = []

    # 将文件内容按行分割
    lines = file_content.strip().split('\n')
    
    # 遍历每一行数据
    for line in lines:
        # 去除行末尾的换行符并按逗号分割每行数据
        data = line.strip().split(',')

        if len(data) >= 6:  # 确保我们有足够的字段
            # 创建一个字典来存储每个员工的数据
            employee = {
                "name": data[0].strip(),
                "phone": data[3].strip(),
                "addr": data[2].strip(),  # 假设部门名称作为地址
                "place": "",  # 地址的具体位置，这里留空
                "door": "",  # 详细位置，这里留空
                "birth": "",  # 出生日期，这里留空
                "mail": data[4].strip(),
                "slang": "",  # 俚语，这里留空
                "other": ""  # 其他信息，这里留空
            }
            employees.append(employee)

    return employees

# 使用函数解析文件内容
file_content = """
Mohan  Bansal,Manager,ZO BHOPAL,7389949987,mohanbansal@unionbankofindia.bank
Satish Babau  Vaddi,Senior Manager,RO - HYDERABAD KOTI,7093199840,rmd.hyderabadkoti@unionbankofindia.bank
Naseeruddin  Shaik,Chief Manager,CO ANNEX HYDERABAD,9847490036,naseer1606@unionbankofindia.bank
Rudra  Prasad,Senior Manager,ZAO VISAKHAPATNAM,9000899566,cbs-ssivisakhapatnam@unionbankofindia.bank
Y.Srikanth  Kumar,ASST. GENERAL MANAGER,CR Cell HYDERABAD,7674838888,yskumar@unionbankofindia.bank
Chatles R  Collins,Senior Manager (Branch Head),RAJARAJESHWARI NAGAR MAIN,9488181763,seeyesias@gmail.com
Devash Kumar  Bajpai,Chief Manager (ZCO),ZO NEW DELHI,8422918593,deveshbajpai@unionbankofindia.bank
Sudesh Cheniramji  Patwardhan,Senior Manager,STATION ROAD AKOLA,9626477264,sudeshcp2011@gmail.com
Abhishek  Soni,Chief Manager,RO - INDORE,9329588990,abhisheks.soni@unionbankofindia.bank
K.K.  Shyji,Senior Manager (Branch Head),WEST HILL,9986787340,kkshyji@unionbankofindia.bank
"""
parsed_employees = parse_bank_data(file_content)

# 打印结果
for index, emp in enumerate(parsed_employees, start=1):
    print(f"Employee {index}:")
    print(emp)
