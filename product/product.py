from db import Database

class Product:
    def __init__(self, id = None, name = None, description = None, price = None):
        self.id = id
        self.name = name
        self.description = description
        self.price = price

    @staticmethod
    def get_all():
        db = Database()
        db.query("SELECT * FROM PRODUCTS")
        products = db.cursor.fetchall()
        db.close()
        return [Product(**product) for product in  products]

    @staticmethod
    def get_by_id(product_id):
        db = Database()
        db.query("SELECT * FROM PRODUCTS WHERE id = %s", (product_id,))
        product = db.cursor.fetchone()
        db.close()
        return Product(**product) if product else None

    def save(self):
        db = Database()

        if self.id:
            db.query(
                "UPDATE PRODUCTS SET name = %s, description = %s, price = %s WHERE id = %s",
                (self.name, self.description, self.price, self.id)
            )
        else:
            db.query(
                "INSERT INTO PRODUCTS (name, description, price) VALUES (%s, %s, %s)",
                (self.name, self.description, self.price)
            )
            self.id = db.cursor.lastrowid


        db.commit()
        db.close()

    def delete(self):
        db = Database()
        db.query("DELETE FROM PRODUCTS WHERE id = %s", (self.id,))
        db.commit()
        db.close()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price
        }
