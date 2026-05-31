import random

categories = [
    ('painkillers','Og\'riq qoldiruvchi / Isitma tushiruvchi'),
    ('antibiotics','Antibiotik'),
    ('cardio','Yurak-qon tomir'),
    ('vitamins','Vitaminlar'),
    ('digestive','Ovqat hazm qilish'),
    ('immunity','Immunitet'),
    ('respiratory','Nafas yo\'llari'),
    ('skin','Teriga qarshi'),
    ('sleep','Uyqu va tinchlanish'),
    ('hormonal','Gormonlar')
]
manufacturers = [
    ('Uzpharmsanoat, O\'zbekiston','Uzpharmsanoat, Uzbekistan'),
    ('BukhPharm, O\'zbekiston','BukhPharm, Uzbekistan'),
    ('SamPharma, O\'zbekiston','SamPharma, Uzbekistan'),
    ('Toshkent Farm, O\'zbekiston','Tashkent Pharma, Uzbekistan'),
    ('Berlin-Chemie, Germaniya','Berlin-Chemie, Germany'),
    ('PharmaSwiss, Shveysariya','PharmaSwiss, Switzerland'),
    ('Pfizer, AQSH','Pfizer, USA'),
    ('Sanofi, Frantsiya','Sanofi, France'),
    ('Roche, Shveysariya','Roche, Switzerland'),
    ('Novartis, Shveysariya','Novartis, Switzerland')
]

def get_type_en(cat):
    return {
        'painkillers':'Analgesic / Antipyretic',
        'antibiotics':'Antibiotic',
        'cardio':'Cardiovascular',
        'vitamins':'Vitamin',
        'digestive':'Digestive Aid',
        'immunity':'Immune Support',
        'respiratory':'Respiratory Relief',
        'skin':'Dermatological',
        'sleep':'Sleep Aid',
        'hormonal':'Hormonal Balance'
    }[cat]

for i in range(9, 109):
    cat, type_uz = random.choice(categories)
    type_en = get_type_en(cat)
    med_name = f"Dori {i}"
    eng_name = f"Medicine {i}"
    manufacturer = manufacturers[i % len(manufacturers)]
    price = random.randrange(4000, 52000, 500)
    prescription = random.choice([True, False])
    rating = round(random.uniform(3.8, 5.0), 1)
    views = random.randint(120, 1550)
    createdDate = f"2026-05-{random.randint(1,28):02d}"
    image = f"med_generic_{i}.jpg"
    desc_uz = f"{med_name} organizmni qo‘llab-quvvatlovchi va simptomlarni yengillashtiruvchi zamonaviy preparat."
    desc_en = f"{eng_name} is a modern formulation that supports the body and relieves symptoms."
    usage_uz = f"Kattalar uchun kuniga 1-2 marta ovqatdan keyin {random.choice(['bir tabletka','ikki tabletka','bir kapsula'])} ichiladi."
    usage_en = f"For adults, take 1-2 times daily after meals, {random.choice(['one tablet','two tablets','one capsule'])}."
    dosage_uz = f"{random.choice(['100 mg','200 mg','250 mg','500 mg'])} {random.choice(['planshet','kapsula','sirop'])}."
    dosage_en = f"{random.choice(['100 mg','200 mg','250 mg','500 mg'])} {random.choice(['tablet','capsule','syrup'])}."
    side_uz = f"Kam hollarda allergik reaksiyalar, bosh aylanishi yoki oshqozon noqulayligi paydo bo‘lishi mumkin."
    side_en = f"Rare side effects may include allergic reactions, dizziness, or stomach discomfort."
    warn_uz = f"Agar sizda jigar yoki buyrak kasalligi bo‘lsa, shifokor bilan maslahat qiling."
    warn_en = f"Consult your doctor if you have liver or kidney conditions."
    print('  {')
    print(f'    id: "med-{i}",')
    print(f'    name: {{ uz: "{med_name}", en: "{eng_name}" }},')
    print(f'    image: "{image}",')
    print('    description: {')
    print(f'      uz: "{desc_uz}",')
    print(f'      en: "{desc_en}"')
    print('    },')
    print('    usage: {')
    print(f'      uz: "{usage_uz}",')
    print(f'      en: "{usage_en}"')
    print('    },')
    print('    dosage: {')
    print(f'      uz: "{dosage_uz}",')
    print(f'      en: "{dosage_en}"')
    print('    },')
    print('    sideEffects: {')
    print(f'      uz: "{side_uz}",')
    print(f'      en: "{side_en}"')
    print('    },')
    print('    warnings: {')
    print(f'      uz: "{warn_uz}",')
    print(f'      en: "{warn_en}"')
    print('    },')
    print(f'    manufacturer: {{ uz: "{manufacturer[0]}", en: "{manufacturer[1]}" }},')
    print(f'    price: {price},')
    print(f'    type: {{ uz: "{type_uz}", en: "{type_en}" }},')
    print(f'    category: "{cat}",')
    print(f'    prescription: {str(prescription).lower()},')
    print(f'    rating: {rating},')
    print(f'    views: {views},')
    print(f'    createdDate: "{createdDate}"')
    print('  },')
