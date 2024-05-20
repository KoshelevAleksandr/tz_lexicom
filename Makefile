up:
	docker compose -f docker-compose-local.yaml up -d

stop:
	docker compose -f docker-compose-local.yaml stop

down:
	docker compose -f docker-compose-local.yaml down && docker network prune --force
