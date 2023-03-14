#Definition of operations required to match and evaluate the queries
# Distance measure: D = Sum_i(local)|ha(i) - hb(i)|
import numpy as np

def distances(query_ehd, database_ehd):
    # Calculate distance
    d = np.sum(np.absolute(np.subtract(query_ehd,database_ehd)))

    return d