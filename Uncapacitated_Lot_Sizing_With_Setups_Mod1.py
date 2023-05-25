from mip import *
import time
import re
from io import StringIO
import subprocess

#Récupère les données de l'instance
def get_data(datafileName):
    with open(datafileName, "r") as file:
        line = file.readline()  
        lineTab = line.split()    
        nbPeriodes = int(lineTab[0])
        
        line = file.readline()  
        lineTab = line.split()
        demandes = []
        for i in range(nbPeriodes):
            demandes.append(int(lineTab[i]))
            
        line = file.readline()  
        lineTab = line.split()
        couts = []
        for i in range(nbPeriodes):
            couts.append(int(lineTab[i]))

        line = file.readline()  
        lineTab = line.split()
        cfixes = []
        for i in range(nbPeriodes):
            cfixes.append(int(lineTab[i]))
        
        line = file.readline()  
        lineTab = line.split()    
        cstock = int(lineTab[0])
        return nbPeriodes, demandes, couts, cfixes, cstock
    




# Récupère le nombre de noeuds utilisés dans le modèle grâce à l'output du solveur
def get_node_count(output):
    search_result = re.search(r"Search completed", output)
    partial_result = re.search(r"Partial search", output)
    if search_result:
        remaining_text = output[search_result.end():]
        values = re.findall(r'\b(\S+)\b', remaining_text)
        if len(values) >= 2:
            number = values[7]
            return number
    elif partial_result:
        remaining_text = output[partial_result.end():]
        values = re.findall(r'\b(\S+)\b', remaining_text)
        if len(values) >= 2:
            number = values[10]
            return number
    else:
        return "ERROR"





# Résout le modèle (type = "int" ou "cont")
def resolve_modele(type, nbPeriodes, demandes, couts, cfixes, cstock):
    model = Model(name = "ULS", solver_name="CBC")

    # Variables
    y = [model.add_var(name="Y"+str(i), lb=0, ub=1, var_type=BINARY) for i in range(nbPeriodes)]
    if  type == "int":
        x = [model.add_var(name="X"+str(i), lb=0, var_type=INTEGER) for i in range(nbPeriodes)]
        s = [model.add_var(name="S"+str(i), lb=0, var_type=INTEGER) for i in range(nbPeriodes)]
    elif type == "cont":
        x = [model.add_var(name="X"+str(i), lb=0, var_type=CONTINUOUS) for i in range(nbPeriodes)]
        s = [model.add_var(name="S"+str(i), lb=0, var_type=CONTINUOUS) for i in range(nbPeriodes)]

    #Fonction objectif
    model.objective = minimize(sum(x[i] * couts[i] + y[i] * cfixes[i] + cstock * s[i] for i in range(nbPeriodes)))

    #Contraintes
    M = 100000
    model.add_constr(x[0] == demandes[0] + s[0])
    model.add_constr(s[0] == x[0] - demandes[0])

    for i in range(1, nbPeriodes):
        model.add_constr(s[i-1] + x[i] == demandes[i] + s[i])
        model.add_constr(s[i] == s[i-1] + x[i] - demandes[i])

    for i in range(nbPeriodes):
        model.add_constr(x[i] <= y[i] * M)

    model.write("model1.lp")

    start = time.perf_counter()
    status = model.optimize(max_seconds=180)
    runtime = time.perf_counter() - start

    output = "ERROR"
    if type == "int":
        commande = "python3 optimize.py 1"
        resultat = subprocess.run(commande, shell=True, capture_output=True, text=True)
        if resultat.returncode == 0:
            output = resultat.stdout

    node_count = get_node_count(output)

    return model, status, runtime, node_count, y, x, s





# Affiche les résultats pour une instance dans le terminal
def lot_sizing_resolve(datafileName):
    nbPeriodes, demandes, couts, cfixes, cstock = get_data(datafileName)

    model_relax, status_relax, runtime_relax, node_count_relax, y_relax, x_relax, s_relax = resolve_modele("cont", nbPeriodes, demandes, couts, cfixes, cstock)
    model, status, runtime, node_count, y, x, s = resolve_modele("int", nbPeriodes, demandes, couts, cfixes, cstock)

    print("---------- " + datafileName + " ----------")
    print("Valeur de la relaxation linéaire calculée : ",  model_relax.objective_value)
    if status == OptimizationStatus.OPTIMAL:
        print("Status de la résolution: OPTIMAL")
    elif status == OptimizationStatus.FEASIBLE:
        print("Status de la résolution: TEMPS LIMITE et SOLUTION REALISABLE CALCULEE")
    elif status == OptimizationStatus.NO_SOLUTION_FOUND:
        print("Status de la résolution: TEMPS LIMITE et AUCUNE SOLUTION CALCULEE")
    elif status == OptimizationStatus.INFEASIBLE or status == OptimizationStatus.INT_INFEASIBLE:
        print("Status de la résolution: IRREALISABLE")
    elif status == OptimizationStatus.UNBOUNDED:
        print("Status de la résolution: NON BORNE")

    if model.num_solutions>0:
        print("Valeur de la fonction objectif de la solution calculée : ",  model.objective_value)
        print("Écart % avec la relaxation linéaire : ", 100*(model.objective_value - model_relax.objective_value) / model_relax.objective_value, "%")

        print("Mois de production :")
        for i in range(nbPeriodes):
            print(int(y[i].x), end=' ')
        print()

        print("Quantités produites :")
        for i in range(nbPeriodes):
            print(int(x[i].x), end=' ')
        print()

        print("Quantités stockées :")
        for i in range(nbPeriodes):
            print(int(s[i].x), end=' ')
        print()
        
        print("Nombre de noeuds : ", node_count)
        print("Temps de résolution: ", runtime, "s")

    else:
        print("Pas de solution calculée")
    




# Ecris les résultats pour une instance dans le fichier results_1.txt
def lot_sizing_resolve_to_file(datafileName):
    nbPeriodes, demandes, couts, cfixes, cstock = get_data(datafileName)

    model_relax, status_relax, runtime_relax, node_count_relax, y_relax, x_relax, s_relax = resolve_modele("cont", nbPeriodes, demandes, couts, cfixes, cstock)

    model, status, runtime, node_count, y, x, s = resolve_modele("int", nbPeriodes, demandes, couts, cfixes, cstock)

    file = open("results_1.txt", "a")
    file.write("---------- " + datafileName + " ----------\n")
    file.write("Valeur de la relaxation linéaire calculée : " + str(model_relax.objective_value) + "\n")
    if status == OptimizationStatus.OPTIMAL:
        file.write("Status de la résolution: OPTIMAL\n")
    elif status == OptimizationStatus.FEASIBLE:
        file.write("Status de la résolution: TEMPS LIMITE et SOLUTION REALISABLE CALCULEE\n")
    elif status == OptimizationStatus.NO_SOLUTION_FOUND:
        file.write("Status de la résolution: TEMPS LIMITE et AUCUNE SOLUTION CALCULEE\n")
    elif status == OptimizationStatus.INFEASIBLE or status == OptimizationStatus.INT_INFEASIBLE:
        file.write("Status de la résolution: IRREALISABLE\n")
    elif status == OptimizationStatus.UNBOUNDED:
        file.write("Status de la résolution: NON BORNE\n")

    if model.num_solutions>0:
        file.write("Valeur de la fonction objectif de la solution calculée : "  + str(model.objective_value) + "\n")
        file.write("Écart % avec la relaxation linéaire : " + str(100*(model.objective_value - model_relax.objective_value)/model_relax.objective_value) + "%\n")

        file.write("Mois de production :\n")
        for i in range(nbPeriodes):
            file.write(str(int(y[i].x)) + " ")
        file.write("\n")

        file.write("Quantités produites :\n")
        for i in range(nbPeriodes):
            file.write(str(int(x[i].x)) + " ")
        file.write("\n")

        file.write("Quantités stockées :\n")
        for i in range(nbPeriodes):
            file.write(str(int(s[i].x)) + " ")
        file.write("\n")

        file.write("Nombre de noeuds : " + str(node_count) + "\n")
        file.write("Temps de résolution: " + str(runtime) + "s\n")

    else:
        file.write("Pas de solution calculée\n")
    file.write("\n")
    file.close()





# Rempli le fichier results_1.txt des résultats de toutes les instances
def results_file():
    file = open("results_1.txt", "w")
    file.close
    lot_sizing_resolve_to_file('Instances_ULS/Instance21.1.txt')
    for i in range(1,11):
        lot_sizing_resolve_to_file('Instances_ULS/Instance60.' + str(i) + '.txt')
    for i in range(1,11):
        lot_sizing_resolve_to_file('Instances_ULS/Instance90.' + str(i) + '.txt')
    for i in range(1,11):
        lot_sizing_resolve_to_file('Instances_ULS/Instance120.' + str(i) + '.txt')
    lot_sizing_resolve_to_file('Instances_ULS/Toy_Instance.txt')





lot_sizing_resolve("Instances_ULS/Instance21.1.txt")
#results_file() #Attention, prend du temps à s'exécuter et supprime le fichier results_1.txt avant de réécrire dedans