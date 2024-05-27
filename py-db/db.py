import psycopg2



# DOMAIN (add to cart, show catalog, ...)

def createProduct(name, price_amount, price_currency):
    # CONNECT

    conn = psycopg2.connect("dbname=e_shop_l2_v2 user=postgres password=12345")
    cur  = conn.cursor()

    # QUERY
    cur.execute(f"INSERT INTO products (name) VALUES('{name}')")
    cur.execute("SELECT MAX(id) FROM products")
    conn.commit()
    result=cur.fetchall()
    lastId = result[0][0]
    # print(result)

    cur.execute(f"INSERT INTO money (amount, currency, product_id) VALUES({price_amount},'{price_currency}',{lastId})")
    conn.commit()

def allProducts(byPriceAsc=True):
    # CONNECT
    conn = psycopg2.connect("dbname=e_shop_l2_v2 user=postgres password=12345")
    cur  = conn.cursor()
    #QUERY
    if byPriceAsc:
        cur.execute("SELECT * FROM products INNER JOIN money on money.product_id =products.id ORDER BY amount ASC")
    else:
        cur.execute("SELECT * FROM products INNER JOIN money on money.product_id =products.id ORDER BY amount DESC")
    conn.commit()
    result=cur.fetchall()
    return result


def findProductbyId(id):
    # CONNECT
    conn = psycopg2.connect("dbname=e_shop_l2_v2 user=postgres password=12345")
    cur  = conn.cursor()
    #QUERY
    cur.execute(f"SELECT * FROM products JOIN money on money.product_id =products.id WHERE id = {id}")
    conn.commit()
    result=cur.fetchall()
    return result

#########################################################

# createProduct("XBox 0.5", 900, "USD")
# products = allProducts(False)
# for p in products:
#     print(p)

product=findProductbyId(12)
print(product)