from flask import Flask, jsonify
from flask_cors import CORS
from db import get_db_connection

app = Flask(__name__)
CORS(app)

# 🔹 API 1: Get all areas
@app.route('/areas')
def get_areas():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM areas")
        rows = cursor.fetchall()
        data = [dict(row) for row in rows]
    finally:
        conn.close()

    return jsonify(data)


# 🔹 API 2: Get all hospitals
@app.route('/hospitals')
def get_hospitals():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM hospitals")
        rows = cursor.fetchall()
        data = [dict(row) for row in rows]
    finally:
        conn.close()

    return jsonify(data)


# 🔹 API 3: Coverage with Smart Insight (MAIN API)
@app.route('/coverage')
def get_coverage():
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    SELECT 
        a.name AS area_name,
        a.population,
        a.latitude,
        a.longitude,
        c.nearest_hospital_distance,
        c.hospital_count,
        c.coverage_status
    FROM coverage c
    JOIN areas a ON c.area_id = a.area_id;
    """

    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        data = [dict(row) for row in rows]

        # 🔥 SMART INSIGHT: Critical Zones
        for area in data:
            if area["population"] > 50000 and area["hospital_count"] <= 2:
                area["critical_zone"] = True
            else:
                area["critical_zone"] = False

    finally:
        conn.close()

    return jsonify(data)


# 🔹 API 4: Mapping (JOIN across tables)
@app.route('/mapping')
def get_mapping():
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    SELECT 
        a.name AS area,
        h.name AS hospital,
        m.distance
    FROM area_hospital_map m
    JOIN areas a ON m.area_id = a.area_id
    JOIN hospitals h ON m.hospital_id = h.hospital_id;
    """

    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        data = [dict(row) for row in rows]
    finally:
        conn.close()

    return jsonify(data)


# 🔹 API 5: Roads (to ensure all tables are used 🔥)
@app.route('/roads')
def get_roads():
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    SELECT 
        r.name AS road_name,
        a.name AS area_name
    FROM roads r
    JOIN areas a ON r.area_id = a.area_id;
    """

    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        data = [dict(row) for row in rows]
    finally:
        conn.close()

    return jsonify(data)


# 🚀 Run Server
import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)