from enum import Enum

class SkillGrade(str, Enum):
    zero = "0"            # 0차 스킬 및 제로 공용스킬
    first = "1"           # 1차 스킬
    one_five = "1.5"      # 1.5차 스킬
    second = "2"          # 2차 스킬
    two_five = "2.5"      # 2.5차 스킬
    third = "3"           # 3차 스킬
    fourth = "4"          # 4차 스킬 및 제로 알파/베타 스킬
    hyperpassive = "hyperpassive"  # 하이퍼 패시브 스킬
    hyperactive = "hyperactive"    # 하이퍼 액티브 스킬
    fifth = "5"           # 5차 스킬
    sixth = "6"           # 6차 스킬
