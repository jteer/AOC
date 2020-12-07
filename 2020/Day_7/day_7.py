import os
import sys
import re
import json

rel_path = "input.txt"
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, rel_path)

input_data = open(abs_file_path).read().splitlines()

def parse_input(input_data):
    edge_pattern = re.compile(r'\d+ \w+ \w+[,.]?')
    adjacency_pattern = re.compile(r'(\d+) (.*)')
    
    node, edges = input_data.split(' bags contain')
    parsed_edges = map(lambda x: adjacency_pattern.search(x).groups(), edge_pattern.findall(edges))
    return node, list(parsed_edges)


def find_max_colors(u, graph, search_target):
    if (found := (u == search_target)) or not graph[u]:
        return found
    return any(find_max_colors(v, graph, search_target) for w, v in graph[u])

def find_indiv_req(u, graph):
    return sum(int(w) + int(w) * find_indiv_req(v, graph) for w, v in graph[u])


if __name__ == "__main__":
    print(input_data)
    input_map = map(parse_input, input_data)
    graph = {vertex: edges for vertex, edges in input_map}
    # print(json.dumps(graph, indent=True))
    
    search_target = 'shiny gold'
    total_colors = sum(find_max_colors(u, graph, search_target) for u in graph.keys() if u != search_target)
    print(f'part 1: {total_colors}')

    individual_req = find_indiv_req(search_target, graph)
    print(f'part 2: {individual_req}')