
def meter_to_feet(m):
    f = 3.28084 * m
    return f


y = list(range(1,10001))
for i in y:
    x = meter_to_feet(i)
    print(x)