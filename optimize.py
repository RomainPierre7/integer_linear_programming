from mip import *

# Permet l'appel de la fonction avec subprocess pour récupérer l'output du solveur
def optimize(model_number):
    model = Model(name = "ULS", solver_name="CBC")
    model.read("model" + str(model_number) + ".lp")
    return model.optimize(max_seconds=180)

if __name__ == "__main__":
    import sys
    optimize(sys.argv[1])