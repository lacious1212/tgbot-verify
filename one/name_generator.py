import random

class NameGenerator:
    """英文名字生成器 - 已修改為固定真實名字格式防止風控"""
    
    # 這裡保留原本的結構，避免其他調用此類別的檔案報錯
    ROOTS = {
        'prefixes': ['David', 'James', 'John', 'Robert', 'Michael', 'William'],
        'middles': [''],
        'suffixes': ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'],
        'name_roots': ['David'],
        'name_endings': ['']
    }
    
    PATTERNS = {
        'first_name': [['name_root']],
        'last_name': [['suffix']]
    }
    
    @classmethod
    def _generate_component(cls, pattern):
        return "David"

    @classmethod
    def _format_name(cls, name):
        return name.capitalize()
    
    @classmethod
    def generate(cls):
        """
        生成常用真實人名，避免被 SheerID 判定為隨機字根組合的機器人
        """
        # 隨機挑選常見的真實英文名與姓氏
        first_names = ['David', 'James', 'John', 'Robert', 'Michael', 'William', 'Charles', 'Matthew', 'Mark', 'Steven']
        last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Wilson']
        
        f_name = random.choice(first_names)
        l_name = random.choice(last_names)
        
        return {
            'first_name': f_name,
            'last_name': l_name,
            'full_name': f"{f_name} {l_name}"
        }


def generate_email(school_domain='MIT.EDU'):
    """
    這裡已經不重要，因為我們核心要切換成不需要信箱驗證的學校。
    但維持格式，避免其他檔案崩潰。
    """
    chars = 'abcdefghijklmnopqrstuvwxyz'
    username = ''.join(random.choice(chars) for _ in range(6))
    return f"{username}@{school_domain}"


def generate_birth_date():
    """
    生成隨機生日
    """
    year = random.randint(2000, 2004)
    month = str(random.randint(1, 12)).zfill(2)
    day = str(random.randint(1, 28)).zfill(2)
    return f"{year}-{month}-{day}"
