# Knowledge Representation using facts and relations

knowledge_base = {
    'Akshay': {'is_a': 'Student', 'studies': 'Artificial Intelligence'},
    'AI': {'is_a': 'Subject', 'requires': 'Problem Solving'},
    'Python': {'is_a': 'Programming Language', 'used_for': 'Artificial Intelligence'}
}

for entity, facts in knowledge_base.items():
    print(entity)
    for relation, value in facts.items():
        print(' ', relation, '->', value)
