"""
饮食顾问程序
让用户输入身高（厘米）和体重（公斤），计算 BMI 并给出健康饮食建议。
"""

def get_user_input():
    """获取用户的身高（厘米）和体重（公斤）"""
    height_cm = float(input("请输入身高（厘米）："))
    weight_kg = float(input("请输入体重（公斤）："))
    return height_cm, weight_kg


def calculate_bmi(weight_kg, height_cm):
    """根据体重（公斤）和身高（厘米）计算 BMI"""
    height_m = height_cm / 100.0
    bmi = weight_kg / (height_m ** 2)
    return bmi


def classify_bmi(bmi):
    """根据 BMI 值返回分类名称"""
    if bmi < 18.5:
        return "偏瘦"
    elif bmi < 24:
        return "正常"
    elif bmi < 28:
        return "偏胖"
    else:
        return "肥胖"


def get_advice(category):
    """根据分类返回对应的中文健康饮食建议"""
    advice = {
        "偏瘦": "建议增加营养摄入，多吃富含蛋白质和碳水化合物的食物，如鸡蛋、牛奶、瘦肉、米饭等。",
        "正常": "继续保持均衡饮食，多吃蔬菜水果，适量摄入蛋白质和谷物，保持良好生活习惯。",
        "偏胖": "建议控制总热量摄入，减少高糖高脂食物，增加蔬菜和全谷物比例，配合适量运动。",
        "肥胖": "建议咨询医生或营养师，制定科学减重计划，严格控制饮食，增加有氧运动。",
    }
    return advice.get(category, "未知分类")


def main():
    """主函数：循环获取输入、计算 BMI、分类并输出建议，直到用户选择退出"""
    while True:
        height_cm, weight_kg = get_user_input()
        bmi = calculate_bmi(weight_kg, height_cm)
        category = classify_bmi(bmi)
        advice = get_advice(category)

        print(f"\n您的 BMI 值为：{bmi:.1f}")
        print(f"分类：{category}")
        print(f"建议：{advice}")

        # 询问是否继续
        choice = input("\n是否继续？(y/n)：").strip().lower()
        if choice == "n":
            print("程序结束，再见！")
            break


if __name__ == "__main__":
    main()
