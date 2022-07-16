from doshop.models import Product

 
CART_NAME = 'cart'

class CartSessions:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_NAME)
        if not cart :
            cart = self.session[CART_NAME] = {}
        self.cart = cart
    

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products :
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['total_price'] = int(item['price']) * item['number']
            yield item 


    def remove(self, product):
        product_id =str(product.id)
        if product_id in self.cart :
            del self.cart[product_id]
            self.save()


    def save(self):
        self.session.modified = True
    
    
    def add(self, product, number):
        pd_id = str(product.id)
        
        if pd_id not in self.cart :
            if product.specialـprice :
                product.price = product.specialـprice
            self.cart[pd_id] = {'number' : number, 'price':str(product.price)}
        else :
            self.cart[pd_id]['number'] += number
        self.save()


    def get_total_price(self):
        total = 0
        for item in self.cart.values() :
            sumo = int(item['price']) * item['number']
            total = total + sumo
        return total
        

    def clear(self):
        del self.session[CART_NAME]
        self.save()

