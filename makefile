<<<<<<< HEAD
IMAGE_NAME=lightrag

up:
	sudo docker rmi $$(docker images -q $(IMAGE_NAME)) || true
=======
IMAGE_NAME=lightrag

log:
	sudo docker compose logs -f

down:
	sudo docker compose down

up:
	sudo docker rmi $$(docker images -q $(IMAGE_NAME)) || true
>>>>>>> 861b104ae31676abc8e8e39e863273283747f490
	sudo docker compose up -d --build --force-recreate