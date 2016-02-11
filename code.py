class Warehouse:
    def __init__(self, coords_str, product_str):
        (loc_x, loc_y) = coords_str.split()
        self._x = loc_x
        self._y = loc_y
        self._products = []
        plist = product_str.split()
        for weight in plist:
            self._products.append(int(weight))

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def products(self):
        return self._products

class Order:
    def __init__(self, id_val, coords_str, n_orders_str, products_str):
        (loc_x, loc_y) = coords_str.split()
        self._id = id_val
        self._x = loc_x
        self._y = loc_y
        self._n_products = int(n_orders_str)
        self._products = {}
        products = products_str.split()
        for product in products:
            if product in self._products:
                self._products[product] += 1
            else:
                self._products[product] = 1

    @property
    def products(self):
        return self._products

    @property
    def idval(self):
        return self._id

with open("busy_day.in") as f:
    cur_line = 0
    raw = f.read().splitlines()
    params = raw[cur_line].split()
    cur_line += 1

    rows = params[0]
    cols = params[1]
    drones = params[2]
    deadline = params[3]
    max_load = params[4]

    n_products = int(raw[cur_line])
    cur_line += 1
    product_weights = []
    for weight in raw[cur_line].split():
        product_weights.append(weight)
    cur_line += 1
    n_warehouses = int(raw[cur_line])
    cur_line += 1
    warehouses = []
    for i in range(n_warehouses):
        warehouses.append(Warehouse(raw[cur_line], raw[cur_line + 1]))
        cur_line += 2
    n_orders = int(raw[cur_line])
    cur_line += 1
    orders = []

    for i in range(n_orders):
        orders.append(Order(i, raw[cur_line], raw[cur_line + 1],
            raw[cur_line + 2]))
        cur_line += 3
    for order in orders:
        print(order.idval)
        for product in order.products:
            print(product + ": " + str(order.products.get(product) *
                product_weights[int(product)]))
        print()
