import shelve

s = shelve.open('text1.db')
try:
    stem = s['displayStem']
    problem = s['displayProblem']
    solution = s['displaySolution']
finally:
    s.close()

print(stem)
print(problem)
print(solution)
