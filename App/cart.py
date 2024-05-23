class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            self.session["cart"] = {}
            self.cart = self.session["cart"]
        else:
            self.cart = cart

    def add_service(self, servicio):
        id = str(servicio.id)
        if id not in self.cart.keys():
            self.cart[id]={
                "servicio_id": servicio.id,
                "nombre": servicio.nombre,
                "precio": servicio.precio,
                "acumulado": servicio.precio,
                "cantidad": 1,
            }
        else:
            self.cart[id]["cantidad"] += 1
            self.cart[id]["precio"] = servicio.precio
            self.cart[id]["acumulado"] += servicio.precio
        self.save_cart()

    def save_cart(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    def delete_service(self, servicio):
        id = str(servicio.id)
        if id in self.cart:
            del self.cart[id]
            self.save_cart()

    def subtract(self, servicio):
        id = str(servicio.id)
        if id in self.cart.keys():
            self.cart[id]["cantidad"] -= 1
            self.cart[id]["acumulado"] -= servicio.precio
            if self.cart[id]["cantidad"] <= 0: self.delete_service(servicio)
            self.save_cart()

    def clean(self):
        self.session["cart"] = {}
        self.session.modified = True