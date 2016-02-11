import math
import write_output

output = write_output.Output()

class Warehouse:
    def __init__(self, coords_str, product_str):
        (loc_x, loc_y) = coords_str.split()
        self._x = loc_x
        self._y = loc_y
        self._products = []
        self.ordercount = 0
        self.dronecount = 0
        self.drones = []
        self.orders = []
        plist = product_str.split()
        for weight in plist:
            self._products.append(int(weight))
    
    def nextDrone(self):
        earliest = self.drones[0].cur_turn
        earliest_drone = self.drones[0]
        for d in self.drones[1:]:
            if d.cur_turn < earliest:
                earliest = d.cur_turn
                earliest_drone = d

        return earliest_drone

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

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

class Drone:
    def __init__(self, warehouse):
        global warehouses
        self._id = id_val
        self.cur_turn = 0
        self.x = warehouses[0].x
        self.y = warehouses[0].y
        self.warehouse = warehouse
        self.inventory = []

    def load(self, warehouse, itemtype, amount):
        global output
        self.cur_turn += dist(self, warehouse)
        for a in amount:
            warehouse.remove(itemtype)
            self.inventory.append(itemtype)
        output.load(self.idval, warehouse.idval, itemtype, amount)
        self.x = warehouse.x
        self.x = warehouse.y

    def deliver(self, order, itemtype, amount):
        global output
        self.cur_turn += dist(self, assignment[1])
        order.deliver(self.idval, order.idval,
                itemtype, amount)
        self.x = order.x
        self.y = order.y

    @property
    def idval(self):
        return self._id

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

def allocateDrones():
    global n_orders
    global drones
    global warehouses

    allocated = 0

    for w in warehouses:
        load = w.ordercount/n_orders
        w.dronecount = round(load*(int)(drones))

        for d in drones[allocated:w.dronecount]:
            w.drones.append(d)
        allocated += w.dronecount

def allocateWarehouses():
    global orders
    global warehouses

    for o in orders:
        d = dist(o,warehouses[0])
        closestW = warehouses[0]

        for w in warehouses[1:]:
            if dist(o,w) < d:
                d = dist(o,w)
                closestW = w;

        closestW.orders.append(o)
        closestW.ordercount += 1


allocateDrones()
allocateWarehouses()

warehouseToWarehouseDist = {}

def closestWarehouses(fromWarehouse):
    global warehouseToWarehouseDist
    for w in warehouses:
        warehouseToWarehouseDist[w] = dist(fromWarehouse,w)
    return sorted(warehouseToWarehouseDist.values())

def findClosestProduct(fromWarehouse, order, product, needed):
    warehouses = closestWarehouses(fromWarehouse)
    d = fromWarehouse.nextDrone()
    for w in warehouses:
         if product in w.products > 0:
            numAvailable = w.products[product]
            if numAvailable >= needed:
                d.load(w,product,needed)
                d.deliver(order,product,needed)
                break
            else:
                d.load(w,product,numAvailable)
                d.deliver(order,product,numAvailable)
                needed = needed - numAvailable
            
    return 0






