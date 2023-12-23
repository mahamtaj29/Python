"""
Here I am implementing a simple class Product which can be used to handle products available in a store. Every product has three properties:
name (str)
price (float)
sale percentage (float)
the main focus of code is to implement set_sale_percentage, which can be used to put the product on sale with the given sale percentage and get_price method,
which returns the current sale price of the product, which is either the original price or cheaper if sale percentage is not 0.0.
"""
class Product:
    """ This class defines a simplified product for sale in a store."""
    def __init__(self, name, price, sale_percentage = 0.0):
        """ :param name: str, the name of the product.
            :param price: float, price of the product.
            :param sale_percentage: float, %age discount on the product """
        self.__name = name
        self.__price = price
        self.__sale = sale_percentage = 0.0
        self.__sale_price = 0
    def printout(self, sale_percentage=0.0):
        """ When a product's detail is needed to be printed on screen this method will handle it. """
        print(f"{self.__name}")
        print(f"  price: {self.__price:.2f}")
        print(f"  sale%: {self.__sale:.2f}")
    def get_price(self):
        """ This method will return the original price or cheaper if sale price is zero
            :param price: float, the price of the product
            :return: price: float """
        return (self.__price - self.__sale_price)
    def set_sale_percentage(self, percentage):
        """ When finding the discounted price of the product. :param percentage: float, the discount on the product. """
        # calculating the discount in original price
        self.__sale_price = self.__price * (percentage / 100)
        self.__sale = percentage
def main():
    test_products = {
        "milk": 1.00,
        "sushi": 12.95,
    }
    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)
        prod = Product(product_name, test_products[product_name])
        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")
        print("-" * 20)
        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")
        print("-" * 20)
        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")
        print("-" * 20)
if __name__ == "__main__":
    main()
