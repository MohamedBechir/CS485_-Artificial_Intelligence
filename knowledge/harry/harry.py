from logic import *

rain = Symbol("rain") #It is raining
hagrid = Symbol("hagrid") #Harry visited Hagrid
dumbeldore = Symbol("dumbeldore") #Harry visited Dumbeldore

knowledge = And(Implication (Not(rain), hagrid),
                Or(hagrid, dumbeldore),
                Not(And(hagrid, dumbeldore)),
                dumbeldore)

model = model_check(knowledge, rain)

print(model)