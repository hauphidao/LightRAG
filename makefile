IMAGE_NAME=lightrag

up:
	sudo docker rmi $$(docker images -q $(IMAGE_NAME)) || true
	sudo docker compose up -d --build --force-recreate