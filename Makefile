build:
	docker build -t tps .

run:
	docker run -p 8000:8000 -p 5173:5173 \
	-v $(PWD)/client/public/Data:/app/client/public/Data tps

dockerdelete:
	sudo systemctl stop docker
	sudo rm -rf /var/lib/docker
	sudo systemctl start docker
