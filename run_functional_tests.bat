docker-compose.exe -f .\docker-compose-stage.yml down --remove-orphans
docker-compose.exe -f .\docker-compose-stage.yml up -d
docker-compose.exe run --rm web python ./manage.py test functional_tests