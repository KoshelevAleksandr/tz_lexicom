up:
	docker compose -f docker-compose-local.yaml up -d --build

stop:
	docker compose -f docker-compose-local.yaml stop

down:
	docker compose -f docker-compose-local.yaml down && docker network prune --force
