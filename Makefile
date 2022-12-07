jupyter:
	docker run --rm -it -p 8888:8888 -v $(shell pwd):/usr/src/app pantry_manager_image_docker 

bash:
	docker run --rm -it -p 8888:8888 -v $(shell pwd):/usr/src/app --env-file ./.env pantry_manager_image_docker /bin/bash


