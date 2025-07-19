from flask import Flask, render_template, request
import json, csv


app = Flask(__name__)

def load_products_json():
    with open('products.json') as f:
        return json.load(f)

def load_products_csv():
    products = []
    with open('products.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
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
    else:
        data = []
        error = 'Wrong source'

    # 2. Filter by id if provided
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

    # 3. Render
    return render_template(
        'product_display.html',
        products=data,
        error=error
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)