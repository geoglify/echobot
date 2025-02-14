import os
import psycopg2
from flask import Flask, request, jsonify

app = Flask(__name__)

# Read the PostgreSQL connection URL from the environment variable
DATABASE_URL = os.getenv('DATABASE_URL')

# If it's not defined, raise an error
if not DATABASE_URL:
    raise ValueError("A variável de ambiente DATABASE_URL não está definida.")

# Define an endpoint to test the application
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    imo = data['imo']

    # Connect to the database
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    # Get the ship name from the database
    cur.execute("SELECT name FROM ships WHERE imo = '%s'", (imo,))
    result = cur.fetchone()

    cur.close()
    conn.close()

    # Return the result
    if result:
        return jsonify({'name': result[0]})
    else:
        return jsonify({'error': 'No data found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
