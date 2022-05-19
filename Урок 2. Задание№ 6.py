goods = []
features = {'Название': '', 'Цена': '', 'Количество': '', 'Шт.': ''}
analytics = {'Название': [], 'Цена': [], 'Количество': [], 'Шт.': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Для выхода напишите 'Q', и нажмите 'Enter', для анализа напишите 'W': ").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'W':
        print(f'\n Current analytics \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f'Введите: "{f}" ')
        features[f] = int(feature_) if (f == 'Цена' or f == 'Количество') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))
