from random import choice

class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points

        self.x_val = [0]
        self.y_val = [0]

    def fillWalk(self):
        while len(self.x_val) < self.num_points:
            x_dir = choice([1, -1])
            x_dist = choice([0, 1, 2, 3, 4])
            x_step = x_dir * x_dist

            y_dir = choice([1, -1])
            y_dist = choice([0, 1, 2, 3, 4])
            y_step = y_dir * y_dist

            if x_step and y_step == 0:
                continue

            next_x = self.x_val[-1] + x_step
            next_y = self.y_val[-1] + y_step

            self.x_val.append(next_x)
            self.y_val.append(next_y)