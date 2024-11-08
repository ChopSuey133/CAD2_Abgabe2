# CAD2_Abgabe2
Cloud Architecture Design 2 - Abgabe 2 - FH Joanneum
Es funktioniert eigentlich gar nix.

docker tag uebung2_backend <dockerhub_username>/my-backend-app:latest
docker tag uebung2_proxy <dockerhub_username>/my-nginx-proxy:latest
docker tag uebung2_frontend <dockerhub_username>/my-frontend-app:latest

docker push <dockerhub_username>/my-backend-app:latest
docker push <dockerhub_username>/my-nginx-proxy:latest
docker push <dockerhub_username>/my-frontend-app:latest
