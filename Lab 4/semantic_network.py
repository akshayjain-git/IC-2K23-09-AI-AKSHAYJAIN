# Semantic Network Representation

network = {
    'Canary': [('is_a', 'Bird'), ('color', 'Yellow')],
    'Bird': [('is_a', 'Animal'), ('has', 'Wings'), ('can', 'Fly')],
    'Animal': [('needs', 'Food')]
}

for node, relations in network.items():
    for relation, target in relations:
        print(node, '--', relation, '-->', target)
