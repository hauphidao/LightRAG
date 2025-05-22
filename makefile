IMAGE_NAME=lightrag

log:
	sudo docker compose logs -f

down:
	sudo docker compose down

up:
	sudo docker rmi $$(docker images -q $(IMAGE_NAME)) || true
	sudo docker compose up -d --build --force-recreate