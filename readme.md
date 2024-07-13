# 3D GLTF/GLB Viewer

This is a Streamlit-based web application that allows users to upload and visualize 3D models in GLTF and GLB formats. The application uses `trimesh` to load and parse the 3D models and `plotly` to render the 3D visualizations.

## Features

- Upload GLTF/GLB files
- Visualize 3D models
- Display model metadata (number of vertices and faces)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/3d-viewer.git
    cd 3d-viewer
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the App Locally

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and navigate to `http://localhost:8501`.

## Deploying on Streamlit Cloud

1. Push your project to a GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and sign in.
3. Create a new app and link it to your GitHub repository.
4. Select the appropriate branch and `app.py` file.
5. Deploy the app.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
