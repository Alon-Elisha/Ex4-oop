"""
@author AchiyaZigi
OOP - Ex4
Very simple GUI example for python client to communicates with the server and "play the game!"
"""
import sys
from types import SimpleNamespace

from DiGraph import DiGraph
from EdgeData import EdgeData
from GraphAlgo import GraphAlgo
from NodeData import NodeData
from client import Client
import json
from pygame import gfxdraw
import pygame
from pygame import *
import math
from collections import defaultdict
import time

# init pygame

WIDTH, HEIGHT = 1080, 720

# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'
if __name__ == '__main__':
    pygame.init()

    screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
    clock = pygame.time.Clock()
    pygame.font.init()
    client = Client()
    client.start_connection(HOST, PORT)

    pokemons = client.get_pokemons()
    pokemons_obj = json.loads(pokemons, object_hook=lambda d: SimpleNamespace(**d))

    # print(pokemons)

    graph_json = client.get_graph()
    print(graph_json)

    FONT = pygame.font.SysFont('Arial', 20, bold=True)
    poke_font = pygame.font.SysFont('Arial', 14, bold=True)
    # load the json string into SimpleNamespace Object

    graph = json.loads(
        graph_json, object_hook=lambda json_dict: SimpleNamespace(**json_dict))

    for n in graph.Nodes:
        x, y, _ = n.pos.split(',')
        # n.pos = SimpleNamespace(x=float(x), y=float(y))
        x = float(x)
        y = float(y)
        n.pos = (x, y)

    # print(graph.Edges)
    g = DiGraph()
    Edges = []
    Nodes = {}
    for n in graph.Nodes:
        g.add_node(n.id, n.pos)
        Nodes[n.id] = n.pos
    for e in graph.Edges:
        new_e = EdgeData(e.src, e.dest, e.w)
        # Edges.append(new_e)
        g.add_edge(e.src, e.dest, e.w)

    # get data proportions
    min_x = min(list(graph.Nodes), key=lambda n: n.pos[0]).pos[0]
    min_y = min(list(graph.Nodes), key=lambda n: n.pos[1]).pos[1]
    max_x = max(list(graph.Nodes), key=lambda n: n.pos[0]).pos[0]
    max_y = max(list(graph.Nodes), key=lambda n: n.pos[1]).pos[1]


    def scale(data, min_screen, max_screen, min_data, max_data):
        """
        get the scaled data with proportions min_data, max_data
        relative to min and max screen dimentions
        """
        return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen


    # decorate scale with the correct values

    def my_scale(data, x=False, y=False):
        if x:
            return scale(data, 50, screen.get_width() - 50, min_x, max_x)
        if y:
            return scale(data, 50, screen.get_height() - 50, min_y, max_y)


    radius = 15

    client.add_agent("{\"id\":4}")
    client.add_agent("{\"id\":3}")
    client.add_agent("{\"id\":10}")
    client.add_agent("{\"id\":5}")

    move_counter = 0
    points = 0

    # this commnad starts the server - the game is running now
    client.start()

    """
    The code below should be improved significantly:
    The GUI and the "algo" are mixed - refactoring using MVC design pattern is required.
    """
    pokemon_positions = []
    agent_paths = defaultdict(list)
    stop_pressed = False
    while client.is_running() == 'true':
        start = time.time()
        pokemons = json.loads(client.get_pokemons(),
                              object_hook=lambda d: SimpleNamespace(**d)).Pokemons
        pokemons = [p.Pokemon for p in pokemons]
        for p in pokemons:
            x, y, _ = p.pos.split(',')
            p.pos = SimpleNamespace(x=my_scale(
                float(x), x=True), y=my_scale(float(y), y=True))
        agents = json.loads(client.get_agents(),
                            object_hook=lambda d: SimpleNamespace(**d)).Agents
        agents = [agent.Agent for agent in agents]
        for a in agents:
            x, y, _ = a.pos.split(',')
            a.pos = SimpleNamespace(x=my_scale(
                float(x), x=True), y=my_scale(float(y), y=True))
        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        # refresh surface
        screen.fill(Color(0, 0, 0))

        # draw nodes
        for n in g.get_all_v().values():
            x = my_scale(n.getPos()[0], x=True)
            y = my_scale(n.getPos()[1], y=True)

            # its just to get a nice antialiased circle
            gfxdraw.filled_circle(screen, int(x), int(y),
                                  radius, Color(64, 80, 174))
            gfxdraw.aacircle(screen, int(x), int(y),
                             radius, Color(255, 255, 255))

            # draw the node id
            id_srf = FONT.render(str(n.getId()), True, Color(255, 255, 255))
            rect = id_srf.get_rect(center=(x, y))
            screen.blit(id_srf, rect)

        # draw edges
        for e in g.get_all_edges():
            # find the edge nodes
            src = next(n for n in g.get_all_v().values() if n.getId() == e.get_src())
            dest = next(n for n in g.get_all_v().values() if n.getId() == e.get_dest())

            # scaled positions
            src_x = my_scale(src.getPos()[0], x=True)
            src_y = my_scale(src.getPos()[1], y=True)
            dest_x = my_scale(dest.getPos()[0], x=True)
            dest_y = my_scale(dest.getPos()[1], y=True)

            # draw the line
            pygame.draw.line(screen, Color(61, 72, 126),
                             (src_x, src_y), (dest_x, dest_y))

        # draw agents
        for agent in agents:
            pygame.draw.circle(screen, Color(122, 61, 23),
                               (int(agent.pos.x), int(agent.pos.y)), 10)
            id_srf = FONT.render(str(agent.id), True, Color(255, 255, 255))
            rect = id_srf.get_rect(center=(agent.pos.x, agent.pos.y))
            screen.blit(id_srf, rect)
        # draw pokemons (note: should differ (GUI wise) between the up and the down pokemons (currently they are marked in the same way).
        for p in pokemons:
            if p.type == -1:
               pygame.draw.circle(screen, Color(0, 255, 255), (int(p.pos.x), int(p.pos.y)), 10)
            else:
                pygame.draw.circle(screen, Color(200, 235, 100), (int(p.pos.x), int(p.pos.y)), 10)

            id_srf = poke_font.render(str(int(p.value)), True, Color(0, 0, 0))
            rect = id_srf.get_rect(center=(int(p.pos.x), int(p.pos.y)))
            screen.blit(id_srf, rect)

        point_cnt = poke_font.render("points: " + str(int(points)), True, Color(255, 255, 255))
        move_cnt = poke_font.render("moves: " + str(move_counter), True, Color(255, 255, 255))
        ttl = client.time_to_end()
        time_to_last = poke_font.render("ttl: " + ttl, True, Color(255, 255, 255))
        stop_button = poke_font.render("STOP", True, Color(255, 255, 255), Color(255, 0, 0))
        screen.blit(point_cnt, (10, 10))
        screen.blit(move_cnt, (80, 10))
        screen.blit(time_to_last, (150, 10))
        screen.blit(stop_button, (1000, 10))

        # update screen changes
        display.update()

        # refresh rate
        clock.tick(60)
        # ------------------------------------------------------------------------------

        nodes = g.get_all_v()
        for p in pokemons:
            for e in g.get_all_edges():
                n1 = nodes[e.get_src()]
                n2 = nodes[e.get_dest()]
                n1_x = my_scale(n1.getPos()[0], x=True)
                n1_y = my_scale(n1.getPos()[1], y=True)
                pos1 = (n1_x, n1_y)
                n2_x = my_scale(n2.getPos()[0], x=True)
                n2_y = my_scale(n2.getPos()[1], y=True)
                pos2 = (n2_x, n2_y)
                x, y = p.pos.x, p.pos.y
                p_pos = (float(x), float(y))
                if round(math.dist(pos1, p_pos) + math.dist(p_pos, pos2), 4) == round(math.dist(pos1, pos2), 4):
                    big = max(n1.getId(), n2.getId())
                    small = min(n1.getId(), n2.getId())
                    if e not in pokemon_positions:
                        if p.type == -1:
                            if big == e.get_src():
                                pokemon_positions.append(e)
                        else:
                            if big == e.get_dest():
                                pokemon_positions.append(e)

        # choose next edge
        algo = GraphAlgo(g)
        for agent in agents:
            for p in pokemon_positions:
                if agent.src == p.get_dest() and len(agent_paths[agent.id]) == 0:
                    pokemon_positions.remove(p)
            if agent.dest == -1:
                min_weight = sys.float_info.max
                min_weight_path = []
                final_dest = 0
                for edge in pokemon_positions:
                    w, path = algo.shortest_path(agent.src, edge.get_src())
                    w += edge.get_weight()
                    if w < min_weight:
                        final_dest = edge.get_dest()
                        min_weight = w
                        min_weight_path = path

                if len(min_weight_path) > 0:
                    del min_weight_path[0]
                min_weight_path.append(final_dest)
                agent_paths[agent.id] = min_weight_path

        for agent in agents:
            if agent.dest == -1:
                next_node = agent_paths[agent.id][0]
                client.choose_next_edge(
                    '{"agent_id":' + str(agent.id) + ', "next_node_id":' + str(next_node) + '}')
                del agent_paths[agent.id][0]
                ttl = client.time_to_end()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("HERE")
                pos = pygame.mouse.get_pos()
                if 1000 < pos[0] < 1080 and 10 < pos[1] < 40:
                    client.stop()

        points = 0
        for a in agents:
            points += a.value

        move_counter += 1

        while time.time() - start < 0.1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if 1000 < pos[0] < 1080 and 10 < pos[1] < 40:
                        client.stop()




        """for agent in agents:
            if agent.dest == -1:
                next_node = (agent.src - 1) % len(graph.Nodes)
                client.choose_next_edge(
                    '{"agent_id":'+str(agent.id)+', "next_node_id":'+str(next_node)+'}')
                ttl = client.time_to_end()
                #print(ttl, client.get_info())"""

        client.move()



    # game over:
