NAME="streamlit"
echo "docker run -it -d -p 8501:8501 -v $(pwd):/app --name $NAME -d --restart unless-stopped $NAME-img"
docker run -it -d -p 8501:8501 -v $(pwd):/app --name $NAME -d --restart unless-stopped $NAME-img
