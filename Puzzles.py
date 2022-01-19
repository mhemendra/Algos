def generateProject(projects, dependencies, output=[]):
    nonDepProjects = projects.copy()
    for dep in dependencies:
        try:
            nonDepProjects.remove(dep[1])
        except:
            pass
    if not nonDepProjects:
        return False

    output.extend(nonDepProjects)

    remainingProjects =  [x for x in projects if x not in nonDepProjects]
    remainingDependencies = [x for x in dependencies if x[0] not in nonDepProjects]

    print(remainingProjects, remainingDependencies)

    if not remainingDependencies:
        output.extend(remainingProjects)
    elif remainingProjects:
        if not generateProject(remainingProjects, remainingDependencies, output):
            return False
    return output


projects = ['a', 'b', 'c', 'd', 'e', 'f','g','h']
dependency = [['a','d'], ['f','b'], ['b','d'],['f','a'],['d','c'],['d','g'],['d','h']]
output = generateProject(projects, dependency)
print(output)