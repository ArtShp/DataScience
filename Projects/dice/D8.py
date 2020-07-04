from Projects.dice.kick import Cube
import pygal as pg
from random import choice

count = 50000

grainMayBe = [6, 8, 10, 12]
lst = []
for k in range(100):
    arr = []
    for j in range(2):
        arr.append(Cube(choice(grainMayBe)).roll())
    lst.append(sum(arr))

result = lst





frequencies = []
max_res = Cube.grains
for val in range(Cube.instances, max_res+1):
    freq = result.count(val)
    frequencies.append(freq)

#print(frequencies)

arrr = [i for i in range(Cube.instances/100, Cube.grains+1)]

hist = pg.Bar()
hist.title = f'Результат подбрасывания {Cube.instances} игральных кости {count} раз'
hist.x_labels = arrr
hist._x_title = 'Сторона'
hist._y_title = 'Частота выпадения'

hist.add('D6', frequencies)
hist.render_to_file('Броски.svg')
