from flask import Flask, render_template, request
import json, csv, sqlite3


app = Flask(__name__)


def load_products_json():
    with open('products.json') as f:
        return json.load(f)

def load_products_csv():
    products = []
    with open('products.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id']    = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def load_products_sql():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products;')
        for row in cursor.fetchall():
            products.append({
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            })
    except sqlite3.Error as e:
        print(f"[DB ERROR] {e}")
    finally:
        conn.close()
    return products

@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    id_str = request.args.get('id', None)
    error = None


    if source == 'json':
        data = load_products_json()
    elif source == 'csv':
        data = load_products_csv()
    elif source == 'sql':
        data = load_products_sql()
    else:
        data = []
        error = 'Wrong source'

    if not error and id_str is not None:
        try:
            pid = int(id_str)
        except ValueError:
            data = []
            error = 'Invalid id'
        else:
            filtered = [p for p in data if p['id'] == pid]
            if not filtered:
                error = 'Product not found'
            data = filtered

    return render_template(
        'product_display.html',
        products=data,
        error=error
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)
