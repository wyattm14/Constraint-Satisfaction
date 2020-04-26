# import constraint
#
# problem = constraint.Problem()
#
# problem.addVariable('x', [1,2,3])
# problem.addVariable('y', range(10))
#
# def our_constraint(x, y):
#     if x + y >= 5:
#         return True
#
# problem.addConstraint(our_constraint, ['x','y'])
# # addConstraint(which_constraint, list_of_variable_order)
# #
# # problem.addConstraint(constraint.AllDifferentConstraint())
# solutions = problem.getSolutions()
# # Easier way to print and see all solutions
# # for solution in solutions:
# #    print(solution)
#
# # Prettier way to print and see all solutions
# length = len(solutions)
# print("(x,y) ∈ {", end="")
# for index, solution in enumerate(solutions):
#     if index == length - 1:
#         print("({},{})".format(solution['x'], solution['y']), end="")
#     else:
#         print("({},{}),".format(solution['x'], solution['y']), end="")
# print("}")
r=0
g=1
b=2

import constraint

problem = constraint.Problem()

problem.addVariable('wa', [r,g,b])
problem.addVariable('nt', [r,g,b])
problem.addVariable('sa', [r,g,b])
problem.addVariable('q', [r,g,b])
problem.addVariable('v', [r,g,b])
problem.addVariable('nsw', [r,g,b])
problem.addVariable('t', [r,g,b])

def our_constraint(wa, nt, sa, q, v, nsw, t):
    if wa != nt and wa != sa and nt != sa and nt != q and sa != q and sa != nsw and sa != v and q != nsw and nsw != v:
        return True

problem.addConstraint(our_constraint, ['wa','nt','sa','q','v','nsw','t'])
# addConstraint(which_constraint, list_of_variable_order)
#
# problem.addConstraint(constraint.AllDifferentConstraint())
solutions = problem.getSolutions()
# Easier way to print and see all solutions
count = 0
for solution in solutions:
   print(solution)
   count += 1
print ("The amount of solutions: ", count)

# Prettier way to print and see all solutions
# length = len(solutions)
# print("(x,y) ∈ {", end="")
# for index, solution in enumerate(solutions):
#     if index == length - 1:
#         print("({},{})".format(solution['wa'], solution['nt'],solution['sa'],solution['q'], solution['v'],solution['nsw'],solution['t']), end="")
#     else:
#         print("({},{}),".format(solution['wa'], solution['nt'],solution['sa'],solution['q'], solution['v'],solution['nsw'],solution['t']), end="")
# print("}")
