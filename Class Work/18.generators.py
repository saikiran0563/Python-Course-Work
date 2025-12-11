def reels(data):
    for i in data:
        yield i

data=['1..100','101..200','201..300','301..400','401..500','501..600','601..700','701..800','801..900','901..1000']
scroll=reels(data)
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))