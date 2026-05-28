# SheerID 验证配置文件

# SheerID API 配置
# 這裡維持你設定好的 Google One 活動大門鑰匙
PROGRAM_ID = '69e8a0d18415475fbfbf5157'
SHEERID_BASE_URL = 'https://services.sheerid.com'
MY_SHEERID_URL = 'https://my.sheerid.com'

# 文件大小限制
MAX_FILE_SIZE = 1 * 1024 * 1024  # 1MB

# 學校配置 - 徹底拋棄被封鎖的美國 PSU，改成台灣的大學
SCHOOLS = {
    '44141': {
        'id': 44141,
        'idExtended': '44141',
        'name': 'National Taiwan University (NTU)',
        'city': 'Taipei',
        'state': 'TPE',
        'country': 'TW',
        'type': 'UNIVERSITY',
        'domain': 'NTU.EDU.TW',
        'latitude': 25.0174,
        'longitude': 121.5405
    }
}

# 預設學校（對應上面的台灣大學 ID）
DEFAULT_SCHOOL_ID = '44141'

# UTM 参数（营销追踪参数）
DEFAULT_UTM_PARAMS = {
    'utm_source': 'gemini',
    'utm_medium': 'paid_media',
    'utm_campaign': 'students_pmax_bts-slap'
}
