outer_numbers = [1,2,3]
inner_words = ["ONE", "TWO", "THREE"]
for number in outer_numbers:
    print(f"this is iteration **{number}** of the OUTER loop")
    for word in inner_words:
        print(f"     this is iteration {word} of the INNER loop")
    print("\n")

programmers = [{'name': "rachel", 'favorite_languages': ['Ruby', 'JavaScript', 'SQL', "Java"]},
               {'name': "daniel", 'favorite_languages': ['JavaScript', 'Elixir', 'Python']},
               {'name': "greg", 'favorite_languages': ['C#', 'CoffeeScript', 'R']},
               {'name': "meryl", 'favorite_languages': ['C++', 'PHP', 'Swift']}
              ]
for programmer in programmers:
    for language in programmer['favorite_languages']:
        print(language)        