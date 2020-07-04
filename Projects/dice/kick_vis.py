from Projects.dice.kick import Cube
import pygal as pg

die = Cube()
die2 = Cube()

result = [die.roll() + die2.roll() for i in range(1000)]
#print(result)

frequencies = []
max_res = die.number_of_sides + die2.number_of_sides
for val in range(2, max_res+1):
    freq = result.count(val)
    frequencies.append(freq)

#print(frequencies)

hist = pg.Bar()
hist.title = 'Результат подбрасывания одной игральной кости D6 1000 раз'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist._x_title = 'Сторона'
hist._y_title = 'Частота выпадения'

hist.add('D6', frequencies)
hist.render_to_file('Броски.svg')
