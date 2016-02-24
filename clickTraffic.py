from elos import EloModel

products = {
    "tickle-me-elmo": 5.0,
    "fruit-loops": 4.0,
    "legos": 3.0,
    "army-men": 2.0,
    "lame-shirt": 1.0
}

model = EloModel(teams=products)

# Record the contest, lame-shirt does unexpectedly well
# Counts are numbers of clicks
model.contest("tickle-me-elmo", 6000.0, "lame-shirt", 10.0)
model.contest("tickle-me-elmo", 6000.0, "legos", 8000.0)
model.contest("army-men", 1000.0, "lame-shirt", 10000.0)
model.contest("fruit-loops", 1000.0, "lame-shirt", 10000.0)
model.contest("army-men", 4000.0, "tickle-me-elmo", 5000.0)
model.contest("legos", 1000.0, "lame-shirt", 1000.0)

print(model.teams)

import pdb; pdb.set_trace()
model.contest("lame-shirt", 10.0, "fruit-loops", 5000.0)
