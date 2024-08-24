from flask import request, jsonify, send_file, current_app as app
import os
import uuid
import pandas as pd
from .transformations import apply_transformations
from .visualizations import generate_visualization

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file and file.filename.endswith('.csv'):
        file_id = str(uuid.uuid4())
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{file_id}.csv")
        file.save(file_path)
        return jsonify({"message": "File uploaded successfully", "file_id": file_id})
    return jsonify({"error": "Invalid file format"}), 400

@app.route('/summary/<file_id>', methods=['GET'])
def data_summary(file_id):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{file_id}.csv")
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        summary = df.describe().to_dict()
        data_types = df.dtypes.apply(lambda x: x.name).to_dict()
        for column, dtype in data_types.items():
            summary[column]['dtype'] = dtype
        return jsonify({"summary": summary})
    return jsonify({"error": "File not found"}), 404

@app.route('/transform/<file_id>', methods=['POST'])
def transform_data(file_id):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{file_id}.csv")
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        transformations = request.json.get('transformations', {})
        df_transformed = apply_transformations(df, transformations)
        new_file_id = str(uuid.uuid4())
        new_file_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{new_file_id}.csv")
        df_transformed.to_csv(new_file_path, index=False)
        return jsonify({"message": "Transformations applied successfully", "file_id": new_file_id})
    return jsonify({"error": "File not found"}), 404

@app.route('/visualize/<file_id>', methods=['GET'])
def visualize_data(file_id):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{file_id}.csv")
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        chart_type = request.args.get('chart_type')
        columns = request.args.getlist('columns')
        if chart_type and columns:
            img_path = generate_visualization(df, chart_type, columns)
            return send_file(img_path, mimetype='image/png')
    return jsonify({"error": "File not found"}), 404
