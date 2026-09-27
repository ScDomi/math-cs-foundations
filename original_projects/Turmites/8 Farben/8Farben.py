# these turmites use the instructions LLRLRRLR
# it is displayed using 8 different colors

import mesa.space
from mesa import Agent, Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

class LangtonsAnt(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.direction = 'up'

    def turn_left(self):
        if self.direction == 'up':
            self.direction = 'left'
        elif self.direction == 'left':
            self.direction = 'down'
        elif self.direction == 'down':
            self.direction = 'right'
        else:
            self.direction = 'up'

    def turn_right(self):
        if self.direction == 'up':
            self.direction = 'right'
        elif self.direction == 'right':
            self.direction = 'down'
        elif self.direction == 'down':
            self.direction = 'left'
        else:
            self.direction = 'up'

    def change_color_on_move(self, turn_left, turn_right):
        x, y = self.pos
        cell_contents = self.model.grid.get_cell_list_contents((x, y))
        for agent in cell_contents:
            if isinstance(agent, White):
                self.model.grid.remove_agent(agent)
                self.model.grid.place_agent(Black(agent.unique_id, self.model, (x, y)), (x, y))
                self.turn_left()
                self.move_forward()
            elif isinstance(agent, Black):
                self.model.grid.remove_agent(agent)
                self.model.grid.place_agent(Purple(agent.unique_id, self.model, (x, y)), (x, y))
                self.turn_left()
                self.move_forward()
            elif isinstance(agent, Purple):
                self.model.grid.remove_agent(agent)
                self.model.grid.place_agent(Yellow(agent.unique_id, self.model, (x, y)), (x, y))
                self.turn_right()
                self.move_forward()
            elif isinstance(agent, Yellow):
                self.model.grid.remove_agent(agent)
                self.model.grid.place_agent(Blue(agent.unique_id, self.model, (x, y)), (x, y))
                self.turn_left()
                self.move_forward()
            elif isinstance(agent, Blue):
                self.model.grid.remove_agent(agent)
                self.model.grid.place_agent(Green(agent.unique_id, self.model, (x, y)), (x, y))
                self.turn_right()
                self.move_forward()
            elif isinstance(agent, Green):
                self.model.grid.remove_agent(agent)
                self.model.grid.place_agent(Orange(agent.unique_id, self.model, (x, y)), (x, y))
                self.turn_right()
                self.move_forward()
            elif isinstance(agent, Orange):
                self.model.grid.remove_agent(agent)
                self.model.grid.place_agent(Brown(agent.unique_id, self.model, (x, y)), (x, y))
                self.turn_left()
                self.move_forward()
            elif isinstance(agent, Brown):
                self.model.grid.remove_agent(agent)
                self.model.grid.place_agent(White(agent.unique_id, self.model, (x, y)), (x, y))
                self.turn_right()
                self.move_forward()
    
    def move_forward(self):
        x, y = self.pos
        if self.direction == 'up':
            new_x, new_y = x, y - 1
        elif self.direction == 'right':
            new_x, new_y = x + 1, y
        elif self.direction == 'down':
            new_x, new_y = x, y + 1
        else:
            new_x, new_y = x - 1, y

        self.model.grid.move_agent(self, (new_x, new_y))

    def step(self):
        self.change_color_on_move(self.turn_left(), self.turn_right())

class Black(Agent):
    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id, model)
        self.pos = pos
    def step():
        pass

class White(Agent):
    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id, model)
        self.pos = pos
    def step():
        pass

class Purple(Agent):
    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id, model)
        self.pos = pos
    def step():
        pass

class Yellow(Agent):
    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id, model)
        self.pos = pos
    def step():
        pass

class Blue(Agent):
    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id, model)
        self.pos = pos
    def step():
        pass

class Green(Agent):
    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id, model)
        self.pos = pos
    def step():
        pass

class Orange(Agent):
    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id, model)
        self.pos = pos
    def step():
        pass

class Brown(Agent):
    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id, model)
        self.pos = pos
    def step():
        pass
    
class LangtonsAntModel(Model):
    
    def __init__(self, N, width, height):
        self.num_agents = N
        self.width = width
        self.height = height
        self.grid = MultiGrid(width, height, torus=True)
        self.schedule = RandomActivation(self)
        # Create agents
        for i in range(N):
            a = LangtonsAnt(i, self)
            self.schedule.add(a)
                # Place agents on the grid
            x = 50 + i
            y = 50 + i
            self.grid.place_agent(a, (x, y))
        
        for x in range(width):
            for y in range(height):
                # assign every agent a different unique id like in a matrix
                self.grid.place_agent(White(x*10+y, self, (x, y)), (x, y))

    def step(self):
        """Advance the model by one step."""
        self.schedule.step()

def agent_portrayal(agent):
    if isinstance(agent, LangtonsAnt):
        portrayal = {
            "Shape": "circle",
            "Filled": "true",
            "Layer": 1,     # ant in front of background
            "Color": "brown",
            "r": 1,
            "x": agent.pos[0],
            "y": agent.pos[1]
        }
    elif isinstance(agent, Black):
        portrayal = {
            "Shape": "rect",
            "Filled": "true",
            "Layer": 0,
            "Color": "black",
            "w": 1,
            "h": 1,
            "xAlign": 0.5,
            "yAlign": 0.5,
            "x": agent.pos[0],
            "y": agent.pos[1]
        }
    elif isinstance(agent, White):
        portrayal = {
            "Shape": "rect",
            "Filled": "true",
            "Layer": 0,
            "Color": "white",
            "w": 1,
            "h": 1,
            "xAlign": 0.5,
            "yAlign": 0.5,
            "x": agent.pos[0],
            "y": agent.pos[1]
        }
    elif isinstance(agent, Purple):
        portrayal = {
            "Shape": "rect",
            "Filled": "true",
            "Layer": 0,
            "Color": "purple",
            "w": 1,
            "h": 1,
            "xAlign": 0.5,
            "yAlign": 0.5,
            "x": agent.pos[0],
            "y": agent.pos[1]
        }
    elif isinstance(agent, Yellow):
        portrayal = {
            "Shape": "rect",
            "Filled": "true",
            "Layer": 0,
            "Color": "yellow",
            "w": 1,
            "h": 1,
            "xAlign": 0.5,
            "yAlign": 0.5,
            "x": agent.pos[0],
            "y": agent.pos[1]
        }
    elif isinstance(agent, Blue):
        portrayal = {
            "Shape": "rect",
            "Filled": "true",
            "Layer": 0,
            "Color": "blue",
            "w": 1,
            "h": 1,
            "xAlign": 0.5,
            "yAlign": 0.5,
            "x": agent.pos[0],
            "y": agent.pos[1]
        }
    elif isinstance(agent, Green):
        portrayal = {
            "Shape": "rect",
            "Filled": "true",
            "Layer": 0,
            "Color": "green",
            "w": 1,
            "h": 1,
            "xAlign": 0.5,
            "yAlign": 0.5,
            "x": agent.pos[0],
            "y": agent.pos[1]
        }
    elif isinstance(agent, Orange):
        portrayal = {
            "Shape": "rect",
            "Filled": "true",
            "Layer": 0,
            "Color": "orange",
            "w": 1,
            "h": 1,
            "xAlign": 0.5,
            "yAlign": 0.5,
            "x": agent.pos[0],
            "y": agent.pos[1]
        }
    elif isinstance(agent, Brown):
        portrayal = {
            "Shape": "rect",
            "Filled": "true",
            "Layer": 0,
            "Color": "brown",
            "w": 1,
            "h": 1,
            "xAlign": 0.5,
            "yAlign": 0.5,
            "x": agent.pos[0],
            "y": agent.pos[1]
        }
    else:
        portrayal = {}  # Default portrayal for other agent types

    return portrayal


grid = mesa.visualization.CanvasGrid(agent_portrayal, 100, 100, 800, 800)
server = mesa.visualization.ModularServer(LangtonsAntModel, [grid], "Langton's Ant", {"N": 1, "width": 100, "height": 100})
server.port = 8521
server.launch()