from datetime import datetime

categories = {'居家用品': {'url': ''},
              '廚房用品': {'url': ''},
              '衛生用品': {'url': ''},
              '身體保養': {'url': ''},
              '臉部保養': {'url': ''},
              '彩妝用品': {'url': ''},
              '零食': {'url': ''},
              '冷凍食品': {'url': ''},
              '料理包': {'url': ''},
             }

types = {'生活館': {'居家用品': categories['居家用品'], '廚房用品': categories['廚房用品'], '衛生用品': categories['衛生用品']},
         '保養館': {'身體保養': categories['身體保養'], '臉部保養': categories['臉部保養'], '彩妝用品': categories['彩妝用品']},
         '美食館': {'零食': categories['零食'], '冷凍食品': categories['冷凍食品'], '料理包': categories['料理包']}
        }

tags = {'網紅代言':{},
        '化妝品':{},
        '眼霜':{},
        '美甲':{},
        '油':{},
        '洗髮乳':{},}

products = {'P001': {'p_id': 'P001',
                     'image_url': 'images/silverware-1.jpg', # 540*720
                     'image_alt': 'product-01',
                     'image_list': ['images/product-07.jpg', 'images/product-08.jpg', 'images/product-09.jpg'], # 540*720
                     'discount': None,
                     'price': 430,
                     'name': 'C2C經典純色刷毛大學帽T．多入優惠',
                     'intro': '這是一個很棒的產品唷',
                     'size': ['S', 'M', 'L'],
                     'categories': ['特價', '刷毛', '經典'],
                     'views': 67,
                     'created_date': datetime(2022, 11, 15),
                     'last_edit_date': datetime(2022, 11, 15),
                     },
            'P002': {'p_id': 'P002',
                     'image_url': 'images/silverware-2.jpg',
                     'image_alt': 'product-02',
                     'image_list': ['images/product-10.jpg', 'images/product-11.jpg', 'images/product-12.jpg'],
                     'discount': None,
                     'price': 100,
                     'name': '支援MagSafe無線磁吸充電',
                     'intro': '很棒的產品唷',
                     'size': ['S', 'M', 'L'],
                     'categories': ['特價', '無線', 'MagSafe'],
                     'views': 627,
                     'created_date': datetime(2022, 11, 10),
                     'last_edit_date': datetime(2022, 11, 13),
                     },
            'P003': {'p_id': 'P003',
                     'image_url': 'images/silverware-3.jpg',
                     'image_alt': 'product-03',
                     'image_list': ['images/product-13.jpg', 'images/product-08.jpg', 'images/product-14.jpg'],
                     'discount': None,
                     'price': 20,
                     'name': '安全低溫，磁吸充電不傷機',
                     'intro': '這是一個很棒的產品唷',
                     'size': ['S', 'M', 'L'],
                     'categories': ['特價', '熱門', '充電'],
                     'views': 2977,
                     'created_date': datetime(2022, 11, 15),
                     'last_edit_date': datetime(2022, 11, 15),
                     },
            'P004': {'p_id': 'P004',
                     'image_url': 'images/silverware-4.jpg',
                     'image_alt': 'product-04',
                     'image_list': ['images/product-12.jpg', 'images/product-14.jpg', 'images/product-09.jpg'],
                     'discount': None,
                     'price': 100,
                     'name': 'product-04',
                     'intro': '這是一個很棒的產品唷',
                     'size': ['S', 'M', 'L'],
                     'categories': ['特價', '刷毛', '熱門'],
                     'views': 343,
                     'created_date': datetime(2022, 11, 10),
                     'last_edit_date': datetime(2022, 11, 13),
                     },
            'P005': {'p_id': 'P005',
                     'image_url': 'images/silverware-5.jpg',
                     'image_alt': 'product-05',
                     'image_list': ['images/product-15.jpg', 'images/product-16.jpg', 'images/product-09.jpg'],
                     'discount': 0.2,
                     'price': 500,
                     'name': 'product-05',
                     'intro': '這是一個很棒的產品唷',
                     'size': ['S', 'M', 'L'],
                     'categories': ['聖誕節', '很棒', '經典'],
                     'views': 67,
                     'created_date': datetime(2022, 11, 15),
                     'last_edit_date': datetime(2022, 11, 15),
                     },
            'P006': {'p_id': 'P006',
                     'image_url': 'images/silverware-6.jpg',
                     'image_alt': 'product-06',
                     'image_list': ['images/product-11.jpg', 'images/product-12.jpg', 'images/product-09.jpg'],
                     'discount': None,
                     'price': 1000,
                     'name': 'product-06',
                     'intro': '這是一個很棒的產品唷',
                     'size': ['S', 'M', 'L'],
                     'categories': ['特價', '聖誕節', '很棒'],
                     'views': 67,
                     'created_date': datetime(2022, 10, 10),
                     'last_edit_date': datetime(2022, 11, 13),
                     },
            'P007': {'p_id': 'P007',
                     'image_url': 'images/silverware-7.jpg',
                     'image_alt': 'product-07',
                     'image_list': ['images/product-07.jpg', 'images/product-11.jpg', 'images/product-16.jpg'],
                     'discount': None,
                     'price': 500,
                     'name': 'product-07',
                     'intro': '這是一個很棒的產品唷',
                     'size': ['S', 'M', 'L'],
                     'categories': ['特價', '很棒', '經典'],
                     'views': 67,
                     'created_date': datetime(2022, 11, 5),
                     'last_edit_date': datetime(2022, 11, 14),
                     },
            'P008': {'p_id': 'P008',
                     'image_url': 'images/silverware-8.jpg',
                     'image_alt': 'product-08',
                     'image_list': ['images/product-04.jpg', 'images/product-14.jpg', 'images/product-10.jpg'],
                     'discount': None,
                     'price': 150,
                     'name': 'product-08',
                     'intro': '這是一個很棒的產品唷',
                     'size': ['S', 'M', 'L'],
                     'categories': ['很棒', '刷毛', '聖誕節'],
                     'views': 67,
                     'created_date': datetime(2022, 9, 10),
                     'last_edit_date': datetime(2022, 11, 13),
                     },
                        }

topics = {'topic-1': {'url': ''},
          'topic-2': {'url': ''},
          'topic-3': {'url': ''}}

home_banner_list = [{'url': 'images/bg-slider-18.jpg', 'alt': 'banner-1'},
                    {'url': 'images/bg-slider-19.jpg', 'alt': 'banner-2'},
                    {'url': 'images/bg-slider-20.jpg', 'alt': 'banner-3'},]

home_promote_product_id_list = ['P001', 'P002', 'P003', 'P004', 'P005', 'P006', 'P007', 'P008']
home_promote_section_title = '暢銷熱賣'
home_promote_section_subtitle = ' '