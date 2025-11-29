class Catalogue:
    products = []
    def __init__(self, name: str):
        self.name = name

    def add_product(self, product_name: str):
        Catalogue.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        # return [product for product in self.products if product.startswith(first_letter)]
        filtered_products = []
        for product in self.products:
            if product[0] == first_letter:
                filtered_products.append(product)
        return filtered_products

    def __repr__(self):
        return f"Items in the {self.name} catalogue:\n" + '\n'.join(sorted(Catalogue.products))