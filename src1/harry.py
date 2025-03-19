from logic import *

rain = Symbol("rain")
hagrid = Symbol("hagrid")
dumbledore = Symbol("dumbledore")

knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)

print(rain.name + " is " + str(model_check(knowledge, rain)))
print(hagrid.name + " is " + str(model_check(knowledge, hagrid)))
print(dumbledore.name + " is " + str(model_check(knowledge, dumbledore)))
