import math

class Warehouse:
    def __init__(self, coords_str, product_str):
        (loc_x, loc_y) = coords_str.split()
        self._x = loc_x
        self._y = loc_y
        self._products = []
        self.ordercount = 0
        self.dronecount = 0
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
        self.warehouse = None
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

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


class District:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

def dist(a,b):
    return math.sqrt(math.pow(int(a.x)-int(b.x),2)+math.pow(int(a.y)-int(b.y),2))

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


def allocateDrones():
    global n_orders
    global drones
    global warehouses
    global ordersForWarehouse

    print("drones:" + drones)

    for w in warehouses:
        load = w.ordercount/n_orders
        w.dronecount = round(load*(int)(drones))

def allocateWarehouses():
    global orders
    global warehouses
    global warehouseForOrder
    global ordersForWarehouse

    for o in orders:
        d = dist(o,warehouses[0])
        closestW = warehouses[0]

        for w in warehouses[1:]:
            if dist(o,w) < d:
                d = dist(o,w)
                closestW = w;

        o.warehouse = closestW
        closestW.ordercount += 1


allocateDrones()
allocateWarehouses()
