NAME="streamlit"
IMG="$NAME-img"
echo "docker run -p 8501:8501 $IMG"
docker run -p 8501:8501 $IMG -v $(pwd):/home/streamlit
